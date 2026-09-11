# To-Do List

# Menu Loop

todo_list = []

# Add task function
def add_task():
    todo_list
    task_input = input("Input Task: ")
    todo_list.append(task_input)
    print(todo_list)

# View task
def view_task():
    print(todo_list)

# Delete task
def delete_task():
    task_remove = input("Input task to delete: ")
    todo_list.remove(task_remove)
    print(todo_list)




# Main function
def main():
   
    while True:
        print("1. Add task(s), 2. View task(s), 3. Delete tasks(s), 4. Quit")

        user_input = (input("Select your option: "))
    

        if user_input == "1":
            print("Add task(s)")
            add_task()
        elif user_input == "2":
            print("View task(s)")
            view_task()
        elif user_input == "3":
            print("Delete tasks(s)")
            delete_task()
        elif user_input == "4":
            print("Back to menu")
            break
        else:
            print ("Please input a number from 1 to 4")

if __name__ == "__main__":
    main() 





