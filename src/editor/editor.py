import sys
from screeninfo import get_monitors
import random
from PySide6 import QtCore, QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel(
            "Hello World", alignment=QtCore.Qt.AlignmentFlag.AlignCenter
        )

        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addWidget(self.text)
        self.main_layout.addWidget(self.button)
        self.setLayout(self.main_layout)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))


if __name__ == "__main__":
    height, width = 0, 0
    for monitor in get_monitors():
        if monitor.is_primary:
            height = monitor.height
            width = monitor.width

    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(width, height)
    widget.show()

    sys.exit(app.exec_())
