class TaskManager:
    log_file = 'task_log.txt'

    def __init__(self):
        self.tasks = []
        self.initialize()

    def initialize(self):
        with open(self.log_file, 'w') as f:
         f.write('')

    def log(self, message):
        with open(self.log_file, 'a') as f:
            f.write(message + '\n')

    def create_task(self, task):
        self.log(f'Input: Create Task "{task}"')
        if task in self.tasks:
            self.log(f'Output: created "{task}" - unsuccessful (already exists)')
            print("Cannot add pre-existing task")
        else:
            self.tasks.append(task)
            self.log(f'Output: created "{task}" - successful')
            print(f'Task "{task}" created successfully')

    def remove_task(self, task):
        self.log(f'Input: Remove Task "{task}"')
        if task in self.tasks:
            self.tasks.remove(task)
            self.log(f'Output: removed "{task}" - successful')
            print(f'Task "{task}" removed successfully')
        else:
            self.log(f'Output: removed "{task}" - unsuccessful (task not found)')
            print("The task you want to remove does not exist")

    def search_task(self, task):
        self.log(f'Input: Search Task "{task}"')
        if task in self.tasks:
            self.log(f'Output: searched "{task}" - found')
            print(f'Task "{task}" found')
        else:
            self.log(f'Output: searched "{task}" - not found')
            print("Task not found")

    def print_tasks(self):
        self.log('Input: Print All the Tasks')
        if self.tasks:
            self.log('Output: printed tasks - successful')
            for task in self.tasks:
                print(task)
        else:
            self.log('Output: printed tasks - unsuccessful (no tasks present)')
            print("No tasks present")

    def print_log(self):
        self.log('Input: Print Log')
        try:
            with open(self.log_file, 'r') as f:
                 print(f.read())
        except FileNotFoundError:
            self.log('Output: No log file found')
            print("No log file found")

def main():
    tm = TaskManager()

    while True:
        print("\nTask Manager")
        print("1. Create Task")
        print("2. Remove Task")
        print("3. Search Task")
        print("4. Print All Tasks")
        print("5. Print Log")
        print("6. Exit")

        choice = input("Enter your choice: ")
        tm.log(f'Input: User selected choice "{choice}"')

        if choice == '1':
            task = input("Enter task to create: ")
            tm.create_task(task)
        elif choice == '2':
            task = input("Enter task to remove: ")
            tm.remove_task(task)
        elif choice == '3':
            task = input("Enter task to search: ")
            tm.search_task(task)
        elif choice == '4':
            tm.print_tasks()
        elif choice == '5':
            tm.print_log()
        elif choice == '6':
            tm.log('Input: Exit')
            print("Exiting Task Manager")
            break
        else:
            tm.log('Output: Invalid choice')
            print("Invalid choice, please try again")

if __name__ == "__main__":
    main()
