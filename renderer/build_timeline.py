import json
from pathlib import Path

from mutagen.mp3 import MP3

with open(
    "output/content_spec.json",
    "r",
    encoding="utf-8"
) as f:
    content = json.load(f)

scenes = content["scenes"]

timeline = []

audio_dir = Path("assets/audio")

current_time = 0

for i, scene in enumerate(
    scenes,
    start=1
):

    audio_file = (
        audio_dir /
        f"scene_{i}.mp3"
    )

    duration = MP3(
        str(audio_file)
    ).info.length

    timeline.append({
        "scene": i,
        "start": round(
            current_time,
            2
        ),
        "end": round(
            current_time + duration,
            2
        ),
        "duration": round(
            duration,
            2
        ),
        "scene_type": scene.get(
        "scene_type",
        "stock"
        ),
        "narration": scene["narration"],
        "visual_query": scene["visual_query"]
    })

    current_time += duration

Path("output").mkdir(
    exist_ok=True
)

with open(
    "output/timeline.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        timeline,
        f,
        indent=2
    )

print(
    "Saved timeline.json"
)