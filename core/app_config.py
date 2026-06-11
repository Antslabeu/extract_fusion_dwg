from pathlib import Path

FUSION_PATH = (
    Path.home()
    / "Library"
    / "Application Support"
    / "Autodesk"
    / "Autodesk Fusion 360"
)

OUTPUT_DIR = (
    Path(__file__).resolve().parent.parent
    / "output"
)

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)