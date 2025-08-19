import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QLineEdit, QFileDialog, QVBoxLayout, QMessageBox, QDesktopWidget
)
from app.generate import generate_qr
from app.scan import scan_qr

class QRToolGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qrtool")
        screen = QDesktopWidget().availableGeometry()
        width = int(screen.width() * 0.5)   
        height = int(screen.height() * 0.5) 
        self.setFixedSize(width, height)
        self.center_window()

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout()

        #Input for texte
        self.input_label = QLabel("Entrer votre texte")
        layout.addWidget(self.input_label)

        self.text_input = QLineEdit()
        layout.addWidget(self.text_input)
        
        #Button to generate QR
        self.generate_btn = QPushButton("Generate QR")
        self.generate_btn.clicked.connect(self.generate_qr_code)
        layout.addWidget(self.generate_btn)

        #Button to scan qr
        self.scan_btn = QPushButton("Scan QR")
        self.scan_btn.clicked.connect(self.scan_qr_code)
        layout.addWidget(self.scan_btn)

        self.setLayout(layout)


    def generate_qr_code(self):
        text = self.text_input.text().strip()

        if not text:
            QMessageBox.warning(self, "Warning", "Please enter text to generate QR code" )
            return 
        
        filename, _ = QFileDialog.getSaveFileName(self, "Save QR Code Image", "", "PNG Files (*.png);;All Files (*)")
        if filename:
            generate_qr(text, filename)
            QMessageBox.information(self, "Success", f"QR code saved as {filename}")

    def scan_qr_code(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open QR Code Image", "", "PNG Files (*.png);;All Files (*)")
        if filename:
            try:
                decoded_text = scan_qr(filename)
                QMessageBox.information(self, "QR Code Content", f"Decoded text: {decoded_text}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to scan QR code: {e}")

    def center_window(self):
        #Size of the window
        qr = self.frameGeometry()
        #Center of the screen
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

def run_app():
    app = QApplication(sys.argv)
    window = QRToolGUI()
    window.show()
    sys.exit(app.exec_())