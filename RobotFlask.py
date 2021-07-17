import flask
from flask import request, jsonify, render_template
from os import getcwd
import multiprocessing
import PythonExecutor
#import json

UPLOAD_FOLDER = getcwd() + '/userscripts/'

app = flask.Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


killflag = {"kill": False}
process: multiprocessing.Process = None
lastTB = []
blocklyActive = False

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
    import Blockly
    global blocklyActive
    blocklyActive = True
    Blockly.runCode(request, killflag)
    return jsonify(success=True)

@app.route('/reloadconfig')
def reloadconfig():
    import Blockly
    Blockly.load_config()
    return "Config reloaded"

@app.route('/restoreconfig')
def restoreconfig():
    import Blockly
    Blockly.restore_config()
    return "Config restored to default"

@app.route('/config')
def viewconfig():
    import Blockly
    return jsonify(Blockly.config)


@app.route('/changeconfig')
def changeconfig():
    import Blockly
    if 'value' in request.args and 'key' in request.args:
        Blockly.setconfig(str(request.args['key']), float(request.args['value']))
        return "Key updated with value."
    else:
        return "Error. Missing value or key."

#endregion

#region calib
@app.route('/calibrate')
def calibrateUI():
    return render_template("CalibrationPage.html")

@app.route('/calib_action')
def custom_calib_req():
    import Blockly
    #nokill = {"kill": False}
    if 'type' not in request.args:
        return "Type arg missing."
    reqtype = request.args['type']

    if reqtype not in ["forward", "turn"]:
        return "Type not valid. Try forward / turn"

    else:
        p = multiprocessing.Process(target=Blockly.start_action_thread, args=(reqtype,))
        p.start()
        return "200 ok"

@app.route('/calib_response')
def handle_change_calib():
    import Blockly
    if ('type' not in request.args) or ('dir' not in request.args):
        return "Missing type or dir"

    reqtype = request.args['type']
    if reqtype not in ["forward", "turn"]:
        return "Type not valid. Try forward / turn"

    reqdir = request.args['dir']
    try:
        reqdir = int(reqdir)
    except ValueError:
        return "Request direction is not int"
    Blockly.configUI(reqtype, reqdir)
    return "200 ok"
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
    global blocklyActive
    if len(lastTB) > 0:
        return lastTB.pop(0)
    if blocklyActive:
        return "Blockly was started on the robot. Please reboot to use full functionality."
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
    app.run(host="0.0.0.0", port=80, ssl_context=('cert.pem', 'key.pem'))

