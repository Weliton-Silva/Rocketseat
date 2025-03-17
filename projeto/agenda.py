def novo_contato(nome, telefone, email, favorito: False):
    contato[nome] = {
        "telefone":telefone,
        "email": email,
        "favorito": favorito
    }
    return
def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o número do contato: ")
    email = input("Digite o email do seu contato: ")
    favorito = input("O contato é favorito ? (sim/nao): ").strip().lower()
    favorito_verificacao = True if favorito =="sim" else False
    novo_contato(nome, telefone, email, favorito_verificacao)
    print("Contato Salvo com sucesso !")
    input("Pressione enter para retornar ao menu...")
    return

def exibir_contato():
    print("Lista de contatos: ")
    if contato:
        for nome, dados in contato.items():
            print(f"Nome: {nome}, Telefone: {dados['telefone']}, Email: {dados['email']}, Favorito: {dados['favorito']}")
    else:
        print("Nenhum contato encontrado.")
    return

def editar_contato():
    print("Lista de contatos para edição:")
    if not contato:
        print("Nenhum contato encontrado.")
        return

    for edit, nome in enumerate(contato, 1):
        print(f"{edit}. {nome}")
    
    try:
        escolha = int(input("Digite o número do contato que deseja editar: "))
        if escolha < 1 or escolha > len(contato):
            print("Opção inválida!")
            return
        
        nome_contato = list(contato.keys())[escolha - 1]
        print(f"Editando o contato: {nome_contato}")
        
        telefone = input(f"Digite o novo telefone para {nome_contato} (atual: {contato[nome_contato]['telefone']}): ")
        email = input(f"Digite o novo email para {nome_contato} (atual: {contato[nome_contato]['email']}): ")
        favorito = input(f"O contato {nome_contato} é favorito? (sim/nao) (atual: {'sim' if contato[nome_contato]['favorito'] else 'nao'}): ").strip().lower()
        favorito_verificacao = True if favorito == "sim" else False
        
        contato[nome_contato] = {
            "telefone": telefone,
            "email": email,
            "favorito": favorito_verificacao
        }
        
        print("Contato atualizado com sucesso!")

    except ValueError:
        print("Opção inválida! Por favor, insira um número válido.") 

def editar_favorito():
    if not contato:
        print("Nenhum contato disponível para favoritar.")
        return

    print("\nLista de contatos disponíveis para favoritar:")
    for i, nome in enumerate(contato, 1):
        print(f"{i}. {nome} {'(Favorito)' if contato[nome]['favorito'] else ''}")

    try:
        escolha = int(input("Digite o número do contato que deseja salvar como favorito: ")) - 1
        if escolha < 0 or escolha >= len(contato):
            print("Opção inválida!")
            return

        nome_contato = list(contato.keys())[escolha]
        contato[nome_contato]["favorito"] = True
        print(f"{nome_contato} agora é um contato favorito!")

    except ValueError:
        print("Entrada inválida! Digite um número válido.")

def remover_dos_favoritos():
    favoritos = [nome for nome, dados in contato.items() if dados["favorito"]]

    if not favoritos:
        print("Nenhum contato favorito encontrado.")
        return

    print("\nLista de contatos favoritos:")
    for i, nome in enumerate(favoritos, 1):
        print(f"{i}. {nome}")

    try:
        escolha = int(input("Digite o número do contato que deseja remover dos favoritos: ")) - 1
        if escolha < 0 or escolha >= len(favoritos):
            print("Opção inválida!")
            return

        nome_contato = favoritos[escolha]
        contato[nome_contato]["favorito"] = False
        print(f"{nome_contato} foi removido da lista de favoritos.")

    except ValueError:
        print("Entrada inválida! Digite um número válido.")

def apagando_contato():
    if not contato:
        print("Nenhum contato disponível para apagar.")
        return

    print("\nLista de contatos para remoção:")
    for i, nome in enumerate(contato, 1):
        print(f"{i}. {nome}")

    try:
        escolha = int(input("Digite o número do contato que deseja apagar: ")) - 1
        if escolha < 0 or escolha >= len(contato):
            print("Opção inválida!")
            return

        nome_contato = list(contato.keys())[escolha]
        del contato[nome_contato]
        print(f"O contato {nome_contato} foi apagado com sucesso!")

    except ValueError:
        print("Entrada inválida! Digite um número válido.")

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
    
    escolha = input("Digite a opção desejada: ")
    
    if escolha == "1":
        adicionar_contato()
    elif escolha == "2":
        exibir_contato()
    elif escolha =="3":
        editar_contato()
    elif escolha =="4":
        editar_favorito()
    elif escolha == "5":
        remover_dos_favoritos()
    elif escolha =="6":
        apagando_contato()
    elif escolha == "7":
        print("Aplicação encerrada")
        break

    

