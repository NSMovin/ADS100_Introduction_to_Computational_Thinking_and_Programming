def largest_num(num1, num2):
    if num1 > num2:
        print(f"Largest number is {num1}")
    else:
        print(f"Largest number is {num2}")


n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

largest_num(n1, n2)