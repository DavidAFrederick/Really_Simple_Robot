import wpilib
import wpilib.drive
from commands2 import Command
from drivetrain_subsystem import DriveTrain

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class TeleopDrive(Command):
    def __init__(self, drivetrain: DriveTrain, controller: wpilib.Joystick):
        self.drivetrain = drivetrain
        self.controller = controller
        self.addRequirements(self.drivetrain)
        print ("TeleOpDrive Command Instantiated  (Runs one time at command creation) +++++++++++++++++")

  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def initialize(self):
        print ("TeleOpDrive Command Initialized  (Runs one time when command called) ==================")

    def execute(self):
        self.drivetrain.drive_teleop( -self.controller.getRawAxis(0), -self.controller.getRawAxis(1))

    def isFinished(self) -> bool:
        return False
    
    def end(self, interrupted: bool):
        self.drivetrain.drive_teleop(0,0)

  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
