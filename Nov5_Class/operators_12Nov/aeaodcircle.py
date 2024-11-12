r = float(input("Enter the radius value:\n"))
a = 3.14 * pow(r, 2)
print("Area of circle:", a)
print(f"Area: {a:.2f}")


# / or a=3.14*(r**2)
#/2nd way using math librry
import math
r=float(input("radius:"))
a=math.pi*math.pow(r,2)
print(f"area:, {a:.4f}")