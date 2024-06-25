import maths as math
import sys
from functools import partial
import sympy as sp


from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QLabel, QPushButton
from PyQt5.QtGui import QFont

from screeninfo import get_monitors



dropdown = False

class MainWindow(QMainWindow):
    def __init__(self, width, height):
        self.Width = width
        self.Height = height
        self.sol_shown = False
        self.all_sol = []

        super().__init__()

        self.setupWindow()




    def setupWindow(self):
        self.clearWindow()

        self.setWindowTitle("Main")
        self.setFixedSize(QSize(self.Width, self.Height))

                # Title
        self.label = QLabel('Quadratic Generator', self)
        self.label.setFont(QFont("Arial", 40))
        self.label.adjustSize()
        self.label.move(self.Width // 2 - self.label.width() // 2, self.Height // 2 - self.label.height() // 2 - 250)
        self.label.show()


        # Buttons                        <---------- perhaps, later can be automated
        self.eq_btn = QPushButton(self) #
        self.eq_btn.setText("Equation")
        self.eq_btn_size = (self.Width // 2 - self.eq_btn.width() - 140, self.Height // 2 -30, 180, 100)  #x ,y ,width, height
        self.eq_btn.move(self.eq_btn_size[0], self.eq_btn_size[1])
        self.eq_btn.setFixedSize(self.eq_btn_size[2], self.eq_btn_size[3])
        self.eq_btn.setFont(QFont("Arial", 16, QFont.Bold)) #
        self.eq_btn.adjustSize()  #
        self.eq_btn.clicked.connect(partial(self.expression_chosen, "Equation"))
        self.eq_btn.show()


        self.ineq_btn = QPushButton(self) #
        self.ineq_btn.setText("Inequality")
        self.ineq_btn_size = (self.Width // 2 +60, self.Height // 2 -30, 180, 100)
        self.ineq_btn.move(self.ineq_btn_size[0], self.ineq_btn_size[1])
        self.ineq_btn.setFixedSize(self.ineq_btn_size[2], self.ineq_btn_size[3])
        self.ineq_btn.setFont(QFont("Arial", 16, QFont.Bold))
        self.ineq_btn.adjustSize()
        self.ineq_btn.clicked.connect(partial(self.expression_chosen, "Inequality"))
        self.ineq_btn.show()

        self.gen_btn = QPushButton(self)
        self.gen_btn.setText("Generate")
        self.gen_btn_size = (self.Width // 2 -80, self.Height // 2 +180, 160, 60)
        self.gen_btn.move(self.gen_btn_size[0], self.gen_btn_size[1])
        self.gen_btn.setFixedSize(self.gen_btn_size[2], self.gen_btn_size[3])
        self.gen_btn.setFont(QFont("Helvetica [Cronyx]", 14, QFont.Bold))
        self.gen_btn.clicked.connect(self.expWindow)
        self.gen_btn.adjustSize()
        self.gen_btn.hide()   

        self.error3 = QLabel('Please select type of equation', self)
        self.error3.setFont(QFont("Arial", 10))
        self.error3.adjustSize()
        self.error3.setStyleSheet("QLabel { color : red; }")
        self.error3.move(self.Width // 2 - self.eq_btn.width() - 85, self.Height // 2 -55)
        self.error3.hide() 

        self.error2 = QLabel('Please enter number \n in range from 1 to 10', self)
        self.error2.setFont(QFont("Arial", 9))
        self.error2.adjustSize()
        self.error2.setStyleSheet("QLabel { color : red; }")
        self.error2.hide()

        self.error1 = QLabel('Please enter number', self)
        self.error1.setFont(QFont("Arial", 9))
        self.error1.adjustSize()
        self.error1.setStyleSheet("QLabel { color : red; }")
        self.error1.hide() 

        #Dropdown
        self.comboBox = QComboBox(self)
        self.DDMplaceholder = "Type of equation..."

        self.comboBox.hide()


        # Input field
        self.input_field = QLineEdit(self)
        self.input_field.setFixedSize(int(self.eq_btn_size[2]*0.6), int(self.eq_btn_size[3]*0.6))
        self.input_field.adjustSize()
        self.input_field.hide()
        
                


    def expWindow(self):
        try:
            int(self.input_field.text())

            if int(self.input_field.text()) <= 10:
                if self.comboBox.currentText().lower() != "type of equation...":
                    expression = self.expression_type
                    amount = int(self.input_field.text())
                    type = self.comboBox.currentText().lower()


                    self.clearWindow()
                    
                    self.expressions, self.problems = math.genr_expression(expression, amount, type)    # latex expressions
                    self.setCentralWidget(self.expressions)

                    self.eq_dropdown = QComboBox(self)
                    self.eq_dropdown.addItem("Select expression")
                    self.eq_dropdown.setCurrentIndex(0)
                    self.eq_dropdown.model().item(0).setEnabled(False)
                    
                    ordinals = []
                    for i in range(amount):
                        ordinals.append(QLabel(f'{i+1}.', self))
                        self.eq_dropdown.addItem(f'Expression .{i+1}')

                    self.eq_dropdown.addItem("All")

                    for i, ordinal in enumerate(ordinals):
                        ordinal.setFont(QFont("Arial", 20))
                        ordinal.adjustSize()
                        ordinal.move(int(self.Width*0.2), int(((self.Height)//12)*(i+1)))
                        ordinal.show()

                    self.eq_dropdown.setFont(QFont("Arial", 13))
                    self.eq_dropdown.adjustSize()
                    self.eq_dropdown.move(int(self.Width*0.8), int(self.Height*0.05))
                    self.previous_text = self.eq_dropdown.currentText()
                    self.eq_dropdown.currentIndexChanged.connect(self.hide_solution_dropdown)
                    self.eq_dropdown.show()

                    
                    self.solution_btn = QPushButton(self) 
                    self.solution_btn.setText("Show Solution")
                    self.solution_btn.setFixedSize(150,70)
                    self.solution_btn.move(int(self.Width*0.82), int(self.Height*0.11))
                    self.solution_btn.setFont(QFont("Arial", 10, QFont.Bold))
                    self.solution_btn.adjustSize() 
                    self.solution_btn.show()
                    self.solution_btn.clicked.connect(self.toggle_solution)

                        

                    self.explanation_btn = QPushButton(self) 
                    self.explanation_btn.setText("Explanation")
                    self.explanation_btn.setFixedSize(150,70)
                    self.explanation_btn.move(int(self.Width*0.82), int(self.Height*0.18))
                    self.explanation_btn.setFont(QFont("Arial", 10, QFont.Bold))
                    self.explanation_btn.adjustSize() 
                    self.explanation_btn.clicked.connect(self.show_explanation)
                    self.explanation_btn.show()


                    self.home_btn = QPushButton(self) 
                    self.home_btn.setText("Home")
                    self.home_btn_size = (self.Width // 2 +60, self.Height // 2 -30, 180, 100)
                    self.home_btn.move(30, 30)
                    self.home_btn.setFixedSize(self.ineq_btn_size[2], self.ineq_btn_size[3])
                    self.home_btn.setFont(QFont("Arial", 16, QFont.Bold))
                    self.home_btn.adjustSize()
                    self.home_btn.clicked.connect(self.return_menu)   
                    self.home_btn.show()



                
                else:
                    self.error3.show()

                    self.error2.hide()
                    self.error1.hide()
            else:
                self.error2.move(self.x_error2, self.y_error2)
                self.error2.show()

                self.error3.hide()
                self.error1.hide()

        except: 
            self.error1.move(self.x_error2, self.y_error2)
            self.error1.show()

            self.error3.hide()
            self.error2.hide()







    def clearWindow(self):
        for widget in self.findChildren(QWidget):
            if widget is not self:  # Don't delete the main window
                widget.deleteLater()

    def return_menu(self):
        if self.sol_shown:
            self.hide_solution()
        self.setupWindow()


    def expression_chosen(self, type):   # reaction to clicking eq/ineq button
        global dropdown

        self.error3.hide()
        self.error2.hide()
        self.error1.hide()

        self.input_field.clear()
        self.input_field.setPlaceholderText("Amount")

        if type == "Equation":
            self.x_error2 = self.eq_btn_size[0]-155
            self.y_error2 = self.eq_btn_size[1]-20

            self.expression_type = "Equation"
            self.input_field.move(self.eq_btn_size[0]-150, self.eq_btn_size[1]+20)

            self.comboBox.clear()
            self.comboBox.addItem(self.DDMplaceholder)
            self.comboBox.setCurrentIndex(0)
            self.comboBox.addItem("Complete")
            self.comboBox.addItem("Incomplete")
            self.comboBox.model().item(0).setEnabled(False)

            button_position = self.eq_btn.pos()
            self.comboBox.setGeometry(button_position.x(), button_position.y() + self.eq_btn.height(), self.eq_btn.width(), self.comboBox.sizeHint().height())

            self.comboBox.show()


        elif type=="Inequality":
            self.x_error2 = self.ineq_btn_size[0]+210
            self.y_error2 = self.ineq_btn_size[1]-20

            self.expression_type = "Inequality"
            self.input_field.move(self.ineq_btn_size[0]+220, self.ineq_btn_size[1]+20)

            self.comboBox.clear()
            self.comboBox.hide()

        self.input_field.show()
        self.gen_btn.show()


    def toggle_solution(self):
        if self.sol_shown:
            self.hide_solution()
        else:
            self.show_solution()


    def show_solution(self):
        self.solution_btn.setText("Hide Solution")
        self.sol_shown = True

        if self.eq_dropdown.currentText() == "All":
            self.all_sol = []
            for problem in self.problems:
                self.all_sol.append(QLabel("solution", self))

            for i, sol in enumerate(self.all_sol):
                sol.setFont(QFont("Arial", 13))
                sol.setText(f'{sp.pretty(self.problems[i].solution)}')
                sol.adjustSize()
                sol.move(int(self.Width * 0.47), int(((self.Height) // 12) * (i+1)))
                sol.show()

      
        else:    
            self.solution_label = QLabel("solution", self)
            self.solution_label.setFont(QFont("Arial", 13))
            self.solution_label.setText(f'{sp.pretty(self.problems[self.eq_dropdown.currentIndex() - 1].solution)}')
            self.solution_label.adjustSize()
            self.solution_label.move(int(self.Width * 0.47), int(((self.Height) // 12) * (self.eq_dropdown.currentIndex())))
            self.solution_label.show()

            


    def hide_solution(self):
        self.sol_shown = False
        self.solution_btn.setText("Show Solution")
        if self.eq_dropdown.currentText() == "All":
            for sol in self.all_sol:
                sol.deleteLater()

            self.all_sol = []
                

        else:
            self.solution_label.deleteLater()




    def hide_solution_dropdown(self):
        if self.sol_shown:
            if self.previous_text != "All":        
                self.solution_label.deleteLater()

            elif self.previous_text == "All":  
                for sol in self.all_sol:
                    sol.deleteLater()

                self.all_sol = []

            self.sol_shown = False
            self.solution_btn.setText("Show Solution")

        self.previous_text = self.eq_dropdown.currentText()    
 



    def show_explanation(self):
        pass



app = QApplication(sys.argv)

for monitor in get_monitors():
    m = monitor

window = MainWindow(int(m.width*0.6),int(m.height*0.8))
window.show()

app.exec()