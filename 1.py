class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if task:  
            self.tasks.append(task)
            print(f"Task '{task}' added to list.")
        else:
            print("Empty task.")

    def remove_task(self, task_num):
        if 0 < task_num <= len(self.tasks):
           
            task_removed = self.tasks.pop(task_num - 1)
            print(f"Task '{task_removed}' removed from the list.")
        else:
            print(f"{task_num} Try valid task number.")

    def view_tasks(self):
  
        if not self.tasks:
            print("to-do list is empty.")
        else:
            print("to-do list:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")
    
def run_todo():
    todo_list = ToDoList()  

    while True:
        print("\nOptions:")
        print("1 - Add a task")
        print("2 - Remove a task")
        print("3 - View all tasks")
        print("4 - Exit")

        choice = input("Choose an option (1/2/3/4): ").strip()

        if choice == '1':  
            task = input("Enter the task: ").strip()
            todo_list.add_task(task)
        elif choice == '2': 
            todo_list.view_tasks() 
            try:
                task_num = int(input("Enter the task number to remove: ").strip())
                todo_list.remove_task(task_num)
            except ValueError:  
                print("not a number, Please enter a valid task number.")
        elif choice == '3': 
            todo_list.view_tasks()
        elif choice == '4': 
            print("Hope you completed your tasks")
            break
        else:
          
            print("not a valid option. Please choose 1, 2, 3, or 4.")
run_todo()
