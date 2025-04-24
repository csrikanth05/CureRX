import os, asyncio
from google import genai
from google.genai import types
from utils.config import GEMINI_KEY

client = genai.Client(api_key=GEMINI_KEY)
MODEL = "gemini-2.0-flash"

PROMPT = """
You are a biomedical knowledge assistant. Return detailed information about the protein "{query}" in the following structured format:

Name: [Full protein name and alias]
Basic: [Short introduction about the protein]
Structure: [Summary of the structural features]
Functions: [Detailed description of biological functions]
Diseases: [Diseases or syndromes associated]
Interactions: [Key interactions with other molecules or proteins]
Activities: [Biological activities or processes]
Drug Targets: [Any known or experimental drugs targeting this protein]

Please respond in plain text with each section starting with the section name followed by a colon.
"""



async def ask_model(query: str):
    contents=[types.Content(role="user",
            parts=[types.Part(text=PROMPT.format(query=query))])]
    cfg=types.GenerateContentConfig(response_mime_type="text/plain")
    chunks=client.models.generate_content_stream(model=MODEL,
                                                 contents=contents,
                                                 config=cfg)
    txt="".join([c.text for c in chunks])
    return txt   # already JSON string
