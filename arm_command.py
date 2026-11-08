import wpilib
import wpilib.drive
from commands2 import Command
from arm_subsystem import Arm

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class ArmCommand(Command):
    def __init__(self, arm_subsystem: Arm, right_joystick: wpilib.Joystick):
        self.arm_subsystem = arm_subsystem
        self.right_joystick = right_joystick
        self.addRequirements(self.arm_subsystem)

  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def initialize(self):
        pass

    def execute(self):
        speed_reduction = 0.5
        arm_speed = self.right_joystick.getRawAxis(0) * speed_reduction

        # Stop the motor from going past the limit BUT ALSO allow the arm to move away from the limit
        # Low / False means limit is reached
        if ((not self.arm_subsystem.get_upper_limit_sensor()) and (arm_speed > 0) ): 
            arm_speed = 0

        if ((not self.arm_subsystem.get_lower_limit_sensor()) and (arm_speed < 0) ): 
            arm_speed = 0

        self.arm_subsystem.Arm_Motor(arm_speed)


    def isFinished(self) -> bool:
        return False
    
    def end(self, interrupted: bool):
        pass

    #  FRC discussion on coordiate systems
    #  https://docs.wpilib.org/en/stable/docs/software/basic-programming/coordinate-system.html

  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
