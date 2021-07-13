import flask
from flask import request, jsonify, render_template
from os import getcwd
import multiprocessing
import Blockly
import PythonExecutor

UPLOAD_FOLDER = getcwd() + '/userscripts/'

app = flask.Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


killflag = {"kill": False}
process: multiprocessing.Process = None
lastTB = []

@app.route('/')
def home():
    return render_template('index.html')

#region Blockly
@app.route('/blockly')
def blockly():
    return render_template('blockly.html')

@app.route('/media/<file>')
def redirect(file):
    return flask.redirect('/static/blockly/media/' + file, 302)

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

@app.route("/stopBlockly")
def stop():
    killflag["kill"] = True
    return jsonify(success=True)

@app.route('/runBlocklyCode', methods = ["POST"])
def runBlocklyCode():
    Blockly.runCode(request, killflag)
    return jsonify(success=True)
#endregion
#region Python
@app.route('/python')
def index():
    return render_template('PythonExecutor.html')

@app.route('/uploadPython', methods=['POST'])
def upload():
    PythonExecutor.upload_file(app, request)
    return "200 OK"

@app.route("/runPython")
def runScript():
    global lastTB
    global process
    manager = multiprocessing.Manager()
    lastTB = manager.list()
    process = multiprocessing.Process(target=PythonExecutor.runUserScript, args=(lastTB,))
    process.start()
    return "Code running."

@app.route("/traceback")
def getTraceback():
    global lastTB
    if len(lastTB) > 0:
        return lastTB.pop(0)
    return ""

@app.route("/prints")
def getPrints():
    with open("userscripts/printlog.txt") as f:
        lines = f.readlines()
    return ''.join(lines)

@app.route("/stopPython")
def stopScript():
    global process
    if process is not None and process.is_alive():
        process.terminate()
        with open("userscripts/printlog.txt", "a") as file:
            file.write("---SCRIPT STOPPED---\n")
    return "Code stopped."
#endregion

def startFlask():
    app.run()