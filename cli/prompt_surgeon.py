#!/usr/bin/env python3
"""Prompt Surgeon CLI — sharpen prompts using any LLM you configure."""
import argparse, json, os, sys, requests

MODES = {
    "clarity": "You are a prompt engineering expert. Rewrite the user's prompt to be maximally clear, specific, and unambiguous while preserving intent. Return ONLY the rewritten prompt with no explanation.",
    "concise": "You are a prompt engineering expert. Rewrite the user's prompt to be as short and efficient as possible while preserving all key intent and constraints. Remove fluff, combine instructions, use direct language. Return ONLY the rewritten prompt.",
    "structured": "You are a prompt engineering expert. Restructure the user's prompt with clear sections: ROLE, TASK, CONSTRAINTS, OUTPUT_FORMAT, EXAMPLES. Add anything missing. Return ONLY the rewritten prompt.",
    "creative": "You are a prompt engineering expert. Rewrite the user's prompt to encourage more creative, unexpected, and novel outputs. Add open-ended framing, metaphorical language, and room for the model to surprise. Return ONLY the rewritten prompt.",
}

def improve(prompt, mode="clarity", model=None, api_key=None, base_url=None):
    system = MODES.get(mode, MODES["clarity"])
    
    # Default: try Hermes config, then env vars, then Ollama local
    if not base_url:
        base_url = os.environ.get("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
    if not api_key:
        api_key = os.environ.get("OPENROUTER_API_KEY", "")
    if not model:
        model = os.environ.get("MODEL", "deepseek/deepseek-v4-flash")
    
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 4096,
        "temperature": 0.3,
    }
    
    try:
        r = requests.post(f"{base_url}/chat/completions", headers=headers, json=payload, timeout=30)
        r.raise_for_status()
        data = r.json()
        return data["choices"][0]["message"]["content"]
    except requests.exceptions.ConnectionError:
        # Fallback: try Ollama local
        ollama_url = "http://localhost:11434/api/generate"
        ollama_payload = {
            "model": model.replace("ollama/", ""),
            "prompt": f"{system}\n\nUser prompt: {prompt}\n\nRewritten prompt:",
            "stream": False
        }
        r = requests.post(ollama_url, json=ollama_payload, timeout=30)
        return r.json().get("response", "")

def main():
    parser = argparse.ArgumentParser(description="✂️ Prompt Surgeon — Sharpen your prompts.")
    parser.add_argument("prompt", nargs="?", help="The prompt to improve")
    parser.add_argument("--mode", "-m", choices=MODES.keys(), default="clarity",
                        help="Improvement mode (default: clarity)")
    parser.add_argument("--model", help="Model to use (e.g., qwen3.6, claude-sonnet-4)")
    parser.add_argument("--api-key", help="API key (default: OPENROUTER_API_KEY env)")
    parser.add_argument("--base-url", help="API base URL (default: OpenRouter)")
    parser.add_argument("--pipe", "-p", action="store_true", help="Read prompt from stdin")
    
    args = parser.parse_args()
    
    if args.pipe or not args.prompt:
        prompt = sys.stdin.read().strip()
    else:
        prompt = args.prompt
    
    if not prompt:
        parser.print_help()
        sys.exit(1)
    
    result = improve(prompt, args.mode, args.model, args.api_key, args.base_url)
    print(result)

if __name__ == "__main__":
    main()