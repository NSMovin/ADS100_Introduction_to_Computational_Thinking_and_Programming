import math

def volume(radius, height):
    return math.pi * radius**2 * height

def surface_area(radius, height):
    return 2 * math.pi * radius**2 + (2 * math.pi * radius * height)

r = float(input("Enter radius: "))
h = float(input("Enter height: "))

v = volume(r, h)
s = surface_area(r, h)

print(f"The volume is: {v:.2f}")
print(f"The surface area is: {s:.2f}")