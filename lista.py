# Declaração

minha_lista = [1, 2, 3, 4, 5, "rockseat", True, False]

#Exibindo a lista
print("Minha lista de exemplo", minha_lista)

#Exibindo a lista
print(minha_lista[0])
print(minha_lista[5])
print(minha_lista[1:7])
print(minha_lista[:6])
print(minha_lista[2:])

#Métodos de listas

#Método append(): adicona um elemento no final da lista
minha_lista.append(6)
print("Após append(6):", minha_lista)

#Método index

indice = minha_lista.index(6)
print("Indice do elemento 6", indice)

#Método insert: Insere um elemento em um indice especifico
minha_lista.insert(2, 10)
print("Após o insert (2,10):", minha_lista)

# Método pop
elemento_removido = minha_lista.pop(3)
print("Elemento removido:", elemento_removido)
print("Após o pop (3)", minha_lista)

#Método remove

minha_lista.remove(False)
print("Após remove(False):", minha_lista)

# Método sort
#minha_lista.sort()
#print("Após sort()", minha_lista)