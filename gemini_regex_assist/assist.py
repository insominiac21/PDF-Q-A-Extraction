"""
gemini_regex_assist/assist.py
Uses Gemini API to propose regex patterns for question/answer markers if confidence is low.
"""

import os
import requests

def propose_regex_patterns(snippets, failures):
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise EnvironmentError("Gemini API key not found.")
    url = "https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key=" + api_key
    prompt = {
        "contents": [{
            "parts": [{
                "text": f"Suggest regex patterns for question and answer markers.\nExamples:\n{snippets}\nFailures:\n{failures}\nReturn only regex candidates and a short explanation."}]
        }]
    }
    response = requests.post(url, json=prompt)
    if response.status_code == 200:
        result = response.json()
        # Extract regex candidates from Gemini response
        # ...existing code...
        return result
    else:
        raise RuntimeError(f"Gemini API error: {response.status_code}")
