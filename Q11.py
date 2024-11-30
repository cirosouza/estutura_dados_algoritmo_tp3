def fatorial_recursivo(num):
    # Soluciona os casos bases para 0 e 1
    if num == 0 or num == 1:
        return 1
    
    return num * fatorial_recursivo(num - 1)



def fatorial_iterativo(num):
    # Soluciona os casos bases para 0 e 1
    if num == 0 or num == 1:
        return 1
    
    fatorial = 1
    for n in range(2, num+1):
        fatorial *= n
    
    return fatorial

print(fatorial_iterativo(1100))

