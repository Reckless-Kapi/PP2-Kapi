def trapezoid():
    height = float(input("Height: "))
    base1 = float(input("Base, first value: "))
    base2 = float(input("Base, second value: "))

    area = ((base1 + base2) * height) / 2
    print(f"Expected Output: {area:.2f}")

trapezoid()
