#Calculator
from replit import clear
from art import logo
#Add 
def add(n1,n2):
    return n1 + n2

#Subtract
def subtract(n1,n2):
    return n1 - n2 

#Multiply
def multiply(n1, n2):
    return n1 * n2 

#Divide
def divide(n1, n2):
    return n1 / n2

#square
def square(n1, n2):
    return n1 ** n2     

#Create a dictionary named operations
operations = {
 "+": add,
 "-": subtract,
 "*": multiply,
 "/": divide,
 "^": square, 
}

def calculator():
    print(logo)
    num1 = float(input("What\'s the first number?: "))
    #Loop that print the chararcter of the operations
    for operation in operations:
        print(operation)

    should_continue = True

    while should_continue:    
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]
        first_answer = calculation_function(num1, num2)
        
        print(f"{num1} {operation_symbol} {num2} = {first_answer}")

        if input(f"Type 'Y' to continue calculating with {first_answer}, or type 'N' to start a new calculator: \n").lower() == "y":
            num1 = first_answer
        else:
            clear()   
            should_continue = False
            #Recursion
            #al llamar a la funcion dentro de si
            #empieza desde el principio
            calculator()

calculator()   
        
    

