import time
import explorerhat as eh

class KillFlagException(Exception):
    pass


class Robot:
    def __init__(self, killflag, config):
        self.killflag = killflag
        self.lmotor_speed = config['lmotor_speed'] * config['lmotor_inverse']
        self.rmotor_speed = config['rmotor_speed'] * config['rmotor_inverse']
        self.linv = config["lmotor_inverse"]
        self.rinv = config["rmotor_inverse"]
        self.lmotor_time = config['lmotor_time'] / 10
        self.rmotor_time = config['rmotor_time'] / 10
        self.motor_time = (self.lmotor_time + self.rmotor_time) / 2
        self.turn_time = config['turn_time']

    def moveFD(self, dis):
        print("[MOVE CMD] Move fd command called with: " + str(dis))
        if dis > 0:
            direction = 1
        else:
            direction = -1
        eh.motor.one.speed(self.lmotor_speed * direction)
        eh.motor.two.speed(self.rmotor_speed * direction)
        self.wait(self.motor_time * abs(dis))
        eh.motor.stop()
        eh.motor.one.stop()
        eh.motor.two.stop()
        self.wait(0.1)
        

    def left(self, deg):
        print("[MOVE CMD] Left command called with: " + str(deg))
        eh.motor.one.speed(self.lmotor_speed * -1)
        eh.motor.two.speed(self.rmotor_speed)
        self.wait(self.turn_time * (float(deg)/90))
        eh.motor.stop()
        eh.motor.one.stop()
        eh.motor.two.stop()
        self.wait(0.1)
        

    def right(self, deg):
        print("[MOVE CMD] Right command called with: " + str(deg))
        eh.motor.one.speed(self.lmotor_speed)
        eh.motor.two.speed(self.rmotor_speed * -1)
        self.wait(self.turn_time * (float(deg)/90))
        eh.motor.stop()
        eh.motor.one.stop()
        eh.motor.two.stop()
        self.wait(0.1)
        

    def runMotors(self, lm, rm):
        print("[MOVE CMD] Set motor speeds. LM:", lm, "RM:", rm)
        if lm == 0 and rm == 0:
            eh.motor.stop()
            eh.motor.one.stop()
            eh.motor.two.stop()
            self.wait(0.1)
        else:
            eh.motor.one.speed(lm * self.linv)
            eh.motor.two.speed(rm * self.rinv)
        

    def checkFlag(self):
        if self.killflag["kill"]:
            raise KillFlagException("Kill Flag Triggered")

    def wait(self, duration):
        starttime = time.time()
        while time.time() - starttime < duration:
            time.sleep(0.01)
            self.checkFlag()

    def stop(self):
        eh.motor.stop()
        eh.motor.one.stop()
        eh.motor.two.stop()
        time.sleep(0.1)
        if self.killflag["kill"]:
            print("Kill flag activated. Robot stopped.")
        else:
            print("Code execution finished. Robot stopped.")
