export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');
  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'POST') return res.status(405).json({ error: 'POST only' });

  const { prompt, mode, apiKey, model, baseUrl } = req.body;
  if (!prompt || prompt.length > 10000) {
    return res.status(400).json({ error: 'Prompt required (max 10k chars)' });
  }
  if (!apiKey) {
    return res.status(400).json({ error: 'API key required — bring your own from openrouter.ai/keys' });
  }

  const systemPrompts = {
    clarity: 'You are a prompt engineering expert. Rewrite the user\'s prompt to be maximally clear, specific, and unambiguous while preserving intent. Return ONLY the rewritten prompt with no explanation.',
    concise: 'You are a prompt engineering expert. Rewrite the user\'s prompt to be as short and efficient as possible while preserving all key intent and constraints. Remove fluff, combine instructions, use direct language. Return ONLY the rewritten prompt.',
    structured: 'You are a prompt engineering expert. Restructure the user\'s prompt with clear sections: ROLE, TASK, CONSTRAINTS, OUTPUT_FORMAT, EXAMPLES. Add anything missing. Return ONLY the rewritten prompt.',
    creative: 'You are a prompt engineering expert. Rewrite the user\'s prompt to encourage more creative, unexpected, and novel outputs. Add open-ended framing, metaphorical language, and room for the model to surprise. Return ONLY the rewritten prompt.',
  };

  try {
    const response = await fetch(baseUrl || 'https://openrouter.ai/api/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${apiKey}`,
        'Content-Type': 'application/json',
        'HTTP-Referer': 'https://prompt-surgeon.vercel.app',
      },
      body: JSON.stringify({
        model: model || 'deepseek/deepseek-v4-flash',
        messages: [
          { role: 'system', content: systemPrompts[mode] || systemPrompts.clarity },
          { role: 'user', content: prompt }
        ],
        max_tokens: 4096,
        temperature: 0.3,
      }),
    });

    const data = await response.json();
    if (!response.ok) {
      return res.status(response.status).json({ error: data.error?.message || 'API error' });
    }

    const improved = data.choices?.[0]?.message?.content || '';
    res.json({
      original: prompt,
      improved,
      mode: mode || 'clarity',
      tokens: { in: data.usage?.prompt_tokens || 0, out: data.usage?.completion_tokens || 0 }
    });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
}