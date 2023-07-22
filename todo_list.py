
import json

start_question = "What would you like to do? (add/remove/edit/quit): "
add_question = "What would you like to add? "
remove_question = "What would you like to remove? "
quit_question = "Are you sure you want to quit? (y/n): "
quit_message = "Goodbye!"
question = ""
tasks = []

def get_option():
    print('\n'"1. Add")
    print("2. Remove")
    print("3. Edit")
    print("4. Quit")
    option = input("Please choose an option (1-4): ")
    return option

def verify_option(option, json_loaded):
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
        pass
    else:
        print("Invalid option, please try again.")

def edit_todo(json_loaded):
    print("edit")
    
    id = display_options(json_loaded)
    
    is_tast_editable = does_task_exist(json_loaded, id)
    
    if(is_tast_editable):
        update_task(json_loaded, id)
    


def update_task(json_loaded, id):
    print(id, "OOp")

def display_options(json_loaded):
    tasks = json_loaded['tasks']
    
    for task in tasks:
        print(f'{task["id"]}. {task["task"]}')

    id = input("Choose a number: ")
    
    return id

def does_task_exist(json_loaded, id): 
    tasks = json_loaded["tasks"]
    for task in tasks:
        if task["id"] == int(id):
            return True
    return False

def delete_task(json_loaded):
    print(remove_question)
    
    id = display_options(json_loaded)

    does_exist = does_task_exist(json_loaded, id)

    if(does_exist): 

        print("Deleting option: ", id)

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

    print("Success, deleted task! : ", task_name)



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



def start():
    print("Welcome to the Todo List App!")
    print("Type 'quit' at any time to exit.")
    print("Type 'list' at any time to see your list.")
    print("Type 'help' at any time to see this message again.")
    print('\n')
    
    if(question == "quit"):
        return
        
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
            print(task['task'])
            

    option = get_option()

    verify_option(option, data)

start()
