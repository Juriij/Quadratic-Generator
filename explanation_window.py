import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QScrollArea, QSpacerItem, QSizePolicy
from screeninfo import get_monitors
from maths import Equation
import matplotlib.pyplot as plt

class SecondWindow(QWidget):
    def __init__(self, width, height, problem, method):
        super().__init__()
        self.width = width
        self.height = height
        self.problem = problem
        self.method = method
        
        # Set up the main layout
        layout = QVBoxLayout(self)
        
        # Create a QScrollArea
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(False)
        
        # Create a widget that will be placed inside the scroll area
        container_widget = QWidget()
        container_layout = QVBoxLayout(container_widget)
        

        canvases = self.problem.Discriminant()   ############## To be changed

        for canvas in canvases:
            container_layout.addWidget(canvas)

            

        # Set the container widget as the widget for the scroll area
        scroll_area.setWidget(container_widget)
        
        # Add the scroll area to the main layout
        layout.addWidget(scroll_area)
        
        # Set the main layout to the window
        self.setLayout(layout)
        
        # Set window title and size
        self.setWindowTitle('Explanation')
        self.resize(self.width, self.height)


    def close_figs(self, method):      # AFTER REDOING THE OTHER METHODS AND CREATING NEW SUBPLOTS,                                         
        if method == "discriminant":   # DON'T FORGET TO CLOSE THEM ACCORDINGLY
            for i in range(1,4):
                plt.close(i)            #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                                        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                                        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                                        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    

    def closeEvent(self, event):       ####### Method is called when window is closed ##########
        print("Explanation Window closed!")
        self.close_figs(self.method)    
        self.close()                            
        self.deleteLater()         
        super().closeEvent(event)               


        


if __name__ == '__main__':


    for monitor in get_monitors():
        m = monitor

    problem = Equation("incomplete")
    problem.equation_genr(False)

    app = QApplication(sys.argv)

    # Example instantiation of SecondWindow
    window = SecondWindow(int(m.width*0.6),int(m.height*0.8), problem,"square")
    window.show()
    sys.exit(app.exec_())