def inverte_string(texto):
    if len(texto) == 0:
        return ""

    return texto[-1] + inverte_string(texto[:-1])

print(inverte_string("inacreditavel"))

print(inverte_string("recursão"))


