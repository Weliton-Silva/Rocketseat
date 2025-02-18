# Exemplo
def saudacao(nome):
    print(f"Olá, {nome}!")

print("\nChamando a função saudação:")
saudacao("Alice")
saudacao("Bob")

# Funcao com retorno
def quadrado(numero):
    resultado = numero ** 2
    return resultado
print("\nChamando a função quadrado:")
resultado_quadrado = quadrado(5)
print("Resultado da função quadrado: ", resultado_quadrado)

#Função com multiplos paramentros
def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

print("\nChamando a função soma:")
resultado_soma = soma(20,50)
print("A soma do numero 20 e 50 é ", resultado_soma)