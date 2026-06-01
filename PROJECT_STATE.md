PROJECT: Future Economy AI Content Engine (MVP_v1 Complete, Starting MVP_v2)

GOAL:
Build a semi-automated faceless short-form content system for:

* YouTube Shorts
* Instagram Reels
* X

NICHE: Future Economy

Topics include:

* AI
* Robotics
* Semiconductors
* Future Jobs
* Energy
* Space Economy
* Infrastructure
* Fintech
* Automation
* Technology

CONTENT STYLE TARGET:
ColdFusion + Vox (short-form)

NOT:

* Generic AI news
* Generic finance news
* Generic stock footage channel

QUESTION BEHIND EVERY VIDEO:
"What technologies, companies, and systems are reshaping civilization?"

CONSTRAINTS:

* Free-first
* Open-source whenever possible
* Local-first
* Windows
* i5 CPU
* 16GB RAM
* No GPU
* 300 Mbps internet
* Future VPS migration

CURRENT PROJECT LOCATION:
C:\ai_projects\by_sudhanshu

CURRENT ARCHITECTURE (WORKING)

Topic
↓
Gemini
↓
content_spec.json
↓
Scene Audio Generation (Edge-TTS)
↓
Timeline Generation
↓
Scene-Based Asset Downloads
↓
Renderer
↓
Video

TOOLS CURRENTLY WORKING:

* Python
* VS Code
* FFmpeg
* MoviePy
* Gemini API
* Edge-TTS
* Pexels API
* n8n
* Docker

CURRENT FOLDER STRUCTURE:

├── Scripts/                  # Python Virtual Environment (Windows venv)
│   ├── activate.bat
│   ├── pip.exe
│   ├── python.exe
│   └── [Other venv internal executables & scripts]
│
├── assets/                   # Input media assets
│   ├── audio/
│   │   └── scene_1.mp3 to scene_14.mp3
│   ├── images/
│   └── video/
│       └── scene_1/ to scene_14/
│           └── Each containing: clip_1.mp4, clip_2.mp4, clip_3.mp4
│
├── config/                   # Configuration files
│   └── settings.json
│
├── logs/                     # Log outputs
├── temp/                     # Temporary processing directory
├── templates/                # Layout/video templates
├── workflows/                # Automation workflows
├── scripts/                  # Miscellaneous automation scripts
│
├── prompts/                  # LLM Prompt storage
│   └── shorts_prompt.txt
│
├── renderer/                 # Core Python processing logic
│   ├── build_timeline.py
│   ├── download_assets.py
│   ├── generate_scene_audio.py
│   ├── generate_voice.py
│   ├── render_v2.py
│   ├── render_video.py
│   └── test_gemini.py
│
└── output/                   # Final rendered deliverables
├── content_spec.json
├── timeline.json
├── voice.mp3
├── final_video.mp4
└── final_video_v2.mp4

MVP_V1 RESULTS:

V1:

* Generic stock footage
* Weak visual relevance
* ~7/10 quality

MVP_v1 CONCLUSION

The largest quality improvement came from:
Scene Planning -> Scene-Based Visual Selection

NOT from:

* Better AI models
* More automation
* Faster rendering
* More footage

Future development should prioritize:
Visual storytelling quality over automation complexity.

V2 Scene-Based Rendering:

* Major improvement
* Visuals generally relevant
* Quality noticeably higher
* Rendering slower but acceptable

IMPORTANT LESSONS LEARNED:

1. Scene planning improved quality more than any technical optimization.

2) Pexels is not the problem.
   Bad search queries were the problem.

3. One scene = one visual concept.

4) Scene-specific footage performs much better than generic keywords.

5. The bottleneck is visual storytelling, not automation.

6) n8n is orchestration, not the product.

7. The Python content engine is the actual product.

CURRENT TIMELINE SYSTEM:

content_spec.json
↓
scene_1 narration
scene_2 narration
...
↓
scene_1.mp3
scene_2.mp3
...
↓
timeline.json
↓
scene-aware rendering

MVP_V2 GOAL:

Move away from:

* Stock footage only

Toward:

* Stock footage
* Graphics
* Logos
* Screenshots

NOT focusing on AI video generation.

AI images only when necessary for concepts that cannot be filmed.

TARGET VISUAL MIX:

40% Stock Footage
30% Graphics
20% Logos
10% Screenshots

AI Images: <5%

SUPPORTED SCENE TYPES FOR MVP_V2:

1. stock
   Examples:

* Data centers
* Factories
* Offices
* Scientists
* Solar farms
* Robotics

2. graphic
   Examples:

* Market cap
* Revenue
* Growth
* Comparisons
* Timelines
* Large numbers
* Text animation

3. logo
   Examples:

* NVIDIA
* OpenAI
* Tesla
* TSMC
* SpaceX

4. screenshot
   Examples:

* News headlines
* Research papers
* Company websites
* Product pages

MVP_V2 FIRST PRIORITIES:

1. Modify content_spec schema.

Scenes should include:

{
"scene_type": "stock|graphic|logo|screenshot"
}

2. Build graphic renderer.

3) Build logo scene renderer.

4. Build screenshot scene renderer.

5) Then build caption system.

Captions are intentionally postponed because better visuals provide more value than captions at the current stage.

LONG TERM N8N ROLE:

* Trend discovery
* Topic ranking
* Content queue
* Duplicate detection
* Telegram approval workflow
* Publishing
* Analytics feedback

n8n should orchestrate.

Python should create.

CURRENT STATUS:

MVP_v1 complete and functional.

Ready to begin MVP_v2 implementation.
