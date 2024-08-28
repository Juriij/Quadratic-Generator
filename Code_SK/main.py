import maths as math
import sys
from functools import partial
import sympy as sp
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QLabel, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from PyQt5.QtGui import QPixmap, QPainter
from screeninfo import get_monitors
from explanation_window import SecondWindow   
import matplotlib.pyplot as plt

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

        self.setWindowTitle("Menu")
        self.setFixedSize(QSize(self.Width, self.Height))

                # Title
        self.label = QLabel('Kvadratický Generátor', self)
        self.label.setFont(QFont("Arial", 40))
        self.label.adjustSize()
        self.label.move(self.Width // 2 - self.label.width() // 2, self.Height // 2 - self.label.height() // 2 - 250)
        self.label.show()



        self.eq_btn = QPushButton(self) #
        self.eq_btn.setText("Rovnica")
        self.eq_btn_size = (self.Width // 2 - self.eq_btn.width() - 140, self.Height // 2 -30, 180, 100)  #x ,y ,width, height
        self.eq_btn.move(self.eq_btn_size[0], self.eq_btn_size[1])
        self.eq_btn.setFixedSize(self.eq_btn_size[2], self.eq_btn_size[3])
        self.eq_btn.setFont(QFont("Arial", 16, QFont.Bold)) #
        self.eq_btn.adjustSize()  #
        self.eq_btn.clicked.connect(partial(self.expression_chosen, "Rovnica"))
        self.eq_btn.show()


        self.ineq_btn = QPushButton(self) #
        self.ineq_btn.setText("Nerovnica")
        self.ineq_btn_size = (self.Width // 2 +60, self.Height // 2 -30, 180, 100)
        self.ineq_btn.move(self.ineq_btn_size[0], self.ineq_btn_size[1])
        self.ineq_btn.setFixedSize(self.ineq_btn_size[2], self.ineq_btn_size[3])
        self.ineq_btn.setFont(QFont("Arial", 16, QFont.Bold))
        self.ineq_btn.adjustSize()
        self.ineq_btn.clicked.connect(partial(self.expression_chosen, "Nerovnica"))
        self.ineq_btn.show()

        self.gen_btn = QPushButton(self)
        self.gen_btn.setText("Generovať")
        self.gen_btn_size = (self.Width // 2 -80, self.Height // 2 +180, 160, 60)
        self.gen_btn.move(self.gen_btn_size[0], self.gen_btn_size[1])
        self.gen_btn.setFixedSize(self.gen_btn_size[2], self.gen_btn_size[3])
        self.gen_btn.setFont(QFont("Helvetica [Cronyx]", 14, QFont.Bold))
        self.gen_btn.clicked.connect(self.exprWindow)
        self.gen_btn.adjustSize()
        self.gen_btn.hide()   

        self.error3 = QLabel('Prosím, vyberte si typ rovnice', self)
        self.error3.setFont(QFont("Arial", 10))
        self.error3.adjustSize()
        self.error3.setStyleSheet("QLabel { color : red; }")
        self.error3.move(self.Width // 2 - self.eq_btn.width() - 85, self.Height // 2 -55)
        self.error3.hide() 

        self.error2 = QLabel('Prosím, zadajte číslo \n v rozmedzí od 1 do 10', self)
        self.error2.setFont(QFont("Arial", 9))
        self.error2.adjustSize()
        self.error2.setStyleSheet("QLabel { color : red; }")
        self.error2.hide()

        self.error1 = QLabel('Prosím zadajte požadovaný počet rovníc', self)
        self.error1.setFont(QFont("Arial", 9))
        self.error1.adjustSize()
        self.error1.setStyleSheet("QLabel { color : red; }")
        self.error1.hide() 

        #Dropdown
        self.comboBox = QComboBox(self)
        self.DDMplaceholder = "Typ rovnice..."
        self.MTHDplaceholder = "Metóda..."

        self.comboBox.hide()


        # Input field
        self.input_field = QLineEdit(self)
        self.input_field.setFixedSize(int(self.eq_btn_size[2]*0.6), int(self.eq_btn_size[3]*0.6))
        self.input_field.adjustSize()
        self.input_field.hide()
        
                

    def exprWindow(self):
        try:
            int(self.input_field.text())

            if int(self.input_field.text()) <= 10:
                if self.comboBox.currentText().lower() != "typ rovnice...":
                    expression = self.expression_type
                    amount = int(self.input_field.text())
                    type = self.comboBox.currentText().lower()


                    self.clearWindow()

                    self.exp_selected = False
                    self.select_error_colapse = False
                    self.once_select_error = True
                    
                    self.expressions, self.problems = math.genr_expression(expression, amount, type)    # latex expressions
                    self.setCentralWidget(self.expressions)

                    self.eq_dropdown = QComboBox(self)
                    self.eq_dropdown.addItem("Vyberte si rovnicu")
                    self.eq_dropdown.setCurrentIndex(0)
                    self.eq_dropdown.model().item(0).setEnabled(False)

                    
                    
                    ordinals = []
                    for i in range(amount):
                        ordinals.append(QLabel(f'{i+1}.', self))
                        self.eq_dropdown.addItem(f'Rovnica číslo .{i+1}')

                    self.eq_dropdown.addItem("Všetky")

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
                    self.solution_btn.setText("Ukáž výsledok")
                    self.solution_btn.setFixedSize(150,70)
                    self.solution_btn.move(int(self.Width*0.82), int(self.Height*0.11))
                    self.solution_btn.setFont(QFont("Arial", 10, QFont.Bold))
                    self.solution_btn.adjustSize() 
                    self.solution_btn.show()
                    self.solution_btn.clicked.connect(self.toggle_solution)

                        
                    if not self.hide_explanation:
                        self.explanation_btn = QPushButton(self) 
                        self.explanation_btn.setText("Výpočet")
                        self.explanation_btn.setFixedSize(150,70)
                        self.explanation_btn.move(int(self.Width*0.82), int(self.Height*0.18))
                        self.explanation_btn.setFont(QFont("Arial", 10, QFont.Bold))
                        self.explanation_btn.adjustSize() 
                        self.explanation_btn.clicked.connect(self.show_explanation)
                        self.explanation_btn.show()


                        self.mthd_dropdown = QComboBox(self)
                        self.mthd_dropdown.clear()
                        self.mthd_dropdown.addItem(self.MTHDplaceholder)
                        self.mthd_dropdown.setCurrentIndex(0)
                        self.mthd_dropdown.addItem("Diskriminant")
                        self.mthd_dropdown.addItem("Rozklad na korene")
                        self.mthd_dropdown.addItem("Štvorec")
                        self.mthd_dropdown.model().item(0).setEnabled(False)

                        button_position = self.explanation_btn.pos()
                        self.mthd_dropdown.setGeometry(button_position.x(), button_position.y() + self.explanation_btn.height(), self.explanation_btn.width(), self.mthd_dropdown.sizeHint().height())

                        self.mthd_dropdown.show()

                    self.home_btn = QPushButton(self) 
                    self.home_btn.setText("Menu")
                    self.home_btn_size = (self.Width // 2 +60, self.Height // 2 -30, 180, 100)
                    self.home_btn.move(30, 30)
                    self.home_btn.setFixedSize(self.ineq_btn_size[2], self.ineq_btn_size[3])
                    self.home_btn.setFont(QFont("Arial", 16, QFont.Bold))
                    self.home_btn.adjustSize()
                    self.home_btn.clicked.connect(self.return_menu)   
                    self.home_btn.show()

                    self.print_btn = QPushButton(self) 
                    self.print_btn.setText("vytlačiť!")
                    self.print_btn_size = (self.Width // 2 +60, self.Height // 2 -30, 180, 100)
                    self.print_btn.move(int(self.Width*0.27), int(self.Height*0.9))
                    self.print_btn.setFixedSize(self.ineq_btn_size[2], self.ineq_btn_size[3])
                    self.print_btn.setFont(QFont("Arial", 13, QFont.Bold))
                    self.print_btn.adjustSize()
                    self.print_btn.clicked.connect(self.showPrintDialog)   
                    self.print_btn.show()

                
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

    def close_fig(self):
        plt.close(100)
    

    def return_menu(self):
        if self.sol_shown:
            self.hide_solution()

        if self.is_win_open("Výpočet"):                                                                  
            self.close_win(self.scwindow)                  
        
         
        self.close_fig()
        self.setupWindow()

    
    def close_win(self, win):
        self.scwindow.close_figs()  
        win.close()                               
        win.deleteLater() 
        win = None


 


    def expression_chosen(self, type):   # reaction to clicking eq/ineq button
        global dropdown

        self.error3.hide()
        self.error2.hide()
        self.error1.hide()

        self.input_field.clear()
        self.input_field.setPlaceholderText("Počet")

        if type == "Rovnica":
            self.hide_explanation = False
            self.x_error2 = self.eq_btn_size[0]-155
            self.y_error2 = self.eq_btn_size[1]-20

            self.expression_type = "Rovnica"
            self.input_field.move(self.eq_btn_size[0]-150, self.eq_btn_size[1]+20)

            self.comboBox.clear()
            self.comboBox.addItem(self.DDMplaceholder)
            self.comboBox.setCurrentIndex(0)
            self.comboBox.addItem("Úplná")
            self.comboBox.addItem("Neúplná")
            self.comboBox.model().item(0).setEnabled(False)

            button_position = self.eq_btn.pos()
            self.comboBox.setGeometry(button_position.x(), button_position.y() + self.eq_btn.height(), self.eq_btn.width(), self.comboBox.sizeHint().height())

            self.comboBox.show()


        elif type=="Nerovnica":
            self.hide_explanation = True
            self.x_error2 = self.ineq_btn_size[0]+210
            self.y_error2 = self.ineq_btn_size[1]-20

            self.expression_type = "Nerovnica"
            self.input_field.move(self.ineq_btn_size[0]+220, self.ineq_btn_size[1]+20)

            self.comboBox.clear()
            self.comboBox.hide()

        self.input_field.show()
        self.gen_btn.show()



    def toggle_solution(self):
        if self.sol_shown:
            self.hide_solution()
        else:
            if self.exp_selected:
                self.show_solution()
            else:
                self.selection_error()


    def show_solution(self):
        self.solution_btn.setText("Skryť výsledky")
        self.sol_shown = True

        if self.eq_dropdown.currentText() == "Všetky":
            self.all_sol = []
            for problem in self.problems:
                self.all_sol.append(QLabel("výsledok", self))

            for i, sol in enumerate(self.all_sol):
                sol.setFont(QFont("Arial", 13))
                sol.setText(f'{sp.pretty(self.problems[i].solution)}')
                sol.adjustSize()
                sol.move(int(self.Width * 0.55), int(((self.Height) // 12) * (i+1)))
                sol.show()

      
        else:    
            self.solution_label = QLabel("výsledok", self)
            self.solution_label.setFont(QFont("Arial", 13))
            self.solution_label.setText(f'{sp.pretty(self.problems[self.eq_dropdown.currentIndex() - 1].solution)}')
            self.solution_label.adjustSize()
            self.solution_label.move(int(self.Width * 0.55), int(((self.Height) // 12) * (self.eq_dropdown.currentIndex())))
            self.solution_label.show()

            


    def hide_solution(self):
        self.sol_shown = False
        self.solution_btn.setText("Ukáž výsledky")
        if self.eq_dropdown.currentText() == "Všetky":
            for sol in self.all_sol:
                sol.deleteLater()

            self.all_sol = []
                

        else:
            self.solution_label.deleteLater()




    def hide_solution_dropdown(self):
        if self.is_win_open("Výpočet"):
            self.close_win(self.scwindow)

        self.exp_selected = True

        if self.select_error_colapse:
            self.select_error_colapse = False
            self.selection_error_resolved() 


        if self.sol_shown:
            if self.previous_text != "Všetky":        
                self.solution_label.deleteLater()

            elif self.previous_text == "Všetky":  
                for sol in self.all_sol:
                    sol.deleteLater()

                self.all_sol = []

            self.sol_shown = False
            self.solution_btn.setText("Ukáž výsledky")

        self.previous_text = self.eq_dropdown.currentText()    
 
    
    def selection_error(self):
        if self.once_select_error:
            self.once_select_error = False
            self.select_error_colapse = True
            self.error4 = QLabel('Prosím, vyberte si rovnicu', self)
            self.error4.setFont(QFont("Arial", 11))
            self.error4.adjustSize()
            self.error4.setStyleSheet("QLabel { color : red; }")
            self.error4.move(int(self.eq_dropdown.x()-self.Width//5.5), int(self.eq_dropdown.y()+self.Height//100))
            self.error4.show()

    def mthd_empty_error(self):
        self.error5 = QLabel('Prosím, vyberte si metódu výpočtu', self)
        self.error5.setFont(QFont("Arial", 11))
        self.error5.adjustSize()
        self.error5.setStyleSheet("QLabel { color : red; }")
        self.error5.move(int(self.mthd_dropdown.x()-self.Width//5.5+40), int(self.mthd_dropdown.y()+self.Height//100+25))
        self.error5.show()

    def mthd_empty_error_resolved(self):
        self.error5.deleteLater()


    def selection_error_resolved(self):
        self.error4.deleteLater()



    def show_explanation(self):
        if self.exp_selected:
            if not self.mthd_dropdown.currentText() == self.MTHDplaceholder:
                try:
                    self.mthd_empty_error_resolved()
                except:
                    pass

                if (not self.is_win_open("Výpočet")) and (not self.eq_dropdown.currentText() == "Všetky"):
                    index = self.eq_dropdown.currentIndex()-1
                    method = self.mthd_dropdown.currentText()
                    self.scwindow = SecondWindow(int(m.width*0.4),int(m.height*0.6), self.problems[index], method)
                    self.scwindow.show()

                else:
                    pass
            else:
                self.mthd_empty_error()
        else:
            self.selection_error()



    def is_win_open(self, window_title):
        app = QApplication.instance()
        if not app:
            return False
        
        for widget in app.topLevelWidgets():
            if widget.windowTitle() == window_title:
                return True
        
        return False



    def showPrintDialog(self):
        printer = QPrinter()
        dialog = QPrintDialog(printer, self)
        
        if dialog.exec_() == QPrintDialog.Accepted:
            self.print_plot(printer)


    def print_plot(self, printer):
        # Save the canvas to a temporary file
        self.expressions.print_figure('temp_plot.png', dpi=300)
        
        # Load the temporary file into a QPixmap
        pixmap = QPixmap('temp_plot.png')
        
        # Create a QPainter to draw the pixmap on the QPrinter
        painter = QPainter(printer)
        
        # Get the dimensions of the printable area
        pageRect = printer.pageRect()
        
        # Calculate the scale factor to make the image significantly larger
        scale_factor = min(pageRect.width() / pixmap.width(), pageRect.height() / pixmap.height()) * 1.75  # Increased scale factor

        # Scale the pixmap
        scaled_pixmap = pixmap.scaled(int(pixmap.width() * scale_factor), int(pixmap.height() * scale_factor))
        
        # Draw the scaled pixmap
        painter.drawPixmap(0, 0, scaled_pixmap)
        
        # End the painting
        painter.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    for monitor in get_monitors():
        m = monitor

    window = MainWindow(int(m.width*0.6),int(m.height*0.8))
    window.show()

    sys.exit(app.exec_())