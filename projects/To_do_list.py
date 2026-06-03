#To DO LIST

#An Empty list to store the tasks
task = []

print("----TO DO LIST----")

# Using while loop 
while True:
    print("\nOptions: ")
    print("1.View")
    print("2.Add")
    print("3.Remove")
    print("4.Exit")
    choice = input("Enter your choice(1-4): ")

    if choice == "1":
        print("\nYour task list:")
        if not task:
            print("Your list is empty!!")
        else:
            for index, item in enumerate(task, start=1):
                print(f"{index}.{item}")
    
    elif choice == "2":
        new_task = input("Enter the task: ")
        task.append(new_task)
        print("Task added")
    
    elif choice == "3":
        if not task:
            print("Nothing to remove")
        else:
            for index, item in enumerate(task, start=1):
                print(f"{index}.{item}")
            num = int(input("Enter the task no. to removed: "))
            task.pop(num-1)
            print("Task Removed.")

    elif choice == "4":
        print("GOOD BYE!!")
        break

    else:
        print("Invalid choice!!!")
        print("Please enter correct choice")
