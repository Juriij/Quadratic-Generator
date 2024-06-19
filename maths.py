import sympy as sp
import random
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas



class Expression:

    def Discriminant(self):
        fig1, ax1 = plt.subplots()
        y = 0.9

        canvas_list = []


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

            fig2, ax2 = plt.subplots()
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

            fig3, ax3 = plt.subplots()
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
        
############################################


    def Factoring(self, SOLUTION):
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
            show_rootage = sp.Eq((x1+p)*(x2+q), 0)
            show_b = sp.Eq(b, p+q)
            show_c = sp.Eq(c, p*q)
            rootage = sp.Eq((x1+self.p)*(x2+self.q), 0)
            show_x1 = sp.Eq(x1+self.p,0)
            sol_x1 = sp.Eq(x1,self.x1)
            show_x2 = sp.Eq(x2+self.q,0)
            sol_x2 = sp.Eq(x2,self.x2)

            sp.pprint(show_rootage)
            sp.pprint(show_b)
            sp.pprint(show_c)
            sp.pprint(rootage)
            sp.pprint(show_x1)
            sp.pprint(sol_x1)
            sp.pprint(show_x2)
            sp.pprint(sol_x2)

        else:
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

            show_rootage = sp.Eq((x+p)*(x+q), 0)
            show_b = sp.Eq(b, p+q)
            show_c = sp.Eq(c, p*q)
            rootage = sp.Eq((x+self.p)*(x+self.q), 0)
            show_x1 = sp.Eq(x+self.p,0)
            sol_x1 = sp.Eq(x,self.x)

            sp.pprint(show_rootage)
            sp.pprint(show_b)
            sp.pprint(show_c)
            sp.pprint(rootage)
            sp.pprint(show_x1)
            sp.pprint(sol_x1)




    def Square(self, EQUATION):
        x = sp.symbols("x")

        c = self.c
        b = self.b
        b2 = b/2

        if self.a != 1:
            c = self.c/self.a
            b = self.b/self.a
            b2 = b/2

        equation1 = sp.Eq((self.a*x**2 + self.b*x + self.c)/self.a, 0)

        sp.pprint (EQUATION)
        if self.a != 1:
            sp.pprint(equation1)

        if c>=0:
            print(f"x**2 + {b*x} + {b2**2} - {b2**2} + {c} = 0")
        else:
            print(f"x**2 + {b*x} + {b2**2} - {b2**2} {c} = 0")

        print(f"(x+{b2})**2 { - b2**2 + c}"," = ",0)
        print(f"(x+{b2})**2  = { b2**2 - c}")
        print(f"(x+{b2}) = - {round(float((sp.sqrt(b2**2 - c))),2)}")
        print(f"(x+{b2}) = {round(float((sp.sqrt(b2**2 - c))),2)}")
        print(f"x1 = { round(float(-(sp.sqrt(b2**2 - c)) - b2),1)}")
        print(f"x2 = { round(float((sp.sqrt(b2**2 - c)) - b2), 1)}")









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
    y = 1

    for problem in problems:
        if expression == "Equation":
            latex_form = sp.latex(problem.equation)
            ax.text(0.4, y, f'${latex_form}$', ha="center", va="center", fontsize=20, color="black")
            y = y - 0.1


        elif expression == "Inequality":
            latex_form = sp.latex(problem.inequality)
            ax.text(0.4, y, f'${latex_form}$', ha="center", va="center", fontsize=20, color="black")
            y = y - 0.1

    # Set plot limits
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # Remove axes
    ax.axis('off')


    canvas = FigureCanvas(fig)
    return canvas





if __name__ == "__main__":
    genr_expression("Equation", 3, "complete")