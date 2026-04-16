#This is some very simple and stupid stuff
import argparse
tasks = []
#Commands
parse = argparse.ArgumentParser()
parse.add_argument("--add", type=str)
parse.add_argument("--remove", type=str)
args = parse.parse_args()
#Write change to file
def write_tasks_file():
    with open("notes.txt", "a") as file:
        for i in tasks:    
            file.write(f"\n{i}")
#Append tasks
def append_task():
    tasks.append(args.add)

if args.add:
    append_task()
write_tasks_file()
