import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Calculator")
        self.setGeometry(100, 100, 300, 400)
        
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()

        self.result_display = QLineEdit()
        self.result_display.setReadOnly(True)
        self.layout.addWidget(self.result_display)

        button_grid = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"]
        ]

        for row in button_grid:
            h_layout = QHBoxLayout()
            for button_text in row:
                button = QPushButton(button_text)
                button.clicked.connect(self.handle_button_click)
                h_layout.addWidget(button)
            self.layout.addLayout(h_layout)

        self.setLayout(self.layout)

        self.current_input = ""

    def handle_button_click(self):
        button = self.sender()
        button_text = button.text()

        if button_text == "=":
            try:
                result = str(eval(self.current_input))
                self.result_display.setText(result)
            except Exception as e:
                self.result_display.setText("Error")
            self.current_input = ""
        else:
            self.current_input += button_text
            self.result_display.setText(self.current_input)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = CalculatorApp()
    calculator.show()
    sys.exit(app.exec_())




    