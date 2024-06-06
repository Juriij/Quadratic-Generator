import maths as math
import sys
from functools import partial

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 



class MainWindow(QMainWindow):
    def __init__(self, width, height):
        self.Width = width
        self.Height = height
        super().__init__()

        self.setWindowTitle("Main")
        self.setFixedSize(QSize(self.Width, self.Height))


        # Title 
        self.label = QLabel('Quadratic Generator', self) 
        self.label.setFont(QFont("Arial", 40))
        self.label.adjustSize() 
        self.label.move(self.Width // 2 - self.label.width() // 2, self.Height // 2 - self.label.height() // 2 - 250)


        # Buttons                        <---------- perhaps, later can be automated  
        self.eq_btn = QPushButton(self)
        self.eq_btn.setText("Equation")
        self.eq_btn_size = (self.Width // 2 - self.eq_btn.width() - 140, self.Height // 2 -30, 180, 100)
        self.eq_btn.move(self.eq_btn_size[0], self.eq_btn_size[1])
        self.eq_btn.setFixedSize(self.eq_btn_size[2], self.eq_btn_size[3])
        self.eq_btn.setFont(QFont("Arial", 16, QFont.Bold))
        self.eq_btn.adjustSize() 
        self.eq_btn.clicked.connect(partial(self.expression_chosen, "Equation"))

        self.ineq_btn = QPushButton(self)
        self.ineq_btn.setText("Inequality")
        self.ineq_btn_size = (self.Width // 2 +60, self.Height // 2 -30, 180, 100)
        self.ineq_btn.move(self.ineq_btn_size[0], self.ineq_btn_size[1])
        self.ineq_btn.setFixedSize(self.ineq_btn_size[2], self.ineq_btn_size[3])
        self.ineq_btn.setFont(QFont("Arial", 16, QFont.Bold))
        self.ineq_btn.adjustSize() 
        self.ineq_btn.clicked.connect(partial(self.expression_chosen, "Inequality"))


  
        # show all the widgets 
        self.show() 

    
    def expression_chosen(self, arg1):
        print(arg1)
        #juro 



app = QApplication(sys.argv)

window = MainWindow(1400,1300)
window.show()

app.exec()