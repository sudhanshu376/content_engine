from pathlib import Path

from moviepy import (
    VideoFileClip,
    AudioFileClip,
    concatenate_videoclips
)

audio_path = "output/voice.mp3"

video_dir = Path("assets/video")

video_files = sorted(video_dir.glob("*.mp4"))

if not video_files:
    raise Exception("No video clips found")

audio = AudioFileClip(audio_path)

voice_duration = audio.duration

clip_duration = voice_duration / len(video_files)

clips = []

for file in video_files:

    clip = VideoFileClip(str(file))

    clip = clip.subclipped(
        0,
        min(clip.duration, clip_duration)
    )

    clip = clip.resized(height=1920)

    if clip.w > 1080:
        x_center = clip.w / 2

        clip = clip.cropped(
            x_center=x_center,
            width=1080,
            y_center=clip.h / 2,
            height=1920
        )

    clips.append(clip)

final_video = concatenate_videoclips(
    clips,
    method="compose"
)

final_video = final_video.with_audio(audio)

output_path = "output/final_video.mp4"

final_video.write_videofile(
    output_path,
    codec="libx264",
    audio_codec="aac",
    fps=30
)

print(f"Saved: {output_path}")