import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("PyQt5 Input Example")
        
        # Set the central widget and the overall layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout(central_widget)
        
        # Create a QLineEdit widget
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Enter the number")
        
        # Create a QLabel to display the input
        self.label = QLabel("Your input will appear here")
        
        # Add widgets to the layout
        layout.addWidget(self.input_field)
        layout.addWidget(self.label)
        
        # Connect the textChanged signal to a slot method
        self.input_field.textChanged.connect(self.update_label)

    def update_label(self, text):
        self.label.setText(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())
