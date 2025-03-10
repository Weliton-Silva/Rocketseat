def adicionar_tarefas(tarefas,nome_tarefas):
    
# tarefa: nome da tarefa
# completanda: indicar se essa tarefa ja foi completada ou nao

    tarefa = {"tarefa": nome_tarefas, "completada": False}
    tarefas.append(tarefa)
    print(f'Tarefa {nome_tarefas} foi adicionada com sucesso !')
    return

def ver_tarefas(tarefas):
    print("\nLista de tarefas:")
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✓" if  tarefa["completada"] else " "
        nome_tarefa = tarefa["tarefa"]
        print(f"{indice}. [{status}] {nome_tarefa}")
    return

def atualizar_nome_tarefa(tarefas,indice_tarefa, novo_nome_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) -1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len (tarefas):
        tarefas[indice_tarefa_ajustado]["tarefa"] = novo_nome_tarefa
        print(f"Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa}")
    else:
        print("Indice de tarefa inválido.")
    return


tarefas = []
while True:
    print("\n Menu de Gerenciador de Lista de tarefa")
    print("1. Adicionar tarefa")
    print("2. Ver Tarefa")
    print("3. Atualizar Tarefa")
    print("4. Completar Tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        nome_tarefas = input("Digite o nome da tarefa que deseja adicionar: ")
        adicionar_tarefas(tarefas,nome_tarefas)
    elif escolha == "2":
        ver_tarefas(tarefas)
    elif escolha == "3":
        ver_tarefas(tarefas)
        indice_tarefa = input("Digite o número da tarefa que deseja atualizar: ")
        novo_nome = input("Digite o novo nome da tarefa: ")
        atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome)
    elif escolha == "6":
        break

print("Programa finalizado.")