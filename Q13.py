def verifica_palindromo(palavra):
    if len(palavra) == 1 or len(palavra) == 0:
        return True
    
    primeira_letra = palavra[:1]
    ultima_letra = palavra[-1:]
    palavra_cortada = palavra[1:-1]

    return primeira_letra == ultima_letra and verifica_palindromo(palavra_cortada)

print(verifica_palindromo("4554"))
print(verifica_palindromo("ovo"))
print(verifica_palindromo("roma é amor"))
print(verifica_palindromo("renner"))
print(verifica_palindromo("chico"))
print(verifica_palindromo("casa"))





