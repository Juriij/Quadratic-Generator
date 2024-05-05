import functions as fun
import sympy as sp



problem_type = input("What problems should be generated Equation/Inequality? ")
amount = int(input("How many problems should be generated? "))

if problem_type == "Equation":
    type = input("What type of equation should be generated? (complete/incomplete) ")


problems = []

for i in range(amount):
    if problem_type == "Equation":
        problems.append(fun.Equation(type))


    elif problem_type == "Inequality":        
        problems.append(fun.Inequality())



for problem in problems:

    if problem_type == "Equation":
        problem.equation_genr()
        sp.pprint(problem.equation)
        print("")
        print("")

    elif problem_type == "Inequality":
        problem.InequalitySetup()                  ### <----- to be changed          
        sp.pprint(problem.inequality)
        print("")
        print("")




while True:
    action = input("Solution/Explanation: ")

    if problem_type == "Equation": 

        if action == "Solution":
            n_Eq = int(input("Solution for: "))

            if len(problems) < n_Eq or 0 > n_Eq:
                print(f"There is no equation number {n_Eq}, please check the order.") 
                print("")
                print("")
                print("")
            
            else:
                print(problems[n_Eq-1].solution)
                print("")
                print("")




        elif action == "Explanation":
            n_Eq = int(input("Explanation for: "))

            if len(problems) < n_Eq or 0 > n_Eq:
                print(f"There is no equation number {n_Eq}, please check the order.") 
                print("")
                print("")
                print("")


            else:
                method = input("Which method do you want to see (Square/Factoring/Discriminant): ")

                if method == "Square":
                    problems[n_Eq-1].Square(problems[n_Eq-1].equation)

                elif method == "Factoring":
                    problems[n_Eq-1].Factoring(problems[n_Eq-1].solution)

                elif method == "Discriminant":
                    problems[n_Eq-1].Discriminant()







    elif problem_type == "Inequality":

        if action == "Solution":
            n_Eq = int(input("Solution for: "))

            if n_Eq < len(problems) < n_Eq:
                print(f"There is no inequality number {n_Eq}, please check the order.") 
                print("")
                print("")
                print("")


            else:
                print(problems[n_Eq-1].solution)
                print("")
                print("")





        elif action == "Explanation":
            n_Eq = int(input("Explanation for: "))

            if n_Eq < len(problems) < n_Eq:
                print(f"There is no inequality number {n_Eq}, please check the order.") 
                print("")
                print("")
                print("")

            
            else:
                problems[n_Eq-1].solving()