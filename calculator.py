from arithmetic import *

def calculator():
    expression = raw_input().strip()
    input_list = expression.split(" ")
    #based on example calculator.pyc, format is always function,num1,num2
    function = input_list[0]
    num1 = input_list[1]
    num2 = input_list[2]

calculator()