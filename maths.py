import sympy as sp
import random
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas



class Expression:

    def Discriminant(self):
        fig0, ax0 = plt.subplots()
        y = 0.9

        canvas_list = []

        ax0.text(0.4, y, f'Equation: ', ha="center", va="center", fontsize=20, color="black")
        y = y - 0.20

        x = sp.symbols("x")
        self.equation = sp.Eq(self.a*x**2 + self.b*x + self.c, 0)
        latex_equation = sp.latex(self.equation)

        ax0.text(0.4, y, f'${latex_equation}$', ha="center", va="center", fontsize=20, color="black")
        y = y - 0.20

        ax0.text(0.4, y, f'${'a = '+ str(self.a)}$', ha="center", va="center", fontsize=20, color="black")
        y = y - 0.15

        ax0.text(0.4, y, f'${'b = '+ str(self.b)}$', ha="center", va="center", fontsize=20, color="black")
        y = y - 0.15

        ax0.text(0.4, y, f'${'c = '+ str(self.c)}$', ha="center", va="center", fontsize=20, color="black")
        y = y - 0.15

        ax0.set_xlim(0, 1)
        ax0.set_ylim(0, 1)

        # Remove axes
        ax0.axis('off')
        canvas0 = FigureCanvas(fig0)
        canvas_list.append(canvas0)
        


        fig1, ax1 = plt.subplots()
        y = 0.9



        ax1.text(0.4, y, 'Calculation of discriminant:', ha="center", va="center", fontsize=20, color="black")
        y = y - 0.15

        D = sp.symbols ("D")

        a = sp.symbols ("a")
        b = sp.symbols ("b")
        c = sp.symbols ("c")

        show_discriminant = sp.Eq(D, b**2 - 4*a*c)

        latex_form = sp.latex(show_discriminant)
        ax1.text(0.4, y, f'${latex_form}$', ha="center", va="center", fontsize=20, color="black")
        y = y - 0.15

        discriminant = sp.Eq(D, self.b**2 - 4*self.a*self.c)
        ax1.text(0.4, y, f'${'D = - 4*' + str(self.a)+"*"+str(self.c)+'+'+str(self.b**2)}$', ha="center", va="center", fontsize=20, color="black")
        y = y - 0.15


        if (4*self.a*self.c)<0:
            ax1.text(0.4, y, f'${"D =" + str(-4*self.a*self.c) + "+" + str(self.b**2)}$', ha="center", va="center", fontsize=20, color="black")
            y = y - 0.3
        else:
            ax1.text(0.4, y, f'${"D =" + str(-4*self.a*self.c) + "+" + str(self.b**2)}$', ha="center", va="center", fontsize=20, color="black")
            y = y - 0.3

        D_list = sp.solve(discriminant)
        latex_form = sp.latex(discriminant)
        ax1.text(0.4, y, f'${latex_form}$', ha="center", va="center", fontsize=20, color="black")
        y = y - 0.15



        if D_list[0] >=0:

            ax1.set_xlim(0, 1)
            ax1.set_ylim(0, 1)

        # Remove axes
            ax1.axis('off')

            canvas1 = FigureCanvas(fig1)

            canvas_list.append(canvas1)

            fig2, ax2 = plt.subplots(num=2)
            y = 0.9

            ax2.text(0.4, y, 'Calculation of x1: ', ha="center", va="center", fontsize=20, color="black")
            y = y - 0.15

            x1 = sp.symbols("x1")

            show_solution1 = sp.Eq(x1, (-b -(sp.sqrt(D)))/(2*a))
            show_solution1 = sp.latex(show_solution1)
            ax2.text(0.4, y, f'${show_solution1}$', ha="center", va="center", fontsize=20, color="black")
            y = y - 0.15


            _b = sp.symbols(f'{-self.b}')
            rootD = sp.symbols(f'{sp.sqrt(D_list[0])}')
            denominator = sp.symbols(f'{2*self.a}')   

            solution1 = sp.Eq(x1, (_b - rootD)/(denominator))
            solution1 = sp.latex(solution1)
            ax2.text(0.4, y, f'${solution1}$', ha="center", va="center", fontsize=20, color="black")
            y = y - 0.15

            numerator = sp.symbols(f'{-self.b -(sp.sqrt(D_list[0]))}') 
            denominator = sp.symbols(f'{2*self.a}')

            show_solution1 = sp.Eq(x1, numerator/denominator)
            show_solution1 = sp.latex(show_solution1)

            ax2.text(0.4, y, f'${str(show_solution1)}$', ha="center", va="center", fontsize=20, color="black")
            y = y - 0.3

            solution1 = sp.Eq(x1, (-self.b -(sp.sqrt(D_list[0])))/(2*self.a))
            x1_list = sp.solve(solution1)
            solution1 = sp.latex(solution1)
            ax2.text(0.4, y, f'${str(solution1)}$', ha="center", va="center", fontsize=20, color="black")


            ax2.set_xlim(0, 1)
            ax2.set_ylim(0, 1)

        # Remove axes
            ax2.axis('off')
            canvas2 = FigureCanvas(fig2)
            canvas_list.append(canvas2)

            fig3, ax3 = plt.subplots(num=3)
            y = 0.9

            ax3.text(0.4, y, 'Calculation of x2: ', ha="center", va="center", fontsize=20, color="black")
            y = y - 0.15

            x2 = sp.symbols("x2")

            show_solution2 = sp.Eq(x2, (-b +(sp.sqrt(D)))/(2*a))
            show_solution2 = sp.latex(show_solution2)
            ax3.text(0.4, y, f'${str(show_solution2)}$', ha="center", va="center", fontsize=20, color="black")
            y = y - 0.15

            solution2 = sp.Eq(x2, (-self.b +(sp.sqrt(D_list[0])))/(2*self.a))

            _b = sp.symbols(f'{-self.b}')
            rootD = sp.symbols(f'{sp.sqrt(D_list[0])}')
            denominator = sp.symbols(f'{2*self.a}')   

            solution2 = sp.Eq(x2, (_b + rootD)/(denominator))
            solution2 = sp.latex(solution2)
            ax3.text(0.4, y, f'${solution2}$', ha="center", va="center", fontsize=20, color="black")
            y = y - 0.15

            numerator = sp.symbols(f'{-self.b +(sp.sqrt(D_list[0]))}') 
            denominator = sp.symbols(f'{2*self.a}')

            show_solution2 = sp.Eq(x2, numerator/denominator)
            show_solution2 = sp.latex(show_solution2)
            ax3.text(0.4, y, f'${show_solution2}$', ha="center", va="center", fontsize=20, color="black")
            y = y - 0.3

            solution2 = sp.Eq(x2, (-self.b +(sp.sqrt(D_list[0])))/(2*self.a))
            x2_list = sp.solve(solution2)
            solution2 = sp.latex(solution2)
            ax3.text(0.4, y, f'${solution2}$', ha="center", va="center", fontsize=20, color="black")

            ax3.set_xlim(0, 1)
            ax3.set_ylim(0, 1)

        # Remove axes
            ax3.axis('off')


            canvas3 = FigureCanvas(fig3)
            canvas_list.append(canvas3)
            return canvas_list
        
        else:
            ax1.text(0.4, y, 'This equation has no solution', ha="center", va="center", fontsize=20, color="black")

            
            ax1.set_xlim(0, 1)
            ax1.set_ylim(0, 1)

        # Remove axes
            ax1.axis('off')

            canvas1 = FigureCanvas(fig1)

            canvas_list.append(canvas1)
            return canvas_list
        


    def Factoring(self):
        SOLUTION = []
        SOLUTION = self.solution
        if len(SOLUTION)>1:
            self.x1, self.x2 = SOLUTION
            self.p = -(self.x1)
            self.q = -(self.x2)

            b = sp.symbols("b")
            c = sp.symbols("c")
            p = sp.symbols("p")
            q = sp.symbols("q")
            x1 = sp.symbols("x1")
            x2 = sp.symbols("x2")

            fig0, ax0 = plt.subplots()
            y = 0.9

            canvas_list = []

            ax0.text(0.4, y, f'Equation: ', ha="center", va="center", fontsize=20, color="black")
            y = y - 0.20

            x = sp.symbols("x")
            self.equation = sp.Eq(self.a*x**2 + self.b*x + self.c, 0)
            latex_equation = sp.latex(self.equation)

            ax0.text(0.4, y, f'${latex_equation}$', ha="center", va="center", fontsize=20, color="black")
            y = y - 0.20

            ax0.text(0.4, y, f'${'a = '+ str(self.a)}$', ha="center", va="center", fontsize=20, color="black")
            y = y - 0.15

            ax0.text(0.4, y, f'${'b = '+ str(self.b)}$', ha="center", va="center", fontsize=20, color="black")
            y = y - 0.15

            ax0.text(0.4, y, f'${'c = '+ str(self.c)}$', ha="center", va="center", fontsize=20, color="black")
            y = y - 0.15

            ax0.set_xlim(0, 1)
            ax0.set_ylim(0, 1)

            # Remove axes
            ax0.axis('off')
            canvas0 = FigureCanvas(fig0)
            canvas_list.append(canvas0)
            

            fig1, ax1 = plt.subplots()
            y = 0.7

            ax1.text(0.4, y, f'Factoring formulas: ', ha="center", va="center", fontsize=20, color="black")
            y = y - 0.20

            show_rootage = sp.Eq((x1+p)*(x2+q), 0)
            show_rootage = sp.latex(show_rootage)
            ax1.text(0.4, y, f'${str(show_rootage)}$', ha="center", va="center", fontsize=20, color="black")
            y -= 0.2

            show_b = sp.Eq(b, p+q)
            show_b = sp.latex(show_b)
            ax1.text(0.4, y, f'${str(show_b)}$', ha="center", va="center", fontsize=20, color="black")
            y -= 0.15

            show_c = sp.Eq(c, p*q)
            show_c = sp.latex(show_c)
            ax1.text(0.4, y, f'${str(show_c)}$', ha="center", va="center", fontsize=20, color="black")
            y -= 0.15


            ax1.set_xlim(0, 1)
            ax1.set_ylim(0, 1)

            # Remove axes
            ax1.axis('off')
            canvas1 = FigureCanvas(fig1)
            canvas_list.append(canvas1)

            fig2, ax2 = plt.subplots()
            y = 0.9

            ax2.text(0.4, y, f'Solutions: ', ha="center", va="center", fontsize=20, color="black")
            y = y - 0.17

            rootage = sp.Eq((x1+self.p)*(x2+self.q), 0)
            rootage = sp.latex(rootage)
            ax2.text(0.4, y, f'${str(rootage)}$', ha="center", va="center", fontsize=20, color="black")
            y -= 0.2

            show_x1 = sp.Eq(x1+self.p,0)
            show_x1 = sp.latex(show_x1)
            ax2.text(0.4, y, f'${str(show_x1)}$', ha="center", va="center", fontsize=20, color="black")
            y -= 0.15

            sol_x1 = sp.Eq(x1,self.x1)
            sol_x1 = sp.latex(sol_x1)
            ax2.text(0.4, y, f'${str(sol_x1)}$', ha="center", va="center", fontsize=20, color="black")
            y -= 0.3

            show_x2 = sp.Eq(x2+self.q,0)
            show_x2 = sp.latex(show_x2)
            ax2.text(0.4, y, f'${str(show_x2)}$', ha="center", va="center", fontsize=20, color="black")
            y -= 0.15

            sol_x2 = sp.Eq(x2,self.x2)
            sol_x2 = sp.latex(sol_x2)
            ax2.text(0.4, y, f'${str(sol_x2)}$', ha="center", va="center", fontsize=20, color="black")

            ax2.set_xlim(0, 1)
            ax2.set_ylim(0, 1)

            # Remove axes
            ax2.axis('off')
            canvas2 = FigureCanvas(fig2)
            canvas_list.append(canvas2)


        else:
            SOLUTION = []
            SOLUTION.append(0)
            self.x = SOLUTION[0]
            SOLUTION.pop()

            self.p = -(self.x)
            self.q = -(self.x)

            b = sp.symbols("b")
            c = sp.symbols("c")
            p = sp.symbols("p")
            q = sp.symbols("q")
            x = sp.symbols("x")

        

            fig0, ax0 = plt.subplots()
            y = 0.9

            canvas_list = []

            ax0.text(0.4, y, f'Equation: ', ha="center", va="center", fontsize=20, color="black")
            y = y - 0.20

            x = sp.symbols("x")
            self.equation = sp.Eq(self.a*x**2 + self.b*x + self.c, 0)
            latex_equation = sp.latex(self.equation)

            ax0.text(0.4, y, f'${latex_equation}$', ha="center", va="center", fontsize=20, color="black")
            y = y - 0.20

            ax0.text(0.4, y, f'${'a = '+ str(self.a)}$', ha="center", va="center", fontsize=20, color="black")
            y = y - 0.15

            ax0.text(0.4, y, f'${'b = '+ str(self.b)}$', ha="center", va="center", fontsize=20, color="black")
            y = y - 0.15

            ax0.text(0.4, y, f'${'c = '+ str(self.c)}$', ha="center", va="center", fontsize=20, color="black")
            y = y - 0.15

            ax0.set_xlim(0, 1)
            ax0.set_ylim(0, 1)

            # Remove axes
            ax0.axis('off')
            canvas0 = FigureCanvas(fig0)
            canvas_list.append(canvas0)
            

            fig1, ax1 = plt.subplots()
            y = 0.9

            ax1.text(0.4, y, f'Factoring formulas: ', ha="center", va="center", fontsize=20, color="black")
            y = y - 0.20



            show_rootage = sp.Eq((x+p)*(x+q), 0)
            show_rootage = sp.latex(show_rootage)
            ax1.text(0.4, y, f'${str(show_rootage)}$', ha="center", va="center", fontsize=20, color="black")
            y -= 0.15

            show_b = sp.Eq(b, p+q)
            show_b = sp.latex(show_b)
            ax1.text(0.4, y, f'${str(show_b)}$', ha="center", va="center", fontsize=20, color="black")
            y -= 0.15

            show_c = sp.Eq(c, p*q)
            show_c = sp.latex(show_c)
            ax1.text(0.4, y, f'${str(show_c)}$', ha="center", va="center", fontsize=20, color="black")
            y -= 0.15

            ax1.set_xlim(0, 1)
            ax1.set_ylim(0, 1)

            # Remove axes
            ax1.axis('off')
            canvas1 = FigureCanvas(fig1)
            canvas_list.append(canvas1)

            fig2, ax2 = plt.subplots()
            y = 0.9

            ax2.text(0.4, y, f'Solutions: ', ha="center", va="center", fontsize=20, color="black")
            y = y - 0.17

            rootage = sp.Eq((x+self.p)*(x+self.q), 0)
            rootage = sp.latex(rootage)
            ax2.text(0.4, y, f'${str(rootage)}$', ha="center", va="center", fontsize=20, color="black")
            y -= 0.15

            show_x1 = sp.Eq(x+self.p,0)
            show_x1 = sp.latex(show_x1)
            ax2.text(0.4, y, f'${str(show_x1)}$', ha="center", va="center", fontsize=20, color="black")
            y -= 0.15

            sol_x1 = sp.Eq(x,self.x)
            sol_x1 = sp.latex(sol_x1)
            ax2.text(0.4, y, f'${str(sol_x1)}$', ha="center", va="center", fontsize=20, color="black")


            ax2.set_xlim(0, 1)
            ax2.set_ylim(0, 1)

            # Remove axes
            ax2.axis('off')
            canvas2 = FigureCanvas(fig2)
            canvas_list.append(canvas2)

        return canvas_list




    def Square(self):
        try:
            EQUATION = self.equation
            x = sp.symbols("x")
            

            if self.a != 1:
                c = self.c/self.a
                b = self.b/self.a

            else:
                c = self.c
                b = self.b

            b2 = b/2

            fig0, ax0 = plt.subplots()
            y = 0.9

            canvas_list = []

            ax0.text(0.4, y, f'Equation: ', ha="center", va="center", fontsize=20, color="black")
            y = y - 0.20

            x = sp.symbols("x")
            self.equation = sp.Eq(self.a*x**2 + self.b*x + self.c, 0)
            latex_equation = sp.latex(self.equation)

            ax0.text(0.4, y, f'${latex_equation}$', ha="center", va="center", fontsize=20, color="black")
            y = y - 0.20

            ax0.text(0.4, y, f'${'a = '+ str(self.a)}$', ha="center", va="center", fontsize=20, color="black")
            y = y - 0.15

            ax0.text(0.4, y, f'${'b = '+ str(self.b)}$', ha="center", va="center", fontsize=20, color="black")
            y = y - 0.15

            ax0.text(0.4, y, f'${'c = '+ str(self.c)}$', ha="center", va="center", fontsize=20, color="black")
            y = y - 0.15

            ax0.set_xlim(0, 1)
            ax0.set_ylim(0, 1)

            # Remove axes
            ax0.axis('off')
            canvas0 = FigureCanvas(fig0)
            canvas_list.append(canvas0)



            fig1, ax1 = plt.subplots()
            y = 0.9

            spx = sp.symbols(f'{x}')
            spa = sp.symbols(f'{self.a}')
            spb = sp.symbols(f'{self.b}')
            spc = sp.symbols(f'{self.c}')

            ax1.text(0.4, y, f'Square: ', ha="center", va="center", fontsize=20, color="black")
            y = y - 0.20


            if self.a != 1:
                equation1 = sp.Eq((spa*spx**2 + spb*spx + spc)/spa, 0)
                equation1 = sp.latex(equation1)
                ax1.text(0.4, y, f'${str(equation1)}$', ha="center", va="center", fontsize=20, color="black")
                y = y - 0.15


            b22 = sp.symbols(f'{b2**2}')
            devided = sp.Eq(x**2 + b*x + b22, b22 + c*-1)
            devided = sp.latex(devided)
            ax1.text(0.4, y, f'${devided}$', ha="center", va="center", fontsize=20, color="black")
            y = y - 0.15

            b_2 = sp.symbols(f'{b2}')
            square = sp.Eq((x+b_2)**2, b2**2 - c)
            square = sp.latex(square)
            ax1.text(0.4, y, f'${square}$', ha="center", va="center", fontsize=20, color="black")
            y = y - 0.15

            ax1.set_xlim(0, 1)
            ax1.set_ylim(0, 1)

            # Remove axes
            ax1.axis('off')
            canvas1 = FigureCanvas(fig1)
            canvas_list.append(canvas1)




            fig2, ax2 = plt.subplots()
            y = 0.9

            x1 = sp.symbols("x1")
            x2 = sp.symbols("x2")

            ax2.text(0.4, y, f'Calculation of roots:', ha="center", va="center", fontsize=20, color="black")
            y = y - 0.2

            first_line = sp.Eq((x1 + b2), (round(float((sp.sqrt(b2**2 - c))),2))*-1) 
            first_line = sp.latex(first_line)
            ax2.text(0.4, y, f'${first_line}$', ha="center", va="center", fontsize=20, color="black")
            y = y - 0.15


            if b != 0:
                calc_x1 = sp.Eq(x1, round(float(-(sp.sqrt(b2**2 - c)) - b2),1))
                calc_x1 = sp.latex(calc_x1)
                ax2.text(0.4, y, f'${calc_x1}$', ha="center", va="center", fontsize=20, color="black")
                y = y - 0.20


            first_line = sp.Eq((x2 + b2), (round(float((sp.sqrt(b2**2 - c))),2)))
            first_line = sp.latex(first_line)
            ax2.text(0.4, y, f'${first_line}$', ha="center", va="center", fontsize=20, color="black")
            y = y - 0.15
            
            if b != 0:
                calc_x2 = sp.Eq(x2, round(float((sp.sqrt(b2**2 - c)) - b2), 1))
                calc_x2 = sp.latex(calc_x2)
                ax2.text(0.4, y, f'${calc_x2}$', ha="center", va="center", fontsize=20, color="black")
                y = y - 0.20

            ax2.set_xlim(0, 1)
            ax2.set_ylim(0, 1)

            # Remove axes
            ax2.axis('off')
            canvas2 = FigureCanvas(fig2)
            canvas_list.append(canvas2)

            return canvas_list
        
        except TypeError:
            return False








