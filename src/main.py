def show_list(filename): # Show tasks in file
    with open(filename, 'r', encoding='utf-8') as tasklist:
        index = 1 # Keep track of current line
        print("Your tasks are: ")
        for task in tasklist:
            print(f'{index}. {task}', end='') # Print task with index
            index += 1
        print()

def add_task(filename, task): # Add new tasks at bottom in file
    with open(filename, 'a', encoding='utf-8') as tasklist:
        # Add newline at end to ensure next added task is on separate line
        tasklist.write(f'{task}\n')

def delete_task(filename, pos): # Delete task from file
    newlist = ''
    with open(filename, 'r', encoding='utf-8') as tasklist:
        index = 1
        for task in tasklist:
            if index != pos:
                # Add everything except mentioned task to an empty string
                newlist += task
            index += 1
    with open(str(filename), 'w', encoding='utf-8') as tasklist:
        tasklist.write(newlist) # Overwrite original file with string

filename = 'tasks'

while True:
    show_list(filename)
    cmd = input('Input a task/command: ')
    if cmd == 'end': break # Way to terminate program
    # Process 'did X' command to delete tasks
    elif cmd[:4] == 'did ': delete_task(filename, int(cmd[4:]))
    else: add_task(filename, cmd)