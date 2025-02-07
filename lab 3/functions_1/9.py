import math

def sphere_volume():
    radius = float(input())
    volume = (4 / 3) * math.pi * radius**3
    print(f"Volume: {volume:.2f}")

sphere_volume()
