
import json
from colorama import Fore, Style, init

init(autoreset=True)  # This line will automatically reset the color to its original after each print statement

start_question = "What would you like to do? (add/remove/edit/quit): "
add_question = Fore.CYAN + "What would you like to add? "
remove_question = Fore.RED + "What would you like to remove? "
quit_question = "Are you sure you want to quit? (y/n): "
quit_message = "Goodbye!"
question = ""
tasks = []

help_message = Fore.YELLOW + """
Welcome to the Todo List App!
Type 'quit' at any time to exit.
Type 'list' at any time to see your list.
Type 'help' at any time to see this message again.
""" + Fore.RESET

def get_option():
    print("┌────────────────┐")
    print("│" + Fore.CYAN + " 1. Add         " + Fore.RESET + "│")
    print("│" + Fore.GREEN + " 2. Remove      " + Fore.RESET + "│")
    print("│" + Fore.YELLOW + " 3. Edit        " + Fore.RESET + "│")
    print("│" + Fore.RED + " 4. Quit        " + Fore.RESET + "│")
    print("│" + Fore.BLUE + " 5. List        " + Fore.RESET + "│")
    print("└────────────────┘")
    option = input("Please choose an option (1-5): ")
    return option


def verify_option(option, json_loaded):
    with open('../data/tasks.json', 'r') as f:
        list = json.load(f)
        
    if option == "1":
        data = input(add_question)
        add_to_do(data, json_loaded)
    elif option == "2":
        delete_task(json_loaded)
        pass
    elif option == "3":
        edit_todo(json_loaded)
        pass
    elif option == "4":
        # You can add your quit mechanism here
        print(quit_message)
        exit()
    elif option == "5":
        list_tasks(list)
    else:
        print("Invalid option, please try again.")

def edit_todo(json_loaded):
    
    id = display_options(json_loaded)
    
    is_tast_editable = does_task_exist(json_loaded, id)
    
    if(is_tast_editable):
        update_task(json_loaded, id)
    

def ask_what_to_edit():
    print(Fore.CYAN + "1. Edit Task")
    print(Fore.CYAN + "2. Edit Status")
    
    user_response = input("Coose an option (1 or 2): ")
    
    return user_response


def update_task(json_loaded, id):
    
    chosen = ask_what_to_edit()
    
    chosen_key = ""
    
    if(chosen == "1" ):
        chosen_key = "task"
    else:
        chosen_key = "status"
    
    tasks = json_loaded['tasks']

    for task in tasks:
        if task["id"] == int(id):
            updated_value = input("Please enter your updated value: ")
            task[chosen_key] = updated_value

    updated_key_value = json.dumps(json_loaded, indent=2)
    
    with open('../data/tasks.json', 'w', encoding='utf-8') as file:
        file.write(updated_key_value)


def display_options(json_loaded):
    tasks = json_loaded['tasks']
    
    for task in tasks:
        print(f'{task["id"]}. {Fore.YELLOW}{task["task"]}{Fore.RESET}')

    id = input("Choose a number: ")
    
    return id

def does_task_exist(json_loaded, id): 
    tasks = json_loaded["tasks"]
    for task in tasks:
        if task["id"] == int(id):
            return True
    return False

def update_task_ids(json_loaded):
    tasks = json_loaded["tasks"]
    for i, task in enumerate(tasks, start=1):
        task["id"] = i

    with open('../data/tasks.json', 'w', encoding='utf-8') as file: 
        file.write(json.dumps(json_loaded, indent=2))


def delete_task(json_loaded):
    print(remove_question)
    
    id = display_options(json_loaded)

    does_exist = does_task_exist(json_loaded, id)

    if(does_exist): 

        remove_from_list(json_loaded, id)

    else:

        return print("Choose again, invalid option!")
    

def remove_from_list(json_loaded, id): 
    
    tasks = json_loaded["tasks"]

    task_name = ""
    
    for index, task in enumerate(tasks):
        if task["id"] == int(id):
            task_name = task["task"]
            tasks.pop(index)
            
    
    with open('../data/tasks.json', 'w', encoding='utf-8') as file: 
        file.write(json.dumps(json_loaded, indent=2))

    print(Fore.MAGENTA + "Success, deleted task! : ", task_name)

    update_task_ids(json_loaded)



def add_to_do(todo, json_loaded):

    print("adding to do :", todo)

    # Determine the next task ID by finding the maximum current ID and adding 1.
    # If there are no tasks yet, the ID will be 1.
    if json_loaded["tasks"]:
        next_id = max(task["id"] for task in json_loaded["tasks"]) + 1
    else:
        next_id = 1

    new_task = {
        "id": next_id,
        "task": todo,
        "status": "new"
    }

    json_loaded["tasks"].append(new_task)

    added_todo_task = json.dumps(json_loaded, indent=2)

    with open('../data/tasks.json', 'w', encoding='utf-8') as file:
        file.write(added_todo_task)

def list_tasks(json_loaded):
    print("Here are your tasks:")
    for task in json_loaded['tasks']:
        # print(f'{task["id"]}. {task["task"]}')
        # print with color
        print(f'{task["id"]}. {Fore.GREEN}{task["task"]}{Fore.RESET} - {Fore.MAGENTA}{task["status"]}{Fore.RESET}')
        
    start()

def help():
    print(help_message)
    start()


def start():
    print(help_message)
    
    with open('../data/tasks.json', 'r') as f:
        data = json.load(f)
        all_tasks = data["tasks"]
        word_type = ""
        if(len(all_tasks) == 1 ):
            word_type = "task!"
        elif(len(all_tasks) == 0 ):
            word_type = "tasks"
        else :
            word_type = "tasks!"

        print('You have', len(all_tasks),  word_type, '\n')
        for task in all_tasks: 
            print(f'{task["id"]}. {Fore.GREEN}{task["task"]}{Fore.RESET} - {Fore.MAGENTA}{task["status"]}{Fore.RESET}')
            
        while True:  
            option = get_option()
            
            if option.lower() == 'quit':
                print(quit_message)
                break
            elif option.lower() == 'list':
                list_tasks(data)
            elif option.lower() == 'help':
                help()
            else:
                verify_option(option, data)
    

start()
