from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QListWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QFormLayout,
)
from core.fusion_scan import find_drawings
from PySide6.QtGui import QPixmap
from core.thumbnail_extract import (
    extract_thumbnail
)
from datetime import datetime
from pathlib import Path
from core.drawing_extract import extract_dwg
import subprocess


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fusion Drawing Recovery")
        self.resize(1400, 900)

        self.build_ui()

        self.drawings = []

        self.refresh_btn.clicked.connect(self.refresh_drawings)
        self.open_btn.clicked.connect(self.open_current_dwg)

        self.drawing_list.currentRowChanged.connect(self.on_selection_changed)
        self.current_pixmap = None
        self.refresh_drawings()


    def open_current_dwg(self):
        row = self.drawing_list.currentRow()

        if row < 0:
            return

        drawing = self.drawings[row]
        dwg_file = extract_dwg(
            drawing["path"],
            drawing["name"]
        )
        if not dwg_file:
            print("No DWG found")
            return
        librecad = Path("/Applications/LibreCAD.app")
        if librecad.exists():
            subprocess.Popen([
                "open",
                "-a",
                "LibreCAD",
                dwg_file
            ])
            return
        print("No CAD application found")

    def build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)

        root = QVBoxLayout()
        root.setContentsMargins(12, 12, 12, 12)
        root.setSpacing(10)

        central.setLayout(root)

        # main content
        content = QHBoxLayout()
        content.setSpacing(10)
        root.addLayout(content)

        # left
        self.drawing_list = QListWidget()
        self.drawing_list.setMinimumWidth(350)
        content.addWidget(self.drawing_list, 1)

        # right
        right_widget = QWidget()
        right_layout = QVBoxLayout()
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_widget.setLayout(right_layout)
        self.thumbnail_label = QLabel("No Drawing Selected")

        self.thumbnail_label.setAlignment(Qt.AlignCenter)
        self.thumbnail_label.setMinimumSize(400, 300)
        self.thumbnail_label.setStyleSheet("""
            QLabel {
                border: 1px solid #444;
                border-radius: 8px;
            }
        """)

        right_layout.addWidget(self.thumbnail_label, 100)
   
        content.addWidget(
            right_widget,
            2
        )

        # buttons
        buttons = QHBoxLayout()
        buttons.setSpacing(8)

        root.addLayout(buttons)

        self.open_btn = QPushButton("Open DWG")
        self.refresh_btn = QPushButton("Refresh list")

        buttons.addWidget(self.open_btn)
        buttons.addStretch()
        buttons.addWidget(self.refresh_btn)

    def on_selection_changed(self, row):
        if row < 0:
            return
        drawing = self.drawings[row]
        
        thumbnail = extract_thumbnail(drawing["path"])

        if thumbnail:
            self.current_pixmap = QPixmap(thumbnail)
            self.update_thumbnail_display()
        else:
            self.thumbnail_label.setText(
                "No Thumbnail"
            )

    def update_thumbnail_display(self):
        if not self.current_pixmap:
            return
        self.thumbnail_label.setPixmap(
            self.current_pixmap.scaled(
                self.thumbnail_label.contentsRect().size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation,
            )
        )

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.update_thumbnail_display()

    def refresh_drawings(self):
        self.drawings = find_drawings()
        self.drawing_list.clear()

        for drawing in self.drawings:
            self.drawing_list.addItem(
            drawing["name"]
        )
        if self.drawing_list.count() > 0:
            self.drawing_list.setCurrentRow(0)
            # self.on_selection_changed(self, 0)