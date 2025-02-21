import math

def polygon():
    n = int(input("Input number of sides: "))
    s = float(input("Input the length of a side: "))

    area = (n * s ** 2) / (4 * math.tan(math.pi / n))
    print(f"The area of the polygon is: {area:.2f}")

polygon()
