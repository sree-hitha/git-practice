tasks = [] 
 
def add_task(name): 
    tasks.append(name) 
 
def list_tasks(): 
    for i, t in enumerate(tasks, 1): 
        print(f"{i}. {t}") 
 
if __name__ == "__main__": 
    add_task("Learn Git") 
    list_tasks() 
    print("Hello from feature branch") 
# remove task feature 
# priority feature 
# new code 
