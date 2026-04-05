num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

if num1 < num2:
    print(f"The smallest number between {num1} and {num2} is {num1}")
elif num2 < num1:
    print(f"The smallest number between {num1} and {num2} is {num2}")
else:
    print(f"Both {num1} and {num2} are equal")
    