print("for utilizando lista")
lista = [1, 2, 3, 4, 5]
for elemento in lista:
    print(elemento)


print("for utilizando tupla")
tupla = (1, 2, 3, 4, 5)
for elemento in tupla:
    print(elemento)

pessoa = {"nome": "joão", "idade": 30, "cidade": "São Paulo"}
print("\nFor utilizando dicionario - chaves")
for chave in (pessoa.keys()):
    print(chave)

print("\nFor utilizando dicionario - valores")

for chave in (pessoa.values()):
    print(chave)

print("\nFor Utilizando dicionario - valores")

for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")
