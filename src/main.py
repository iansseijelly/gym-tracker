import datetime
import argparse
import os

# initialize parser
def parser_init():
    parser = argparse.ArgumentParser()
    parser.add_argument("task", help="task to be executed")
    parser.add_argument("kwargs", help="kwargs for the task", nargs="*")
    return parser

def check_num_kwargs(kwargs, num):
    if len(kwargs) != num:
        exception = "task requires " + str(num) + " kwargs"
        raise Exception(exception)
    else:
        return True

def select_task(task, kwargs):
    print("selecting tasks here")
    if task == "init" and check_num_kwargs(kwargs, 0):
        print("init")
        init(kwargs)
    elif task == "w" and check_num_kwargs(kwargs, 3):
        add_workout(kwargs)
    elif task == "d":
        add_diet(kwargs)
    else:
        raise Exception("task not found")

# initialize project
def get_common_paths():
    global src_dir, root_dir, data_dir, log_dir, diets_path, workouts_path
    src_dir = os.path.dirname(os.path.realpath(__file__))
    root_dir = os.path.dirname(src_dir)
    data_dir = os.path.join(root_dir, "data")
    log_dir = os.path.join(root_dir, "log")
    diets_path = os.path.join(data_dir, "diets.csv") 
    workouts_path = os.path.join(data_dir, "workouts.csv")  

def init(kwargs):
    pass

def add_workout(kwargs):
    name = kwargs[0]
    duration = kwargs[1]
    calories = kwargs[2]
    date = datetime.date.today()
    time = datetime.datetime.now().time()
    with open(workouts_path, "a") as f:
        f.write("{},{},{},{},{}\n".format(name, duration, calories, date, time))

def add_diet(kwargs):
    name = kwargs[0]
    category = kwargs[1]
    calories = kwargs[2]
    date = datetime.date.today()
    time = datetime.datetime.now().time()
    with open(diets_path, "a") as f:
        f.write("{},{},{},{},{}\n".format(name, category, calories, date, time))

if __name__ == "__main__":
    parser = parser_init()
    args = parser.parse_args()
    task = args.task
    kwargs = args.kwargs
    get_common_paths()
    select_task(task, kwargs)
