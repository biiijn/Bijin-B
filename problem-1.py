class Calculator:
    a=float(input("Enter first number: "))
    b=float(input("Enter second number: "))
    opr=input("Enter operation(add/subtract/multiply/divide): ").lower()
    
    if opr == "add":
        result=a+b
    elif opr == "subtract":
        result=a-b
    elif opr == "multiply":
        result=a*b
    elif opr == "divide":
        if b == 0:
            result = "Error: Cannot divide by zero"
        else:
            result = a / b
    else:
        result = "Error: Invalid operation"
print("Result: ", Calculator.result)