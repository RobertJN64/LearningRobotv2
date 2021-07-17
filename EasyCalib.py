import flask
from flask import render_template as render_template, request as request
from robot import Robot
import multiprocessing as mp
import json


app = flask.Flask(__name__)
nokill = {"kill": False}

config = {}
def load_config():
    global config
    with open("config.json") as file:
        config = json.load(file)
load_config()

def start_action_thread(reqtype):
    robot = Robot(nokill, config)
    if reqtype == "forward":
        robot.moveFD(10)
    else:
        robot.left(90)
    robot.stop() #technically unecessary, but why not


@app.route('/')
def index():
    return render_template("CalibrationPage.html")

@app.route('/calib_action')
def custom_calib_req():
    if 'type' not in request.args:
        return "Type arg missing."
    reqtype = request.args['type']

    if reqtype not in ["forward", "turn"]:
        return "Type not valid. Try forward / turn"

    else:
        p = mp.Process(target=start_action_thread, args=(reqtype,))
        p.start()
        return "200 ok"

@app.route('/calib_response')
def handle_change_calib():
    if ('type' not in request.args) or ('dir' not in request.args):
        return "Missing type or dir"

    reqtype = request.args['type']
    if reqtype not in ["forward", "turn"]:
        return "Type not valid. Try forward / turn"

    reqdir = request.args['dir']
    try:
        reqdir = int(reqdir)
    except ValueError:
        return "Requestion direction is not int"

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

    return "200 ok"


def startFlask():
    app.run()