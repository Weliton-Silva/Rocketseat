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
    elif escolha == "6":
        break

print("Programa finalizado.")