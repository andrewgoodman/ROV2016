import time
class PIDController:
    global millis
    
    def __init__(self):
        global kp,ki,kd,lastTime,SampleTime,Setpoint,Input,lastInput
        kp,ki,kd,lastTime,Setpoint,Input,lastInput =[0,0,0,0,0,0,0]
        SampleTime = 1000
        

    
    millis = lambda: int(round(time.time() * 1000))

    def Compute(self):
        global lastTime
        global lastInput
        now = millis()
        timeChange = now - lastTime
        if timechange >= SampleTime:
      
            error = Setpoint - Input
            errSum += error
            dInput = Input - lastInput
          
            Output = kp * error + ki * errSum + kd * dInput
            return Output
          
            lastInput = Input
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

