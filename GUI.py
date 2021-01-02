import sys
from PIL import Image
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QFileDialog


class App(QWidget):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)

        # Basic Settings
        self.setWindowTitle("Webp to JPG")
        self.setGeometry(800, 400, 350, 350)
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        self.image_path = None

        # Create Browse button
        self.btn_browse = QPushButton("Browse")
        self.btn_browse.clicked.connect(self.get_file)

        # Create convert button
        self.btn_convert = QPushButton("Convert")
        self.btn_convert.clicked.connect(self.convert_file)

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
        file_name = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Images (*.webp)")
        self.label_image.setPixmap(QPixmap(file_name[0]).scaled(400, 400))
        self.image_path = file_name[0]

    def convert_file(self):
        im = Image.open(self.image_path).convert("RGB")
        im.save(self.image_path.replace(".webp", ".jpg"), "jpeg")


def main():
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
