user_input = "random"
data=[]
def show_menu():
    print("menu")
    print('1. Add a task')
    print("2. Mark as done")
    print("3. View to-do list")
    print("4. Exit")

while user_input!=4:

    show_menu()
    user_input= input('Enter your choice: ')


    if user_input == "1":
        item=input('What is to be done? ')
        data.append(item)
        print('Added Task', item)
    elif user_input == '2':
        item= input('What is to be marked as done? ')
        if item in data:
            data.remove(item)
            print("Completed Task:", item)
        else:
            print('Task was not added in to-do list')
    elif user_input== "3":
        print('View the to-do list')
    elif user_input == '4':
        print('Good bye')
    else:
        print("Please enter one of 1,2,3 or 4")