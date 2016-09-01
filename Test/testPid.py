from PyPID import PIDController
pid = PIDController()
pid.printMil()
pid.printTunings()
pid.setTunings(1,4,6)
pid.printTunings()
print "test"
