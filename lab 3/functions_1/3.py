def solve():
    numheads = int(input())
    numlegs = int(input())

    x = (4 * numheads - numlegs) // 2
    y = numheads - x

    print(f"chicken: {x}, rabbits: {y}")

solve()
