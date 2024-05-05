import sympy as sp
import random



class Expression:

    def Discriminant(self):
        print ("Calculation of discriminant: ")

        D = sp.symbols ("D")
  
        a = sp.symbols ("a")
        b = sp.symbols ("b")
        c = sp.symbols ("c")

        show_discriminant = sp.Eq(D, b**2 - 4*a*c)
        sp.pprint(show_discriminant)
        discriminant = sp.Eq(D, self.b**2 - 4*self.a*self.c)


        if (4*self.a*self.c)<0:
            print ("D =", self.b**2, "+", -4*self.a*self.c)
        else:
            print ("D =", self.b**2, "-", 4*self.a*self.c)

        D_list = sp.solve(discriminant)
        sp.pprint(discriminant)
        print ("..................................................")

        print("Calculation of x1: ")

        x1 = sp.symbols("x1")

        show_solution1 = sp.Eq(x1, (-b -(sp.sqrt(D)))/(2*a))
        sp.pprint(show_solution1)
        solution1 = sp.Eq(x1, (-self.b -(sp.sqrt(D_list[0])))/(2*self.a))

        show_solution1 = sp.Eq(x1, (-self.b -(sp.sqrt(D_list[0])))/(2*a))
        sp.pprint(show_solution1)
        x1_list = sp.solve(solution1)
        sp.pprint(solution1)

        print ("..................................................")
        
        print("Calculation of x2: ")

        x2 = sp.symbols("x2")

        show_solution2 = sp.Eq(x2, (-b +(sp.sqrt(D)))/(2*a))
        sp.pprint(show_solution2)
        solution2 = sp.Eq(x2, (-self.b +(sp.sqrt(D_list[0])))/(2*self.a))

        show_solution2 = sp.Eq(x2, (-self.b +(sp.sqrt(D_list[0])))/(2*a))
        sp.pprint(show_solution2)
        x2_list = sp.solve(solution2)
        sp.pprint(solution2)




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
    def __init__(self,type):
        self.type = type



    def EquationSetup(self):

        if self.type == "complete":
            self.a = random.randint(1,5)
            self.b = random.randint(-5,15)
            self.c = random.randint(-150,150)


            
            if self.b == 0 or self.c == 0:
                self.EquationSetup()

            else:
                self.EquationGenr()



        elif self.type == "incomplete":
            self.excluded = random.choice(["b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","c"])

            if self.excluded == "c":
                self.a = random.randint(1,5)
                self.b = random.randint(-5,15)
                self.c = 0

                if self.b == 0:
                    self.EquationSetup()

                else:
                    self.EquationGenr()


                    

            elif self.excluded == "b":
                self.a = random.randint(1,5)
                self.b = 0
                self.c = random.randint(-50,50)

                if self.c == 0:
                    self.EquationSetup()

                else:
                    self.EquationGenr()







    def EquationGenr(self):

        iscomplex = False
        self.one_solution = False

        x = sp.symbols("x")
        self.equation = sp.Eq(self.a*x**2 + self.b*x + self.c, 0)
        self.solution = sp.solve(self.equation)



                            # regulation ---> filtering out 1.not-whole numbered roots
                            #                               2.complex roots


        for sol in self.solution:
            if isinstance(sol, sp.Expr) and sol.has(sp.I):
                iscomplex = True


        if iscomplex:
            self.EquationSetup()

        else:
            if len(self.solution) == 1:
                self.one_solution = True

            if not (int(self.solution[0]*10) == float(self.solution[0]*10) and (self.one_solution or int(self.solution[1]*10) == float(self.solution[1]*10))):
                self.EquationSetup()

                            # regulation
    












class Inequality (Expression):
    def __init__(self):
        pass

    
    def InequalitySetup(self):
        self.a = random.randint(-5,5)
        self.b = random.randint(-5,15)
        self.c = random.randint(-150,150)

        
        if self.a == 0:
            self.InequalitySetup()

        else:
            self.InequalityGenr()






    def InequalityGenr(self):

        symbol = random.randint(1,4)
        x = sp.symbols("x")

        if symbol == 1:
            self.inequality = self.a*x**2 + self.b*x + self.c > 0

        elif symbol == 2:
            self.inequality = self.a*x**2 + self.b*x + self.c < 0

        elif symbol == 3:
            self.inequality = self.a*x**2 + self.b*x + self.c >= 0

        else:
            self.inequality = self.a*x**2 + self.b*x + self.c <= 0




                        # regulation  ---> filtering out                   1. not-whole numbered roots
                        #             ---> leaving room for possibility    1. complex roots


        self.one_solution = False
        iscomplex = False
        self.allow_complex = 0
        
        self.critical_pts = sp.Eq(self.a*x**2 + self.b*x + self.c, 0)
        self.Cpts_solution = sp.solve(self.critical_pts)



        for sol in self.Cpts_solution:
            if isinstance(sol, sp.Expr) and sol.has(sp.I):
                iscomplex = True
                self.allow_complex = random.randint(1,30)           # 1 --> True


        if iscomplex and self.allow_complex != 1:
            self.InequalitySetup()
        
        else:
            if self.allow_complex != 1:
                if len(self.Cpts_solution) == 1:
                    self.one_solution = True

                if not (int(self.Cpts_solution[0]*10) == float(self.Cpts_solution[0]*10) and (self.one_solution or int(self.Cpts_solution[1]*10) == float(self.Cpts_solution[1]*10))):
                    self.InequalitySetup()


           
                        # regulation





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





        if self.allow_complex != 1:

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

