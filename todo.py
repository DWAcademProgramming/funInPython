while True: 
    user_action = input("Type add, show, or exit: ")

    match user_action: 
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            with open('todos.txt', 'r') as file: 
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file: 
                file.writelines(todos)

        case 'show':
            with open('todos.txt', 'w') as file: 
                todos = file.readlines()
                
            for index, item in enumerate(todos): 
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)

        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1

            with open('todos.txt', 'r') as file: 
                todos = file.readlines()
            print('Here are the existing todos ', todos)

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo
            
            with open('todos.txt', 'w') as file: 
                file.writelines(todos)
        case 'complete':
            number = int(input("Number of the todo to complete: "))

            with open('todos.txt', 'r') as file: 
                todos = file.readlines()
            index = number - 1
            todos_to_remove = todos[index].strip('\n')
            todos.pop(number - 1)

            with open('todos.txt', 'w') as file: 
                file.writelines(todos)
            
            message = f"Todo {todos_to_remove} was removed from the list"
        case 'exit': 
            break

print("Bye")