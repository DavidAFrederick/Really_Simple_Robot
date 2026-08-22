import wpilib
import wpilib.drive
from commands2 import Command
from drivetrain_subsystem import DriveTrain
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class DriveShortDistance(Command):
    def __init__(self, drivetrain: DriveTrain):
        self.drivetrain = drivetrain
        self.addRequirements(self.drivetrain)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    def initialize(self):
        self.timer = wpilib.Timer()
        self.timer.start()
   
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    def execute(self):
        self.drivetrain.drive_teleop(0.0, 0.9)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    def isFinished(self) -> bool:
        if self.timer.get() < 4.0:
            return False
        else:
            return True
    def end(self, interrupted: bool):
        self.drivetrain.drive_teleop(0,0)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -









