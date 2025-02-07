def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime():
    numbers_str = input().split()
    numbers = []
    
    for num in numbers_str:
        numbers.append(int(num))
    
    primes = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)

    print("Prime: ", primes)

filter_prime()
