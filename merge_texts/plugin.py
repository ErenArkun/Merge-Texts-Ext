from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog, QLineEdit
import os

class PluginWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Metin Birleştirici")

        self.input_folder = QLineEdit()
        self.output_file = QLineEdit()
        merge_button = QPushButton("Birleştir")

        browse_input = QPushButton("Klasör Seç")
        browse_output = QPushButton("Kaydetme Yolu Seç")

        browse_input.clicked.connect(self.select_input_folder)
        browse_output.clicked.connect(self.select_output_file)
        merge_button.clicked.connect(self.merge_files)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Metin Dosyası Klasörü"))
        layout.addWidget(self.input_folder)
        layout.addWidget(browse_input)
        layout.addWidget(QLabel("Birleştirilmiş Dosya"))
        layout.addWidget(self.output_file)
        layout.addWidget(browse_output)
        layout.addWidget(merge_button)

        self.setLayout(layout)

    def select_input_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Klasör Seç")
        if folder:
            self.input_folder.setText(folder)

    def select_output_file(self):
        file, _ = QFileDialog.getSaveFileName(self, "Kaydedilecek dosya", "", "Text Files (*.txt)")
        if file:
            self.output_file.setText(file)

    def merge_files(self):
        folder = self.input_folder.text()
        output = self.output_file.text()

        with open(output, "w", encoding="utf-8") as outfile:
            for filename in sorted(os.listdir(folder)):
                if filename.endswith(".txt"):
                    with open(os.path.join(folder, filename), "r", encoding="utf-8") as infile:
                        outfile.write(infile.read() + "\n")
        print("Dosyalar birleştirildi.")
