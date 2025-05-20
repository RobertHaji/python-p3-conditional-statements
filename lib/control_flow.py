#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if username.lower() == "admin" and password == "12345":
        return "Access granted"
    else:
        return "Access denied"
    pass

def hows_the_weather(temperature):
    # your code here

    if temperature < 40:
        return "It's brisk out there!"
    elif 40<= temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"
    pass
    # your code here

def calculator(operation, num1, num2):
    # your code here
     if operation == '+':
        return num1 + num2
     elif operation == '-':
        return num1 - num2
     elif operation == '*':
        return num1 * num2
     elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero!"
     else:
        print("Invalid operation!")
        return None
     pass

def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number