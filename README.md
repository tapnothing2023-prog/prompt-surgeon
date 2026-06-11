# ✂️ Prompt Surgeon

**Cut the fluff. Sharpen your prompts.**

A prompt engineering tool that rewrites your prompts for clarity, conciseness, structure, or creativity — using any LLM you configure. Works as a Hermes Agent skill, a standalone CLI, and a web UI.

## Why

Most people write prompts that are too vague, too verbose, or poorly structured. This costs tokens (money) and produces weak outputs. Prompt Surgeon fixes that in one call.

## How It Works

```
"Write a blog about AI for beginners"
        ↓  (concise mode)
"Write a 500-word blog introducing AI concepts to non-technical readers. Include: definition, real-world examples, and learning resources. Target audience: professionals with no ML background."
```

## Features

- **Four modes**: Clarity (🎯), Concise (✂️), Structured (📋), Creative (✨)
- **Zero additional cost** — uses your existing model (local Qwen = free, cloud models = pennies)
- **Works everywhere**: Hermes Agent, CLI, or web browser
- **Open source** (MIT) — no vendor lock-in, no subscription

## Installation & Usage

### Hermes Agent (skill)

```bash
hermes skills install prompt-surgeon
```

Then in any session:

```
Surgeon this for clarity: "write about AI agents"
Make this concise: [paste prompt]
Structured mode: [paste prompt]
```

### CLI

```bash
pip install prompt-surgeon

# Default mode (clarity)
prompt-surgeon "Write a blog post about AI"

# Specific mode
prompt-surgeon --mode concise "Explain machine learning"
prompt-surgeon --mode structured "Build a recommendation system"

# Use a custom model
prompt-surgeon --model qwen3.6 --mode creative "Write a sci-fi story"
```

### Web UI

```bash
# Deploy anywhere (Vercel, Netlify, static hosting)
cd web/
python3 -m http.server 8080
# → http://localhost:8080
```

## API (for integration)

```
POST /api/improve
{
  "prompt": "your prompt here",
  "mode": "clarity|concise|structured|creative",
  "model": "optional model override"
}
```

## Modes

| Mode | System Prompt | Best For |
|------|--------------|----------|
| **clarity** | Eliminate ambiguity, make specifics explicit | Complex instructions, multi-step tasks |
| **concise** | Strip fluff, preserve all key constraints | Token optimization, cost saving |
| **structured** | ROLE / TASK / CONSTRAINTS / OUTPUT format | Developer prompts, API usage |
| **creative** | Open-ended framing, metaphorical language | Brainstorming, content creation |

## Cost

- **Local models** (Qwen, Llama via Ollama): $0
- **Cloud models** (DeepSeek, Claude, GPT via your key): ~$0.0002 per improvement

## Architecture

```
User Input → Prompt Surgeon Engine → Your LLM (any provider) → Improved Prompt
```

The engine is a system prompt + structured call to your existing model. No external services, no data leakage, no subscription.

## License

MIT — free to use, modify, distribute. Go build.

---

Built by RED for the brotherhood. Open source for everyone.