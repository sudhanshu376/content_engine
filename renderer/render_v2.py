import json
from pathlib import Path

from moviepy import (
    VideoFileClip,
    AudioFileClip,
    concatenate_videoclips,
    concatenate_audioclips
)
from run_manager import get_latest_run

run_dir = get_latest_run()

print(
    f"Using run: {run_dir.name}"
)

with open(
    run_dir / "timeline.json",
    "r",
    encoding="utf-8"
) as f:
    timeline = json.load(f)

video_clips = []
audio_clips = []

for scene in timeline:

    scene_num = scene["scene"]
    duration = scene["duration"]

    video_file = (
        run_dir
    / "video"
    / f"scene_{scene_num}"
    / "clip_1.mp4"
    )

    audio_file = (
        run_dir
    / "audio"
    / f"scene_{scene_num}.mp3"
    )

    if not video_file.exists():
        print(
            f"Missing video for scene {scene_num}"
        )
        continue

    video = VideoFileClip(
        str(video_file)
    )

    audio = AudioFileClip(
        str(audio_file)
    )

    if video.duration < duration:

        loops_needed = int(
            duration / video.duration
        ) + 1

        video = concatenate_videoclips(
            [video] * loops_needed
        )

    video = video.subclipped(
        0,
        duration
    )

    video = video.resized(
        height=1920
    )

    if video.w > 1080:

        video = video.cropped(
            x_center=video.w / 2,
            y_center=video.h / 2,
            width=1080,
            height=1920
        )

    video = video.with_audio(audio)

    video_clips.append(video)
    audio_clips.append(audio)

final_video = concatenate_videoclips(
    video_clips,
    method="compose"
)

output_file = (
    run_dir
    / "final_video_v2.mp4"
)

final_video.write_videofile(
    str(output_file),
    codec="libx264",
    audio_codec="aac",
    fps=30
)

print(
    f"Saved: {output_file}"
)