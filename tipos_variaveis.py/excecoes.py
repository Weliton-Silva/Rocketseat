print("Exemplo de captura de exceçôes")
try:
    numero = input(int("Digite um número inteiro: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except ValueError as e:
    print(f"Erro de Value error: {e}")
    raise ValueError("Tipo de variaveis incompativeis")
except Exception as e:
    print(f"Erro: {e}")
else:
    print(f"Resultado {resultado}")
finally:
    print("Operação finalizada")