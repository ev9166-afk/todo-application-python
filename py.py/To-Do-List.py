tasks = []

print("Welcome to the Todo List Application!")

while True:
    print("\nMenu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")

    choice = input("Choose an option 1-4: ")

    try:
        if choice == "1":
            task = input("Enter a task: ")

            if task.strip() == "":
                raise ValueError("Task cannot be empty.")

            tasks.append(task)
            print("Task added successfully!")

        elif choice == "2":
            if len(tasks) == 0:
                print("There are no tasks to view.")
            else:
                print("\nYour Tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")

        elif choice == "3":
            if len(tasks) == 0:
                print("There are no tasks to delete.")
            else:
                print("\nYour Tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")

                task_number = int(input("Enter the task number to delete: "))

                if task_number < 1 or task_number > len(tasks):
                    raise IndexError("That task does not exist.")

                deleted_task = tasks.pop(task_number - 1)
                print(f"Deleted task: {deleted_task}")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            raise ValueError("That menu option does not exist.")

    except ValueError as error:
        print(f"Invalid input: {error}")

    except IndexError as error:
        print(f"input not accepted: {error}")

    else:
        print("Action completed.")

    finally:
        print("Returning to menu...")