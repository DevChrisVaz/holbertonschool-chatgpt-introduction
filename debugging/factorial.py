import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n = n - 1
    return result

if len(sys.argv) != 2:
    print("Usage: python script.py <integer>")
    sys.exit(1)

try:
    num = int(sys.argv[1])
    if num < 0:
        print("Error: The input must be a non-negative integer.")
        sys.exit(1)
except ValueError:
    print("Error: The input must be an integer.")
    sys.exit(1)

f = factorial(num)
print(f)