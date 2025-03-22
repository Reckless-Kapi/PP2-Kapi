import time
import math

number = int(input("number"))
delay_ms = int(input("delay in milliseconds: "))

time.sleep(delay_ms / 1000) 
sqrt_result = math.sqrt(number)

print(f"Square root of {number} after {delay_ms} milliseconds is {sqrt_result}")
