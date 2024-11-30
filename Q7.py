def quickselect(lista, k):

    # Soluciona o caso base da lista com somente um elemento
    if (len(lista) == 1):
        return lista[0]
    
    # O pivot escolhido é o último elemento
    pivot = lista[-1]

    # Particiona a lista em relação ao pivot
    menores = [x for x in lista if x < pivot]
    iguais = [x for x in lista if x == pivot]
    maiores = [x for x in lista if x > pivot]
    
    # Define a posição do pivot em comparação aos numeros menores
    posicao_pivot = len(menores) + 1

    # Verifica se o elemento está na sublista dos menores, se sim, a função é chamada novamente
    if k < posicao_pivot:  
        return quickselect(menores, k)
    # Verifica se o elemento está na sublista dos maiores, se sim, a função é chamada novamente
    elif k > posicao_pivot: 
        # como o pivot é menor que o k-ésimo menor numero, o indice é corrigido para a nova chamada
        return quickselect(maiores, k - posicao_pivot)
    # Caso em que o pivot é o k-ésimo menor elemento
    else:  
        return pivot
    