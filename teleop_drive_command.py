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
        self.drivetrain.drive_teleop( -self.controller.getRawAxis(1), -self.controller.getRawAxis(0))

        # Code used to investigate Axis on Gamepad
        # print(f"Axis 0: {self.controller.getRawAxis(0):.2f}  Axis 1: {self.controller.getRawAxis(1):.2f}  \
        # Axis 2: {self.controller.getRawAxis(2):.2f}  Axis 3: {self.controller.getRawAxis(3):.2f}  \
        # Axis 4: {self.controller.getRawAxis(4):.2f}  Axis 5: {self.controller.getRawAxis(5):.2f}  ")

        print(f"Wheel rotations: Left:{self.drivetrain.get_left_side_encoder_count():.2f}\
        Right:{self.drivetrain.get_right_side_encoder_count():.2f}  ")

    def isFinished(self) -> bool:
        return False
    
    def end(self, interrupted: bool):
        self.drivetrain.drive_teleop(0,0)

    #  FRC discussion on coordiate systems
    #  https://docs.wpilib.org/en/stable/docs/software/basic-programming/coordinate-system.html

  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
