# ✂️ Prompt Surgeon

**Cut the fluff. Sharpen your prompts.** Works with any LLM — local or cloud. Open source (MIT).

---

## 🚀 Quick Install

### Option 1: Hermes Agent (easiest — 10 seconds)

```bash
hermes skills install prompt-surgeon
```

Then in any chat session:

```
Surgeon this: "Write a blog about AI"
Make it concise: [paste your prompt]
Structured mode: [paste your prompt]
```

### Option 2: CLI (any terminal — 30 seconds)

```bash
# Download
curl -sOL https://raw.githubusercontent.com/tapnothing2023-prog/prompt-surgeon/main/cli/prompt_surgeon.py
chmod +x prompt_surgeon.py

# Set your API key (get one free at https://openrouter.ai/keys)
export OPENROUTER_API_KEY="sk-or-v1-..."

# Use it
./prompt_surgeon.py "Write a blog about AI" --mode concise
```

Or pipe text:

```bash
cat my_prompt.txt | ./prompt_surgeon.py --pipe --mode structured
```

### Option 3: Web UI (no install — 2 seconds)

1. Go to **https://prompt-surgeon.vercel.app**
2. Paste your API key from https://openrouter.ai/keys
3. Paste your prompt and click **Improve**

---

## 🎯 How To Use

### Modes

| Mode | What It Does | When To Use |
|------|-------------|-------------|
| **🎯 Clarity** | Removes vague language. Makes instructions explicit. | Complex tasks, multi-step instructions |
| **✂️ Concise** | Cuts fluff. Keeps all key info. | Saving tokens, tight prompts |
| **📋 Structured** | Formats as ROLE / TASK / CONSTRAINTS / OUTPUT | Developer prompts, API calls |
| **✨ Creative** | Opens up framing for unexpected outputs | Brainstorming, content creation |

### Examples

**Before (vague):**
```
Write something about AI agents
```

**After (Clarity mode):**
```
Write a 500-word blog post introducing AI agents to non-technical readers.
Include: definition, 3 real-world examples, and common misconceptions.
Target audience: professionals with no machine learning background.
```

**Before (verbose):**
```
I would like you to please write a really good blog post about artificial intelligence agents and how they work and what they can do for people, make it engaging and fun to read okay thanks
```

**After (Concise mode):**
```
Write an engaging 400-word blog post about AI agents: how they work, what they do, and why they matter. Target: general audience. No jargon.
```

---

## 💰 Cost

- **Local models** (Qwen, Llama via Ollama): **$0 forever**
- **Cloud models** (OpenRouter): ~$0.0002 per improvement — $1 = ~5,000 improvements
- **Your API key, your cost, your control** — no subscriptions, no surprises

---

## 🧠 How It Works

```
You paste a prompt → Prompt Surgeon adds a specialist system prompt → Your LLM rewrites it → You get a sharper version
```

The "surgeon" is just a smart system prompt — no data leaves your model, no servers store your prompts, no tracking.

---

## 🔧 Advanced

### Use any model

```bash
# CLI — specify model
./prompt_surgeon.py "Explain quantum computing" --mode structured --model claude-sonnet-4

# CLI — use local Qwen (free)
./prompt_surgeon.py "Write a poem" --mode creative --model qwen3.6 --base-url http://localhost:11434/v1
```

### Web UI — run locally

```bash
git clone https://github.com/tapnothing2023-prog/prompt-surgeon.git
cd prompt-surgeon/web
python3 -m http.server 8080
# Open http://localhost:8080
```

---

## 📦 What's Included

```
prompt-surgeon/
├── cli/prompt_surgeon.py      # CLI tool (works anywhere)
├── web/
│   ├── index.html             # Web UI (single HTML file)
│   └── api/improve.js         # Serverless function (Vercel)
├── README.md                  # This file
└── LICENSE                    # MIT — do whatever you want
```

---

## 🌐 Links

- **Web UI:** https://prompt-surgeon.vercel.app
- **GitHub:** https://github.com/tapnothing2023-prog/prompt-surgeon
- **Hermes skill:** `hermes skills install prompt-surgeon`
- **Get API key:** https://openrouter.ai/keys
- **License:** MIT — free to use, modify, share

---

Built for the brotherhood. Open source for everyone.