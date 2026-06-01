import json
from pathlib import Path

from mutagen.mp3 import MP3
from run_manager import get_latest_run

run_dir = get_latest_run()
print(
    f"Using run: {run_dir.name}"
)

with open(
    run_dir / "content_spec.json",
    "r",
    encoding="utf-8"
) as f:
    content = json.load(f)

scenes = content["scenes"]

timeline = []

audio_dir = run_dir / "audio"

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

with open(
    run_dir / "timeline.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        timeline,
        f,
        indent=2
    )

print(
    f"Saved: {run_dir / 'timeline.json'}"
)