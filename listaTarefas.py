import datetime

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False
        self.created_at = datetime.datetime.now()
    
    def mark_as_completed(self):
        self.completed = True
    
    def edit(self, new_description):
        self.description = new_description
    
    def __str__(self):
        status = "Concluída" if self.completed else "Pendente"
        return f"{self.description} - {status} (Criada em: {self.created_at.strftime('%Y-%m-%d %H:%M')})"

class TaskList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
    
    def list_tasks(self, filter_by=None):
        filtered_tasks = self.tasks
        if filter_by == "completed":
            filtered_tasks = [task for task in self.tasks if task.completed]
        elif filter_by == "pending":
            filtered_tasks = [task for task in self.tasks if not task.completed]
        
        if not filtered_tasks:
            print("Nenhuma tarefa encontrada.")
            return
        
        for idx, task in enumerate(filtered_tasks, 1):
            print(f"{idx}. {task}")
    
    def mark_task_as_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_completed()
            print("Tarefa marcada como concluída.")
        else:
            print("Índice de tarefa inválido.")
    
    def edit_task(self, index, new_description):
        if 0 <= index < len(self.tasks):
            self.tasks[index].edit(new_description)
            print("Tarefa editada com sucesso.")
        else:
            print("Índice de tarefa inválido.")
    
    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Tarefa '{removed_task.description}' removida.")
        else:
            print("Índice de tarefa inválido.")

def main():
    task_list = TaskList()
    
    while True:
        print("\nAplicativo de Lista de Tarefas")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Editar Tarefa")
        print("5. Remover Tarefa")
        print("6. Filtrar Tarefas (1 - Pendentes / 2 - Concluídas)")
        print("0. Sair")
        
        choice = input("Escolha uma opção: ")
        
        if choice == "1":
            description = input("Digite a descrição da tarefa: ")
            task_list.add_task(description)
            print("Tarefa adicionada.")
        
        elif choice == "2":
            print("\nTarefas:")
            task_list.list_tasks()
        
        elif choice == "3":
            task_list.list_tasks()
            index = int(input("Digite o número da tarefa para marcar como concluída: ")) - 1
            task_list.mark_task_as_completed(index)
        
        elif choice == "4":
            task_list.list_tasks()
            index = int(input("Digite o número da tarefa para editar: ")) - 1
            new_description = input("Digite a nova descrição da tarefa: ")
            task_list.edit_task(index, new_description)
        
        elif choice == "5":
            task_list.list_tasks()
            index = int(input("Digite o número da tarefa para remover: ")) - 1
            task_list.remove_task(index)
        
        elif choice == "6":
            filter_option = input("Digite '1' para ver tarefas Pendentes ou '2' para Concluídas: ")
            if filter_option == "1":
                task_list.list_tasks("pending")
            elif filter_option == "2":
                task_list.list_tasks("completed")
            else:
                print("Opção de filtro inválida.")
        
        elif choice == "0":
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