class Equation (Expression):
    def __init__(self, type):
        self.type = type


    def equation_genr(self, complex_chance=False): 
        
        ### 20% for a complex (so far only) inequality   

        if (complex_chance) and (random.randint(1,5) == 1):
            self.iscomplex = True
            self.a = 0
            self.b = 0
            self.c = 0
                                                      # retrospective by discriminant
            while 4*self.a*self.c <= self.b**2:
                self.a = random.choice([i for i in range(-2,5) if i not in [0]])
                self.b = random.choice([i for i in range(-15,15) if i not in [0]])
                self.c = random.choice([i for i in range(-150,150) if i not in [0]])




        ### 80% for a normal (so far only) inequality
                                                      # retrospective by factoring
        else:       
            self.iscomplex = False
            self.x1 = random.choice([i for i in range(-20,20) if i not in [0]])   

            try:
                if self.type == "complete":
                    self.x2 = random.choice([i for i in range(-20,20) if i not in [0, -self.x1]])

                elif self.type == "incomplete":
                    if "b" == random.choice(["b", "c"]):
                        self.x2 = -self.x1

                    else:                                    # c
                        self.x2 = 0

            except:
                self.x2 = random.choice([i for i in range(-20,20) if i not in [0, -self.x1]])



            self.p = -self.x1
            self.q = -self.x2

            self.a = 1
            self.b = self.p + self.q
            self.c = self.p * self.q

            if bool(random.getrandbits(1)):
                self.a = random.choice([i for i in range(-5,5) if i not in [0,1]])
                self.b = self.b * self.a
                self.c = self.c * self.a





        x = sp.symbols("x")
        self.equation = sp.Eq(self.a*x**2 + self.b*x + self.c, 0)
        
        if not self.iscomplex:        
            self.solution = sp.solve(self.equation, x)       

        else:
            self.solution = sp.EmptySet                 







