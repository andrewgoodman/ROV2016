import time
class PIDController:
    global millis
    
    def __init__(self):
        global isRunning,kp,ki,kd,lastTime,SampleTime,Setpoint,Input,lastInput,ITerm,outMin,outMax
        kp,ki,kd,lastTime,Setpoint,Input,lastInput,ITerm,outMin,outMax=[0,0,0,0,0,0,0,0,0,0]
        SampleTime = 1000
        isRunning = True
    
    millis = lambda: int(round(time.time() * 1000))

    def Compute(self):
        global lastTime
        global lastInput
        global ITerm
        if isRunning:
            now = millis()
            timeChange = now - lastTime
            if timechange >= SampleTime:
          
                error = Setpoint - Input
                ITerm += ki*error
                if ITerm>outMax:
                    ITerm = outMax
                elif ITerm < outMin:
                    ITerm = outMin
                dInput = Input - lastInput
              
                Output = kp * error + ITerm - kd * dInput
                if Output > outMax:
                    Output = outMax
                elif Output < outMin:
                    Output = outMin
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

    def SetOutputLimits(self,Min,Max):
        global outMin,outMax
        if Min < Max:
            outMin = Min
            outMax = Max

    def setMode(self, Mode):
        global isRunning
        isRunning = Mode
        
        






    def printMil(self):
        print(millis())

    def printTunings(self):
        global kp,ki,kd
        print("[%s,%s,%s]" % (kp,ki,kd))

    def printValue(self,value):
        print value

