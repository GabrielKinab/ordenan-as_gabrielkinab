import random

# Função para realizar a ordenação natural
def ordenar_natural(lista):
    return sorted(lista)

# Função para realizar a ordenação customizada
def ordenar_customizada(lista):
    return sorted(lista, key=lambda s: s.lower())

# Função para realizar a ordenação total de uma lista de dicionários
def ordenar_total(lista, chave):
    return sorted(lista, key=lambda item: item[chave])

# Função para gerar uma lista aleatória de frutas para ordenação natural e customizada
def gerar_lista_frutas():
    frutas = [
        "Banana", "abacaxi", "Maçã", "laranja", "Goiaba",
        "Melancia", "Morango", "Pêra", "Cereja", "Uva",
        "Limão", "Kiwi", "Ameixa", "Pêssego", "Mamão"
    ]
    return random.sample(frutas, random.randint(5, 15))

# Função para gerar uma lista aleatória de produtos para ordenação total
def gerar_lista_produtos():
    produtos = [
        {"nome": "Camisa", "preco": 40.00},
        {"nome": "Calça", "preco": 70.00},
        {"nome": "Bermuda", "preco": 30.00},
        {"nome": "Jaqueta", "preco": 150.00},
        {"nome": "Chinelo", "preco": 20.00},
        {"nome": "Tênis", "preco": 120.00},
        {"nome": "Boné", "preco": 25.00},
        {"nome": "Meias", "preco": 10.00},
        {"nome": "Blusa", "preco": 60.00},
        {"nome": "Casaco", "preco": 200.00},
        {"nome": "Saia", "preco": 45.00},
        {"nome": "Vestido", "preco": 80.00},
        {"nome": "Cinto", "preco": 15.00},
        {"nome": "Gravata", "preco": 35.00},
        {"nome": "Luvas", "preco": 18.00}
    ]
    return random.sample(produtos, random.randint(5, 15))

# Geração de listas aleatórias
lista_frutas = gerar_lista_frutas()
lista_produtos = gerar_lista_produtos()

# Exemplo de ordenação natural
lista_ordenada_natural = ordenar_natural(lista_frutas)
print("Ordenação Natural (frutas):")
print(lista_ordenada_natural)

# Exemplo de ordenação customizada
lista_ordenada_customizada = ordenar_customizada(lista_frutas)
print("\nOrdenação Customizada (frutas):")
print(lista_ordenada_customizada)

# Exemplo de ordenação total pela chave 'preco'
lista_ordenada_total = ordenar_total(lista_produtos, 'preco')
print("\nOrdenação Total (produtos por preço):")
for produto in lista_ordenada_total:
    print(f"{produto['nome']} - R$ {produto['preco']:.2f}")