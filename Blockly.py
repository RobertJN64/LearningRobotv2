import warnings
import multiprocessing
import json

#for custom blockly
import random
import math
from numbers import Number
from time import sleep

#region CleanHTML
with open("replacements.txt") as f:
    l = f.readlines()

reps = []
for li in l:
    reps.append([li[0],li[2:5]])

def cleanHTML(string):
    for rep in reps:
        string = string.replace(rep[1], rep[0])
    return string
#endregion
#region config
config = {}
def load_config():
    global config
    with open("config.json") as file:
        config = json.load(file)
load_config()

def restore_config():
    global config
    with open("config_orig.json") as file:
        config = json.load(file)
    with open("config.json", "w+") as file:
        json.dump(config, file)

def setconfig(key, value):
    global config
    config[key] = value
    with open("config.json", "w+") as file:
        json.dump(config, file)

def configUI(reqtype, reqdir):
    global config
    if reqtype == "forward":
        if reqdir == 1:
            config["lmotor_speed"] += 1
            config["rmotor_speed"] -= 1
        elif reqdir == -1:
            config["lmotor_speed"] -= 1
            config["rmotor_speed"] += 1
    else:
        if reqdir == 1:
            config["turn_time"] += 0.02
        elif reqdir == -1:
            config["turn_time"] -= 0.02

    config["rmotor_speed"] = round(config["rmotor_speed"])
    config["lmotor_speed"] = round(config["lmotor_speed"])
    config["turn_time"] = round(config["turn_time"], 2)

    with open("config.json", "w+") as file:
        json.dump(config, file)
#endregion


def start_action_thread(reqtype):
    global config
    from robot import Robot
    nokill = {"kill": False}
    r = Robot(nokill, config)
    if reqtype == "forward":
        r.moveFD(10)
    else:
        r.left(90)
    sleep(0.25)
    r.stop() #technically unecessary, but why not

robot = None
def code_executor(code, killflag):
    from robot import Robot, KillFlagException
    global config
    global robot #makes function definitions easier because it forces robot into global scope
    killflag["kill"] = False
    robot = Robot(killflag, config)
    print("++++EXEC++++")
    try:
        exec(code)
    except KillFlagException:
        pass
    finally:
        robot.stop()
    print("----EXEC----")

t = None
def runCode(request, killflag):
    global t
    killflag["kill"] = True

    if t is not None:
        t.join()

    data = request.get_data()
    data = data.decode('utf-8')
    code = str(data.strip('code=').replace('%0A', "\n").replace('%2520', ' '))
    code = cleanHTML(code)

    lines = code.split('\n')
    for i in range(0, len(lines)):
        if "import sys" in lines[i]:
            warnings.warn("Importing sys is banned.")
        if "import" in lines[i]:
            lines[i] = ""

    code = '\n'.join(lines)
    print("++++CODE++++")
    print(code.strip())
    print("----CODE----\n")

    #region add stop cmds
    stopcmds = []
    for i in range(len(lines) - 1, -1, -1):
        line = lines[i]
        if line == "":
            stopcmds.append("")
        else:
            index = 0
            for index, char in enumerate(line):
                if char != " ":
                    break
            stopcmds.append(" " * index + "robot.checkFlag()")

    stopcmds.reverse()
    code = []
    for i in range(0, len(lines)):
        code.append(stopcmds[i])
        code.append(lines[i])
    #endregion

    for i in range(0, len(code)):
        if code[i][0:3] == "def":
            index = 0
            for index, char in enumerate(code[i+1]):
                if char != " ":
                    break
            code[i] = code[i] + "\n" + " " * index + "global robot\n"

    code = '\n'.join(code)

    t = multiprocessing.Process(target=code_executor, args=(code,killflag,))
    t.start()

def runALlCMDS():
    #so import isn't mad at us

    #more import junk
    x = random.randint(0,1)
    math.floor(x)
    Number()
