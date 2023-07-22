
import json
start_question = "What would you like to do? (add/remove/quit): "
add_question = "What would you like to add? "
remove_question = "What would you like to remove? "
quit_question = "Are you sure you want to quit? (y/n): "
quit_message = "Goodbye!"
question = ""
tasks = []

def get_option():
    return input()


def add_to_do(todo):
    print("adding to do :", todo)


def verify_option(option):
    if(option == "add"):
        data = input("What is the todo you will be adding? " )
        add_to_do(data)
    # elif(option == "remove"):
    #     remove_todo(data)
        



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
            

    print(start_question)

    option = get_option()

    verify_option(option)

start()
