# https://nitratine.net/blog/post/how-to-import-a-pyqt5-ui-file-in-a-python-gui/
from PyQt5 import QtWidgets, uic
import sys
import os.path
from pdf_compressor import compress, get_file_size

from PyQt5.QtWidgets import QFileDialog

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

# determine if application is a script file or frozen exe
if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        try:
            uic.loadUi(os.path.join(PROJECT_PATH, 'data', 'untitled.ui'), self)
        except FileNotFoundError:
            # This loads when running
            uic.loadUi(os.path.join(PROJECT_PATH, 'untitled.ui'), self)
        self.selected_file = ""

        self.browse = self.findChild(QtWidgets.QPushButton, 'pushButton')  # Find the button
        self.browse.clicked.connect(self.select_file_button_pressed)
        self.compress = self.findChild(QtWidgets.QPushButton, 'pushButton_2')  # Find the button
        self.compress.clicked.connect(self.click_button_compress)

        self.spinbox_compress_level = self.findChild(QtWidgets.QSpinBox, 'spinBox')  # Find the button

        self.label_selected = self.findChild(QtWidgets.QLabel, 'label_selected_file')  # Find the button
        self.label_size = self.findChild(QtWidgets.QLabel, 'label_dydis')  # Find the button
        self.label_size_compressed = self.findChild(QtWidgets.QLabel, 'label_dydis_2')  # Find the button
        self.label_compressed_location = self.findChild(QtWidgets.QLabel, 'label_3')  # Find the button

        self.show()

    def browse_file(self):
        f_name = QFileDialog.getOpenFileName(self, "Open this bad boy", application_path)
        return f_name

    def select_file_button_pressed(self):
        # This is executed when the button is pressed
        self.label_size_compressed.setText("")
        selected_file = self.browse_file()[0]
        print(selected_file)
        if selected_file:
            self.label_selected.setText(selected_file)
        else:
            return
        self.selected_file = selected_file
        # print(f'Spinbox value: {self.spinbox_compress_level.value()}')
        size = get_file_size(selected_file)
        print(size)
        self.label_size.setText("{0:.2f}MB".format(size))

    def click_button_compress(self):
        # This is executed when the button is pressed
        print('compress pressed')
        input_file = self.selected_file
        output_file = os.path.join(application_path, "suspaustas.pdf")
        compress(input_file, output_file, self.spinbox_compress_level.value())
        self.label_size_compressed.setText("{0:.2f}MB".format(get_file_size(output_file)))
        self.label_compressed_location.setText(output_file)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
