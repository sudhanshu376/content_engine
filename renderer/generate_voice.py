import json
import asyncio
from pathlib import Path

import edge_tts

VOICE = "en-US-AvaNeural"

async def main():
    with open("output/content_spec.json", "r", encoding="utf-8") as f:
        content = json.load(f)

    script = content["script"]

    output_file = Path("output") / "voice.mp3"

    communicate = edge_tts.Communicate(
        text=script,
        voice=VOICE,
        rate="-5%"
    )

    await communicate.save(str(output_file))

    print(f"Saved voice to: {output_file}")

asyncio.run(main())