# Programa: Gerenciador de Tarefas Simples

tarefas = []

# Função que mostra o menu na tela
def show_menu():
    print("\n=== GERENCIADOR DE TAREFAS ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("4 - Concluir tarefa")
    print("5 - Sair")
# Função para adicionar uma nova tarefa
def add_tarefa():
    task = input("Digite a nova tarefa: ")# usuário digita a tarefa
    # adiciona na lista com status "não concluída"
    tasks.append({"descricao": task, "concluida": False})
    print("Tarefa adicionada com sucesso!")
# Função para listar todas as tarefas
def list_tarefas():
     # verifica se a lista está vazia
    if not tasks:
        print("Nenhuma tarefa cadastrada.")
        return
    print("\nLista de tarefas:")

     # percorre todas as tarefas usando um laço
    for i, tarefa in enumerate(tarefas):
        # verifica se a tarefa foi concluída
        status = "✔" if tarefa["concluida"] else "✘"
        
        print(f"{i + 1}. [{status}] {tarefa['descricao']}")
    # Função para remover uma tarefa  
def remove_tarefa():
    list_tarefas()# mostra as tarefas antes de remover
    try:
         # usuário escolhe o número da tarefa
        index = int(input("Digite o número da tarefa para remover: ")) - 1
         # verifica se o número é válido
        if 0 <= index < len(tarefas):
            removed = tarefas.pop(index)# remove da lista
            print(f"Tarefa '{removed['descricao']}' removida.")
        else:
            print("Número inválido.")
           
            # trata erro caso usuário digite algo que não é número
    except ValueError:
        print("Entrada inválida.")

# Função para marcar tarefa como concluída
def complete_tarefa():
    list_tarefas()
    try:
        index = int(input("Digite o número da tarefa para concluir: ")) - 1
        if 0 <= index < len(tarefas):
            tarefas[index]["concluida"] = True
            print("Tarefa marcada como concluída!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

# Loop principal do programa
while True:
    show_menu()
    choice = input("Escolha uma opção: ")

    if choice == "1":
        add_tarefa()
    elif choice == "2":
        list_tarefa()
    elif choice == "3":
        remove_tarefa()
    elif choice == "4":
        complete_tarefa()
    elif choice == "5":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
