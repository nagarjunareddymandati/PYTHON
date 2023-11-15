import math
def check_right_triangle(a, b, c):
    sides = sorted([a, b, c])
    if sides[2] == sides[0] + sides[1]:
        return True
    return False
a = float(input("Enter side a: "));
b = float(input("Enter side b: "));
c = float(input("Enter side c: "));
if check_right_triangle(a, b, c):
    print("The triangle is a right triangle");
else:
    print("The triangle is not a right triangle");