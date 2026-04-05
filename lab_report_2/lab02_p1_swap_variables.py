a = input("Enter first value a: ")
b = input("Enter second value b: ")

print(f"Current values, a: {a}, b: {b}")

a, b = b, a

print(f"After swapping: ")
print(f"New values, a: {a}, b: {b}")