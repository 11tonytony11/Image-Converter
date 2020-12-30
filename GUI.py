import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QGridLayout, QPushButton, \
    QLabel, QTextEdit, QHBoxLayout, QVBoxLayout, QSizePolicy
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon, QPixmap


class App(QWidget):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)

        # Basic Settings
        self.setWindowTitle("Webp to JPG")
        self.setGeometry(800, 400, 350, 350)
        self.setWindowIcon(QtGui.QIcon('icon.png'))

        # Create Browse button
        self.btn_browse = QPushButton("Browse")
        self.btn_browse.clicked.connect(self.get_file)

        # Create convert button
        self.btn_convert = QPushButton("Convert")
        self.btn_convert.clicked.connect(self.get_file)

        # Create image window
        self.label_image = QLabel("")

        # Buttons layout
        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.btn_browse)
        btn_layout.addWidget(self.btn_convert)

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.addStretch(1)

        # Bind layouts
        main_layout.addWidget(self.label_image)
        main_layout.addLayout(btn_layout)
        self.setLayout(main_layout)

    def get_file(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Image files (*.jpg *.gif)")
        self.label_image.setPixmap(QPixmap(fname[0]).scaled(400, 400))


def main():
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

