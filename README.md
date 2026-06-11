# Fusion Drawing Recovery

Recover original DWG drawings directly from Autodesk Fusion 360 `.f2d` files.

Browse local drawings, preview sheets, and extract DWG files without opening Fusion 360.

Fusion Drawing Recovery is a lightweight desktop utility that scans local Fusion 360 storage, displays drawing previews, and recovers the original DWG files embedded inside Fusion Drawing archives.

**No Fusion export workflow required.**

---

## Screenshot

![Fusion Drawing Recovery](assets/main.png)

---

## Features

- Automatically discover local Fusion Drawing files (`.f2d`)
- Preview drawing thumbnails without opening Fusion 360
- Recover original embedded DWG files
- Clean Autodesk GUID clutter from filenames
- Sort drawings by modification date
- Fast local workflow with no cloud dependency
- Read-only operation (does not modify Fusion files)

---

## Use Cases

- Recover DWG files when the original export was lost
- Access archived drawings without launching Fusion 360
- Browse large collections of local drawings quickly
- Recover drawings from Fusion cache backups
- Extract drawings from older projects
- Locate and organize technical drawings stored locally

---

## Why?

Autodesk Fusion 360 stores technical drawings locally as `.f2d` files.

These files already contain the information needed to preview drawings and recover the original DWG content. However, accessing those files directly is not part of the normal Fusion workflow.

Fusion Drawing Recovery provides a simple interface for browsing local drawing archives, previewing sheets, and extracting DWG files directly from Fusion's local storage.

This makes it useful for recovering lost exports, accessing archived projects, and working with drawings without opening Fusion 360.

---

## Quick Start

### Clone Repository

```bash
git clone https://github.com/Antslabeu/extract_fusion_dwg.git
cd extract_fusion_dwg
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Launch Application

```bash
python main.py
```

You can also run the project directly from VS Code using **F5**.

---

## Requirements

- Python 3.11+
- PySide6
- Pillow

---

## Supported Platforms

| Platform | Status |
|-----------|----------|
| macOS | ✅ Tested |
| Windows | ⚠️ Untested |
| Linux | ⚠️ Untested |

---

## Current Functionality

- Drawing discovery
- Thumbnail extraction
- Drawing preview
- DWG extraction
- Refresh workflow
- PySide6 desktop interface

---

## How It Works

1. Scan Fusion 360 local storage
2. Discover available `.f2d` drawing files
3. Extract and display drawing thumbnails
4. Preview drawings directly in the application
5. Recover embedded DWG files with a single click

---

## Roadmap

- Batch DWG export
- PDF extraction
- SVG export
- Search and filtering
- Drawing metadata viewer
- Multi-sheet preview support
- Improved CAD integration
- Standalone packaged releases

---

## Technical Notes

Fusion Drawing (`.f2d`) files are standard ZIP archives containing drawing-related assets and metadata.

Fusion Drawing Recovery operates entirely on files already stored locally on the user's machine and does not require cloud access.

---

## Disclaimer

This project is not affiliated with Autodesk.

Fusion Drawing Recovery does not modify Autodesk Fusion files.

It only reads data already stored locally on the user's machine and extracts assets already embedded inside Fusion Drawing archives.
