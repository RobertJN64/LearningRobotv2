#TODO - replace all of this code
import time

class KillFlagException(Exception):
    pass


class Robot:
    def __init__(self, killflag):
        self.killflag = killflag

    def moveFD(self, dis):
        print("[MOVE CMD] Move fd command not yet implemented!" + " Called with: " + str(dis))
        self.wait(1)

    def left(self, deg):
        print("[MOVE CMD] Left command not yet implemented." + " Called with: " + str(deg))
        self.wait(1)

    def right(self, deg):
        print("[MOVE CMD] Right command not yet implemented." + " Called with: " + str(deg))
        self.wait(1)

    def runMotors(self, lm, rm):
        print("[MOVE CMD] Set motor speeds. LM:", lm, "RM:", rm)
        self.wait(1)

    def checkFlag(self):
        if self.killflag["kill"]:
            raise KillFlagException("Kill Flag Triggered")

    def wait(self, duration):
        starttime = time.time()
        while time.time() - starttime < duration:
            time.sleep(0.05)
            self.checkFlag()

    def stop(self):
        if self.killflag["kill"]:
            print("Kill flag activated. Robot stopped.")
        else:
            print("Code execution finished. Robot stopped.")
