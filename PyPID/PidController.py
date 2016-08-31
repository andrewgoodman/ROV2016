import time
class PIDController:
    global millis
    
    def __init__(self):
        global kp,ki,kd
        lastTime = 0
        kp,ki,kd =[0,0,0]
        

    
    millis = lambda: int(round(time.time() * 1000))

    def Compute(self):
        global lastTime
        now = millis()
        timeChange = now - lastTime
      
        error = Setpoint - Input;
        errSum += (error * timeChange)
        dErr = (error - lastErr) / timeChange
      
        Output = kp * error + ki * errSum + kd * dErr
        return Output
      
        lastErr = error
        lastTime = now
      
    def setTunings(self,Kp,Ki,Kd):
        global kp,ki,kd
        kp = Kp
        ki = Ki
        kd = Kd

    def printMil(self):
        print(millis())

    def printTunings(self):
        global kp,ki,kd
        print("[%s,%s,%s]" % (kp,ki,kd))

    def printValue(self,value):
        print value

