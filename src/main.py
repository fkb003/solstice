def show_list(filename): # Show tasks in file
    with open(filename, 'r', encoding='utf-8') as tasklist:
        index = 1 # Keep track of current line
        print("Your tasks are: ")
        for task in tasklist:
            print(f'{index}. {task}', end='') # Print task with index
            index += 1
        print()