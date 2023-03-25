import time


def options():
    print("-- TO-DO LIST APP --")
    print("1. Add a new task")
    print("2. Remove a task")
    print("3. List all tasks")
    print("4. Remove all tasks")
    print("5. Edit a task")
    print("6. Exit")


while True:
    try:
        options()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            number_task = int(input("Enter the number of the task: "))
            with open("todo.txt", "a") as file:
                for tasks in range(number_task):
                    task = input(f"{tasks + 1}. Enter the task: ").lower()

                    while len(task) == 0:
                        print("[!] Enter a valid task!")
                        task = input(f"{tasks + 1}. Enter the task: ").lower()

                    file.write(task + "\n")

                time.sleep(1)
                print("[+] Tasks added\n")

        elif choice == 2:
            with open("todo.txt", "r") as file:
                info = file.read()
                print(info)
                remove_task = input("Enter the task to remove: ").lower()

                if remove_task in info:
                    info = info.replace(remove_task, "")

                    with open("todo.txt", "w") as file:
                        file.write(info)

                    print("[-] Task removed\n")
                else:
                    print("[!] Task not found\n")

        elif choice == 3:
            with open("todo.txt", "r") as file:
                info = file.read()
                print(info)

        elif choice == 4:
            with open("todo.txt", "w") as file:
                file.write("")

            print("[-] All tasks removed\n")

        elif choice == 5:
            with open("todo.txt", "r") as file:
                info = file.read()
                print(info)
                edit_task = input("Enter the task to edit: ").lower()

                if edit_task in info:
                    edited_task = input("Enter the new task: ").lower()
                    info = info.replace(edit_task, edited_task)

                    with open("todo.txt", "w") as file:
                        file.write(info)

                    print("[+] Task edited\n")
                else:
                    print("[!] Task not found\n")

        else:
            break

    except ValueError:
        print("[!] Please enter a valid value\n")
