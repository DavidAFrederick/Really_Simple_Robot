import wpilib
import wpilib.drive
from commands2 import Command
from drivetrain_subsystem import DriveTrain
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class DriveShortDistanceSpeed(Command):
    def __init__(self, drivetrain: DriveTrain, speed : float, time : float):
        self.drivetrain = drivetrain
        self.speed = speed 
        self.time = time
        self.addRequirements(self.drivetrain)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    def initialize(self):
        self.timer = wpilib.Timer()
        self.timer.start()
   
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    def execute(self):
        self.drivetrain.drive_teleop(0.0, self.speed)
        print ("Speed")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    def isFinished(self) -> bool:
        if self.timer.get() < self.time:
            return False
        else:
            return True
    def end(self, interrupted: bool):
        self.drivetrain.drive_teleop(0,0)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -









