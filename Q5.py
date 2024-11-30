def quicksort(lista):
    
    #Caso base em que a lista contem somente um elemento
    if len(lista) <= 1:
        return lista
    
    # Sempre escolhe o último elemento como pivô
    pivot = lista[-1]

    # Particionamento da lista em numeros menores que o pivot e numeros maiores
    menores = [num for num in lista[:-1] if num <= pivot]
    maiores = [num for num in lista[:-1] if num > pivot]

    # Reordena de forma recursiva a lista fazendo a subdivisão novamente nas sublistas
    return quicksort(menores) + [pivot] + quicksort(maiores)


