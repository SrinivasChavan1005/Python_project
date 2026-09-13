tasks={}
while True:
    user_choice=input("Enter choice : ")
    if user_choice=="Add Task":
        new_task=input("Enter new task: ")
        tasks.update({new_task:"pending"})
    elif user_choice=="View Task":
        if not tasks:
            print("No tasks available.")
        else:
            for i,(key,value) in enumerate(tasks.items(),start=1):
                print(f"{i}. {key}->{value}")
    elif user_choice=="delete Task":
        remove_task=input("Enter task to be deleted: ")
        tasks.pop(remove_task)
    elif user_choice=="Complete Task":
        completed=input("Enter the task completed: ")
        if not tasks:
            print("Not valid")
        else:
            tasks[completed]="Completed"
    elif user_choice=="Exit":
        break
    else:
        print("Invalid Choice Please Try Again : ")
      
