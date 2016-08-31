import time
class PIDController:
    global millis
    
    def __init__(self):
        global kp,ki,kd
        global lastTime
        global SampleTime
        global Setpoint
        global Input
        Setpoint = 0
        Input = 0
        lastTime = 0
        kp,ki,kd =[0,0,0]
        SampleTime = 1000
        

    
    millis = lambda: int(round(time.time() * 1000))

    def Compute(self):
        global lastTime
        now = millis()
        timeChange = now - lastTime
        if timechange >= SampleTime:
      
            error = Setpoint - Input
            errSum += error
            dErr = error - lastErr
          
            Output = kp * error + ki * errSum + kd * dErr
            return Output
          
            lastErr = error
            lastTime = now
          
    def setTunings(self,Kp,Ki,Kd,inputVar):
        global kp,ki,kd,Input
        Input = inputVar
        SampleTimeInSec = SampleTime/1000
        kp = Kp
        ki = Ki * SampleTimeInSec
        kd = Kd / SampleTimeInSec

    def setSampleTime(newSampleTime):
        global SampleTime
        if newSampleTime > 0:
            ratio = newSampleTime/SampleTime
            ki *= ratio
            kd /= ratio
            SampleTime = newSampleTime

    def setSetpoint(self, setpoint):
        global Setpoint
        Setpoint = setpoint

    def printMil(self):
        print(millis())

    def printTunings(self):
        global kp,ki,kd
        print("[%s,%s,%s]" % (kp,ki,kd))

    def printValue(self,value):
        print value

