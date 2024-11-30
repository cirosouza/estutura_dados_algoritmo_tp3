class Node:
    # Classe que define os nós e cria as relações entre eles
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

    

def percorre_arvore_binaria(node):
    # Soluciona o caso da arvore vazia
    if node is None:
        return []
    
    return (percorre_arvore_binaria(node.left) + [node.data] + percorre_arvore_binaria(node.right))


# Exemplo:

raiz = Node(10)
raiz.left = Node(5)
raiz.right = Node(15)

raiz.left.left = Node(3)
raiz.left.right = Node(7)

raiz.right.left = Node(13)
raiz.right.right = Node(17)

print(percorre_arvore_binaria(raiz))

