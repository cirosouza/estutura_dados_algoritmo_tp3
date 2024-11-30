def fibonacci(n, memo={}):

    # Verifica se o resultado já foi armazeinado
    if n in memo:  
        return memo[n]
    # Soluciona o caso básico
    if n <= 2:
        return 1
    # Calcula e armazena o resultado
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

def fatorial_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


