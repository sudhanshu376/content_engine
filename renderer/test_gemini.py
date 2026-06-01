import os
import json
from pathlib import Path

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

with open("prompts/shorts_prompt.txt", "r", encoding="utf-8") as f:
    system_prompt = f.read()

topic = input("Enter topic: ")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"{system_prompt}\n\nTOPIC:\n{topic}"
)

raw_text = response.text.strip()

# Remove markdown fences if Gemini adds them
if raw_text.startswith("```json"):
    raw_text = raw_text.replace("```json", "", 1)

if raw_text.endswith("```"):
    raw_text = raw_text[:-3]

raw_text = raw_text.strip()

content_spec = json.loads(raw_text)

output_dir = Path("output")
output_dir.mkdir(exist_ok=True)

output_file = output_dir / "content_spec.json"

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(content_spec, f, indent=2)

print("\nSaved:")
print(output_file.resolve())