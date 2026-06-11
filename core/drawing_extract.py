import zipfile
from pathlib import Path
from core.app_config import OUTPUT_DIR


def extract_dwg(f2d_path, drawing_name):

    with zipfile.ZipFile(f2d_path, "r") as archive:

        dwg_files = [
            name
            for name in archive.namelist()
            if name.lower().endswith(".dwg")
        ]

        if not dwg_files:
            return None

        dwg_inside_zip = dwg_files[0]

        output_file = (
            OUTPUT_DIR
            / f"{drawing_name}.dwg"
        )

        with open(output_file, "wb") as f:

            f.write(
                archive.read(
                    dwg_inside_zip
                )
            )

        return str(output_file)