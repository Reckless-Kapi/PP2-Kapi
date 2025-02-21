import math

def radian():
    degree = float(input("Input degree: "))
    radian = degree * (math.pi / 180)
    print(f"Output radian: {radian:.6f}")

radian()
