import json
import asyncio
from pathlib import Path

import edge_tts

from run_manager import get_latest_run

VOICE = "en-US-AvaNeural"

async def generate_audio(text, output_file):

    communicate = edge_tts.Communicate(
        text=text,
        voice=VOICE,
        rate="-5%"
    )

    await communicate.save(str(output_file))


async def main():
    run_dir = get_latest_run()
    print(f"Using run: {run_dir.name}")
    with open(
    run_dir / "content_spec.json",
    "r",
    encoding="utf-8"
    ) as f:
        content = json.load(f)

    scenes = content["scenes"]

    audio_dir = run_dir / "audio"
    audio_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    for i, scene in enumerate(
        scenes,
        start=1
    ):

        narration = scene["narration"]

        output_file = (
            audio_dir /
            f"scene_{i}.mp3"
        )

        print(
            f"Generating scene {i}"
        )

        await generate_audio(
            narration,
            output_file
        )

    print("Done")


asyncio.run(main())