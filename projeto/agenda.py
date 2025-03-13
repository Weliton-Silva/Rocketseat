def novo_contato(nome, telefone, email, favorito: False):
    contato[nome] = {
        "telefone":telefone,
        "email": email,
        "favorito": favorito
    }
    return contato
def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o número do contato: ")
    email = input("Digite o email do seu contato: ")
    favorito = input("O contato é favorito ? (sim/nao): ").strip().lower()
    favorito_verificacao = True if favorito =="sim" else False

    novo_contato(nome, telefone, email, favorito)






contato = {}
titulo = "AGENDA DE CONTATOS"
largura = 50
caracteres = "="
titulo_centralizado = titulo.center(largura,caracteres)
while True:
    print(titulo_centralizado)
    print("\n01. Adicionar novo contato")
    print("02. Ver lista de contatos")
    print("03. Editar contato")
    print("04. Salvar um novo contato como favorito")
    print("05. Remover um contatos da lista de favoritos")
    print("06. Apagar contato")
    print("07. Sair")
    break

escolha = input("Digite a opção desejada: ")

if escolha == "1":
    while True:
        adicionar_contato()
        continuar = input("Deseja adicionar mais algum contato? (sim/nao): ").strip().lower()
        if continuar != "sim":
            break
elif escolha == "2":
    print("Lista de contatos:")
    for nome, dados in contato.item():
         print(f"Nome: {nome}, Telefone: {dados['telefone']}, Email: {dados['email']}, Favorito: {dados['favorito']}")
elif escolha == "7":
        print("Aplicação encerrada")
    

