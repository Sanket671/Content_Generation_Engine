import os
from groq_client import ask_groq
from prompts import BLOG_GENERATION_SYSTEM_PROMPT

OUTPUT_DIR = "generated_blogs"


def generate_blog(keywords):

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    keyword_text = ", ".join(keywords)

    user_prompt = f"""
Use these trending sports keywords:

{keyword_text}

Write a full SEO optimized blog for Reticulo Sports.
"""

    blog = ask_groq(
        BLOG_GENERATION_SYSTEM_PROMPT,
        user_prompt
    )

    path = os.path.join(
        OUTPUT_DIR,
        "reticulo_trending_blog.txt"
    )

    with open(path, "w", encoding="utf-8") as f:
        f.write(blog)

    return path