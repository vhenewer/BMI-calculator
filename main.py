import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic


class BMICalculator(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("mainwindow.ui", self)

        self.button_calculate.clicked.connect(self.calculate_bmi)

        self.setStyleSheet("""
                    QMainWindow {
                        background-color: #A9A9A9;
                    }
                    QPushButton:hover {
                        background-color: #45a049;
                    }
                    QLabel {
                    font-size: 18px;
                    font-weight: bold;
                    }
                    """)

    def calculate_bmi(self):
        try:
            weight_text = self.lineEdit_weight.text().strip()
            height_text = self.lineEdit_height.text().strip()

            if not weight_text or not height_text:
                self.label_result.setText("Error! Please fill in all fields.")
                return

            weight = float(weight_text)
            height = float(height_text) / 100

            if height <= 0 or weight <= 0:
                self.label_result.setText("Error! Values must be positive.")
                return

            bmi = weight / (height ** 2)

            self.label_result.setText(f" {bmi:.2f}")
        except ValueError:
            self.label_result.setText("Error! Please enter correct data.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BMICalculator()
    window.show()
    sys.exit(app.exec())
