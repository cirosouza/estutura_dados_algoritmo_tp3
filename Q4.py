def fibonacci(n):
    if n<= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def fatorial(n):
    if n == 0 or n == 1:
        return n
    
    return n * fatorial(n-1)

