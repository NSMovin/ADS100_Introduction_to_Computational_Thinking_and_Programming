def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

result_add = addition(n1, n2)
result_sub = subtraction(n1, n2)
result_mul = multiplication(n1, n2)
result_div = division(n1, n2)

print(f"The result of addition of {n1} and {n2} is : {result_add}")
print(f"The result of subtraction {n1} and {n2} is : {result_sub}")
print(f"The result of multiplication of {n1} and {n2} is : {result_mul}")
print(f"The result of division {n1} and {n2} is : {result_div:.2f}")
