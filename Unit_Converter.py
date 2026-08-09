using=True
menu=["calculator", "unit converter", "length converter", "exit"]
operators=["+", "-", "*", "/", "**", "%"]
def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    else:
        return a / b
def power(a, b):
    return a ** b
def modulo(a, b):
    return a % b
while using:
    print("Welcome to my Calculator, Unit Converter, and Length Converter menu")
    User_choice=input("What would you like to do? (calculator/unit converter/length converter/exit)\n")
    User_choice=User_choice.lower()
    if User_choice in menu:
        if User_choice=="calculator":
            a=float(input("Enter first number:"))
            operation=input("Enter operation (+, -, *, /,**,%):")
            b=float(input("Enter second number:"))
            if operation in operators:
                if operation=="+":
                    print(addition(a, b))
                elif operation=="-":
                    print(subtraction(a, b))
                elif operation=="*":
                    print(multiplication(a, b))
                elif operation=="/":
                    print(division(a, b))
                elif operation=="**":
                    print(power(a, b))
                elif operation=="%":
                    print(modulo(a, b))
            else:
                print("Invalid operation. Please choose from +, -, *, /, **, %.")
        elif User_choice=="unit converter":
            convert_direction=["celsius to fahrenheit", "fahrenheit to celsius"]
            convert_choice=input("What would you like to convert? (celsius to fahrenheit/fahrenheit to celsius)\n")
            convert_choice=convert_choice.lower()
            if convert_choice in convert_direction:
                if convert_choice=="celsius to fahrenheit":
                    celsius=float(input("Enter temperature in Celsius:"))
                    fahrenheit=(celsius * 9/5) + 32
                    print(f"{celsius}°C is equal to {fahrenheit}°F")
                elif convert_choice=="fahrenheit to celsius":
                    fahrenheit=float(input("Enter temperature in Fahrenheit:"))
                    celsius=(fahrenheit - 32) * 5/9
                    print(f"{fahrenheit}°F is equal to {celsius}°C")
        elif User_choice=="length converter":
            length_direction=["km to miles", "miles to km"]
            length_choice=input("What would you like to convert? (km to miles/miles to km)\n")
            length_choice=length_choice.lower()
            if length_choice in length_direction:
                if length_choice=="km to miles":
                    km=float(input("Enter length in kilometers:"))
                    miles=km * 0.621371
                    print(f"{km} kilometers is equal to {miles} miles")
                elif length_choice=="miles to km":
                    miles=float(input("Enter length in miles:"))
                    km=miles / 0.621371
                    print(f"{miles} miles is equal to {km} kilometers")
        elif User_choice=="exit":
            using=False
    else:
        print("Invalid choice. Please choose from calculator, unit converter, or exit.")