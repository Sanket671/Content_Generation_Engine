# Content Generation Engine

This repository contains a small pipeline that generates SEO-optimized blog posts using trending keywords and a language model, then renders them into complete HTML files using a reusable template.

Full technical documentation is included in `DOCUMENTATION_FULL.md` (recommended reading for maintainers).

Quick start
-----------

1. Create and activate a Python virtual environment.

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Provide your Groq API key in `.env`:

```text
GROQ_API_KEY=your_key_here
```

4. Optionally edit `company_config.json` with the target company metadata.

5. Run the pipeline:

```bash
python main.py
```

What the pipeline does
----------------------
- Fetches trending keywords using `pytrends` (`trends_fetcher.py`), with a built-in fallback list.
- Produces a short trend analysis via `trend_analyzer.py` (LLM-driven).
- Generates a full SEO blog via `blog_generator.py` using the prompts in `prompts.py` and the LLM (`groq_client.py`).
- Converts model output (Markdown) to HTML, injects it into `templates/blog_template.html`, and writes the file to `generated_blogs/`.

Important files
---------------
- `main.py` — orchestrator that runs the end-to-end flow.
- `trends_fetcher.py` — collects trending queries from Google Trends.
- `trend_analyzer.py` — analyzes keywords using the LLM.
- `blog_generator.py` — builds prompts, converts content to HTML, and writes the output.
- `groq_client.py` — Groq API wrapper (reads `GROQ_API_KEY` from `.env`).
- `prompts.py` — system prompts used to steer the model.
- `templates/blog_template.html` — HTML shell with `{{BLOG_CONTENT}}` placeholder.
- `DOCUMENTATION_FULL.md` — in-depth technical documentation for this project.

Notes & caveats
--------------
- Ensure `.env` contains a valid `GROQ_API_KEY` when you want live model responses. If the key is missing or invalid, the system falls back to a built-in placeholder blog.
- Google Trends (`pytrends`) may rate-limit requests. The code handles this by returning fallback keywords; consider adding retry/backoff for production use.
- Generated HTML files are saved to `generated_blogs/` with filenames like `netflix_blog_20260313_094001.html`.

Next steps (recommended)
------------------------
- Read `DOCUMENTATION_FULL.md` for detailed architecture, prompts, failure modes, and suggested improvements.
- I can add an audit index (`generated_blogs/index.json`), stricter prompt contracts (YAML frontmatter), unit tests, or sanitization for model output — tell me which to prioritize.

