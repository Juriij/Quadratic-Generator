import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QLabel

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt5 Dropdown Menu Example')
        self.setGeometry(100, 100, 300, 200)
        
        # Create a layout
        layout = QVBoxLayout()
        
        # Create a label
        self.label = QLabel("Select an option from the dropdown", self)
        layout.addWidget(self.label)
        
        # Create a dropdown menu (QComboBox)
        self.comboBox = QComboBox(self)
        self.comboBox.addItem("Option 1")
        self.comboBox.addItem("Option 2")
        self.comboBox.addItem("Option 3")
        layout.addWidget(self.comboBox)
        
        # Connect the dropdown menu to a method
        self.comboBox.currentIndexChanged.connect(self.update_label)
        
        # Set the layout to the main window
        self.setLayout(layout)
    
    def update_label(self):
        selected_text = self.comboBox.currentText()
        self.label.setText(f"You selected: {selected_text}")

# Main function to run the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = AppDemo()
    demo.show()
    sys.exit(app.exec_())