import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from app.window import MainWindow


def main():
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
    )
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    # 아이콘 설정 (맥: .icns, 윈도우/리눅스: .ico)
    _base = Path(__file__).parent
    _ico = _base / ("0w0.icns" if sys.platform == "darwin" else "0w0.ico")
    if _ico.exists():
        app.setWindowIcon(QIcon(str(_ico)))

    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
