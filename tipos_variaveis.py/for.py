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

# range(): intervalo numérico
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#print(list(range(0,10)))
print("\nUtilizando a função range()")
for numero in range(5):
    print("Número",numero)

print("\nUtilizando a função range() com len()")
lista = [1, 2, 3, 4, 5]
for indice in range(0, len(lista)):
    print("indice: ", indice)
    print("Elemento:", lista [indice])
    if indice == 3:
        lista [indice] = 5
    else:
        lista[indice] = 0
print(lista)

# enumerate()
lista_enumerate = ["a", "b", "c"]
for indice, valor in enumerate(lista):
    print(f"{indice}: {valor}")
    if indice == 1:
        print("indice 1")