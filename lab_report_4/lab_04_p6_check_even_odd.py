def check_even_odd(n):
    if n % 2 == 0:
        print(f"{n} is an Even number")
    else:
        print(f"{n} is an Odd number")


num = int(input("Enter a number: "))
check_even_odd(num)