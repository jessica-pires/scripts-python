# Tupla com produtos
produtos = ("Maçã", "Banana", "Laranja", "Abacaxi", "Uva  ")

# Tupla com preços
precos = (1.0, 0.8, 1.2, 2.5, 3.0)

# Imprime cabeçalho da tabela
print("Produto\t\tPreço")

# Loop para percorrer as tuplas e exibir os dados
for produto, preco in zip(produtos, precos):
    print(f"{produto}\t\t{preco:.2f}")
