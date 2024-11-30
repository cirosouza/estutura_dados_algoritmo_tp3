def torre_de_hanoi(n,origem, auxiliar, destino):
    # Caso mais simples: mover um único disco diretamente para o pino de destino
    if n == 1:
        print(f"Mova o disco 1 de {origem} para {destino}")
        return
    
    # Primeiro Passo: Mover n-1 discos da origem para o pino auxiliar
    # Troca dos parametros "destino" e "auxiliar", pois os pinos sairão da coluna de origem para a auxiliar
    torre_de_hanoi(n - 1, origem, destino, auxiliar)

    # Segundo Passo: Mover o maior disco (n) para o pino de destino
    print(f"Mova o disco {n} de {origem} para {destino}")

    # Terceiro Passo: Mover n-1 discos do pino auxiliar para o destino (que já consta com o disco n) 
    # Troca da posição de todos os parametros, porque os pinos estarão na coluna auxiliar e deverão ser movimentados para o destino
    torre_de_hanoi(n - 1, auxiliar, origem, destino)


    