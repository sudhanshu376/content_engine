from pathlib import Path
from datetime import datetime
import json


def create_run(topic=None):
    """
    Creates a new run directory structure and metadata.

    Returns:
        run_id (str)
        run_dir (Path)
    """

    run_id = datetime.now().strftime("%Y%m%d_%H%M%S")

    run_dir = Path("output") / "runs" / run_id

    # Create directories
    (run_dir / "audio").mkdir(parents=True, exist_ok=True)
    (run_dir / "video").mkdir(parents=True, exist_ok=True)
    (run_dir / "images").mkdir(parents=True, exist_ok=True)

    metadata = {
        "run_id": run_id,
        "topic": topic,
        "created_at": datetime.now().isoformat()
    }

    with open(run_dir / "run.json", "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

    return run_id, run_dir

def get_latest_run():
    runs_dir = Path("output") / "runs"

    if not runs_dir.exists():
        raise FileNotFoundError(
            "output/runs directory not found"
        )

    runs = [
        p for p in runs_dir.iterdir()
        if p.is_dir()
    ]

    if not runs:
        raise FileNotFoundError(
            "No runs found"
        )

    return sorted(runs)[-1]

''' 

from pathlib import Path
from datetime import datetime


def create_run():
    run_id = datetime.now().strftime("%Y%m%d_%H%M%S")

    run_dir = Path("output") / "runs" / run_id

    (run_dir / "audio").mkdir(parents=True, exist_ok=True)
    (run_dir / "video").mkdir(parents=True, exist_ok=True)
    (run_dir / "images").mkdir(parents=True, exist_ok=True)

    return run_id, run_dir

'''