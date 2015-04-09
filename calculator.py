from arithmetic import *


operators = ["+", "-", "*", "square", "cube", "pow", "mod"]


def do_setup():
    expression = raw_input().strip()    #take input and strips white space
    input_list = expression.split(" ") #makes [function, num1, num2] from string expression

    return input_list


def evaluate_input(function, num1, num2): #function, num1, and num2 are strings at this point
    num1 = int(num1)
    num2 = int(num2)

    if function in operators:
        if function == "+":
            return add(num1, num2)
        elif function == "-":
            return subtract(num1, num2)
        elif function == "*":
            return multiply(num1, num2)
        elif function == "/":
            return divide(num1, num2)
        elif function == "square":
            return square(num1, num2)
        elif function == "cube":
            return cube(num1, num2)
        elif function == "pow":
            return power(num1, num2)
        elif function == "mod":
            return mod(num1, num2)
    else:
        print "I don't understand"


def calculator():
    while (expression != "q"):
        input_list = do_setup()

        #based on example calculator.pyc, order is always function,num1,num2
        function = input_list[0]
        num1 = input_list[1]
        num2 = input_list[2]

        output = evaluate_input(function, num1, num2)
        print output


calculator()