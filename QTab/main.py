from PySide6.QtWidgets import QApplication
import sys
from widget import Widget

app = QApplication(sys.argv)

widget = Widget()
widget.show()

if __name__ == '__main__':
    app.exec()