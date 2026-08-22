import wpilib
from commands2 import Subsystem, Command
import wpilib.drive
import phoenix6
from phoenix6.controls import DutyCycleOut


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class DriveTrain(Subsystem):

    def __init__(self) -> None:
        super().__init__()         # Call the parent's (Super) initialization function

        self.left_leader_motor = phoenix6.hardware.TalonFX(1) 
        self.right_leader_motor = phoenix6.hardware.TalonFX(2)

        # Create control requests used by Phoenix Motors (Falcon 500)
        self.left_output = DutyCycleOut(0)
        self.right_output = DutyCycleOut(0)

        self.drive = wpilib.drive.DifferentialDrive(self.left_leader_motor.set, self.right_leader_motor.set)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def drive_teleop(self, forward: float, turn: float):
       self.drive.arcadeDrive(-forward, -turn)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

