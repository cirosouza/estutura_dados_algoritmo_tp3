def conta_caracteres_repetidos(palavra, x):
    if len(palavra) == 0:
        return 0
    
    return (1 if palavra[0] == x else 0) + conta_caracteres_repetidos(palavra[1:],x)

print(conta_caracteres_repetidos("abracadabra", "a"))

