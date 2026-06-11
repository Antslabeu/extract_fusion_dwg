from pathlib import Path
from core.app_config import FUSION_PATH
from core.name_cleaner import clean_name


def find_drawings():

    results = []

    if not FUSION_PATH.exists():
        return results

    for file in FUSION_PATH.rglob("*.f2d"):

        results.append(
            {
                "name": clean_name(file.name),
                "path": str(file),
                "mtime": file.stat().st_mtime,
            }
        )

    results.sort(
        key=lambda x: x["mtime"],
        reverse=True
    )

    return results