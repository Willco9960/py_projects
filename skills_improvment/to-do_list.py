
print(f"[to-do list]")

Tasks = []

while True:
    print(f"What would you like to do?")
    print(f"1) Add a task\n2) View tasks\n3) Remove a task\n4)Exit")
    sel = int(input())

    if sel == 1:
        task = input(f"Whats next on your list? ")
        Tasks.append(task)
        print(f"{task} added successfully")

    elif sel == 2:
       if not Tasks:
           print("Your to-do list is empty")

       else:
            print(f"Here are your tasks:")
            for i, task in enumerate(Tasks, start=1):
                print(f"{i}) {task}")

    elif sel == 3:
        if not Tasks:
            print("Your to-do list is empty")

        else:
            print(f"Here are your tasks:")
            for i, task in enumerate(Tasks, start=1):
                print(f"{i}) {task}")

            try:
                task_num = int(input("Enter the task you would like to remove: "))
                if 1 <= task_num <= len(Tasks):
                    removed_task = Tasks.pop(task_num - 1)
                    print(f"Task removed: {removed_task}")
            except ValueError:
                print("Please enter a valid number.")

    elif sel == 4:
        print("Exiting To-Do List. Goodbye!")
        break

    else:
        print(f"Invalide try again")
