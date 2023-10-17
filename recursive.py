
num = int(input('enter a number:'))

def factorial_recursive (n):
    if n == 1 or n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return n * factorial_recursive(n - 1)

factorial = factorial_recursive(num)

print(factorial)

# vs

def factorial_normal (n):
    factorial = 1
    if n < 0:
        return 0
    for i in range(1, n + 1):
        factorial = factorial * i
    return factorial

nonRec_factorial = factorial_normal(num)

print(nonRec_factorial)