from pathlib import Path
import tempfile
import zipfile
import hashlib


THUMBNAIL_PATH = (
    "Documentation[Active]/"
    "SheetThumbnails/"
    "D3_large.png"
)


def extract_thumbnail(f2d_path):

    try:
        with zipfile.ZipFile(f2d_path, "r") as archive:
            if THUMBNAIL_PATH not in archive.namelist():
                return None

            hash_name = hashlib.md5(
                f2d_path.encode()
            ).hexdigest()

            output_file = (
                Path(tempfile.gettempdir())
                / f"{hash_name}.png"
            )
            with open(output_file, "wb") as f:
                f.write(
                    archive.read(
                        THUMBNAIL_PATH
                    )
                )
            return str(output_file)
    except Exception as e:
        print(e)
        return None