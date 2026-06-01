import json
import os
from pathlib import Path

import requests
from dotenv import load_dotenv
from run_manager import get_latest_run

load_dotenv()

PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")

if not PEXELS_API_KEY:
    raise Exception("PEXELS_API_KEY not found")

run_dir = get_latest_run()

print(
    f"Using run: {run_dir.name}"
)

headers = {
    "Authorization": PEXELS_API_KEY
}

with open(
    run_dir / "content_spec.json",
    "r",
    encoding="utf-8"
) as f:
    content = json.load(f)

scenes = content["scenes"]

base_dir = run_dir / "video"
base_dir.mkdir(parents=True, exist_ok=True)

for scene_index, scene in enumerate(scenes, start=1):

    query = scene["visual_query"]

    print(f"\nScene {scene_index}")
    print(f"Searching: {query}")

    response = requests.get(
        "https://api.pexels.com/videos/search",
        headers=headers,
        params={
            "query": query,
            "per_page": 5
        }
    )

    response.raise_for_status()

    data = response.json()

    videos = data.get("videos", [])

    if not videos:
        print("No videos found")
        continue

    scene_dir = base_dir / f"scene_{scene_index}"
    scene_dir.mkdir(exist_ok=True)

    clips_downloaded = 0

    for video in videos:

        if clips_downloaded >= 3:
            break

        video_files = video.get("video_files", [])

        if not video_files:
            continue

        best_file = max(
            video_files,
            key=lambda x: x.get("width", 0)
        )

        video_url = best_file["link"]

        output_file = (
            scene_dir /
            f"clip_{clips_downloaded + 1}.mp4"
        )

        print(f"Downloading -> {output_file.name}")

        video_content = requests.get(video_url).content

        with open(output_file, "wb") as f:
            f.write(video_content)

        clips_downloaded += 1

    print(
        f"Downloaded {clips_downloaded} clips"
    )

print("\nDone.")