class Inequality (Equation):
    def __init__(self):
        pass
        

    def inequality_genr(self):
        self.equation_genr(True)
        self.critical_pts = self.equation
        self.Cpts_solution = self.solution



        x = sp.symbols("x")
        operator = random.randint(1,4)

        if operator == 1:
            self.inequality = self.a*x**2 + self.b*x + self.c > 0

        elif operator == 2:
            self.inequality = self.a*x**2 + self.b*x + self.c < 0

        elif operator == 3:
            self.inequality = self.a*x**2 + self.b*x + self.c >= 0

        else:
            self.inequality = self.a*x**2 + self.b*x + self.c <= 0



        self.solution = sp.solve_univariate_inequality(self.inequality, x, relational=False)





    def solving(self):
        print ("..................................................")

        print("Solving by finding the critical points")
        print("")
        print("")

        sp.pprint(self.inequality)
        print("")
        sp.pprint(self.critical_pts)
        print("")
        print("")




        if self.iscomplex == False:

            method = input("Which method do you want to see (Square/Factoring/Discriminant): ")

            if method == "Square":
                self.Square(self.critical_pts)

            elif method == "Factoring":
                self.Factoring(self.Cpts_solution)

            elif method == "Discriminant":
                self.Discriminant()

            print("")
            print("")
            print(f"Now when we have the critical points, we can apply them on the interval and slice it into several parts.")
            print("We choose random points from each interval and substitute the 'x' in the original inequality.")
            print(f"Finally, we get the result: {self.solution}")





        else:
            print(f"Result of th equation is a complex number")
            print("That means that there is no real number solution for the equation in the point 0")
            print('')
            print("That leaves us only with 2 options:     1. x = R          2. x = {} ")
            print('')
            print('')
            print("We choose any random point on the number line and substitute the 'x' in the original inequality.")
            print(f"Finally, we get the result: {self.solution}")




                                                         # this function will be called in the
                                                         # expWindow method
def genr_expression(expression, amount, type=False):
    problems = []

    for i in range(amount):
        if expression == "Equation":
            problems.append(Equation(type))

        elif expression == "Inequality":
            problems.append(Inequality())


    for problem in problems:
        if expression == "Equation":
            if type == "complete":
                problem.equation_genr(True)        
            elif type == "incomplete":
                problem.equation_genr(False)

        elif expression == "Inequality":
            problem.inequality_genr()


    return render(problems, expression), problems



def render(problems, expression):
    fig, ax = plt.subplots()
    y = 1.021

    for problem in problems:
        if expression == "Equation":
            latex_form = sp.latex(problem.equation)
            ax.text(0.3, y, f'${latex_form}$', ha="center", va="center", fontsize=20, color="black")
            y = y - 0.108


        elif expression == "Inequality":
            latex_form = sp.latex(problem.inequality)
            ax.text(0.3, y, f'${latex_form}$', ha="center", va="center", fontsize=20, color="black")
            y = y - 0.108

    # Set plot limits
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # Remove axes
    ax.axis('off')


    canvas = FigureCanvas(fig)
    return canvas





if __name__ == "__main__":
    genr_expression("Equation", 3, "complete")