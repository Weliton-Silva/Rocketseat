# Criando um dicionário de exemplo
pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

print("Meu dicionário de exemplo:", pessoa)

# Acessando valores por chave
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("cidade:", pessoa["cidade"])

pessoa["sobrenome"] = "Silva"

print("Sobrenome:", pessoa["sobrenome"])

# Removendo um par chave-valor
del pessoa["sobrenome"]

print("Meu dicionario de exemplo:", pessoa)

# Métodos: keys(), values(), items()
chave = pessoa.keys()
print("Chaves do dicionario:", chave)

valores = list(pessoa.values())
print("valores do dicionarios:", valores)
print("Primeiro valor do dicionario:", valores[0])

#Métodos items
itens = (list(pessoa.items()))
print("Pares chave-valor do dicionário:", itens)
print("Primeiro valor:", itens[0][1])
print("Primeira chave-valor: %s = %s" % (itens[0][0], itens[0][1]))