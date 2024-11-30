def soma_lista(lista_num):
    if not lista_num:
        return 0

    return lista_num[0] + soma_lista(lista_num[1:])


print(soma_lista([20,54,13,87,2,6,45,325,73,64]))