import wpilib
import wpilib.drive
from commands2 import Command
from drivetrain_subsystem_with_counter import DriveTrain


class DriveRobotXWheelCounts(Command):
   def __init__(self, drivetrain: DriveTrain, targetwheelcounts: float, forwardSpeed: int):
       self.drivetrain = drivetrain
       self.targetwheelcounts = targetwheelcounts
       self.forwardSpeed = forwardSpeed
       self.addRequirements(self.drivetrain)
       self.drivetrain.reset_left_side_encoder_count()
       print ("Driving for ", targetwheelcounts,  " Wheel Counts Command Initialized")

   def initialize(self):
       super().initialize()
       self.drivetrain.reset_left_side_encoder_count()

   def execute(self):
       self.drivetrain.drive_teleop(self.forwardSpeed, 0.0)
       print (f"Wheel Counts: {self.drivetrain.get_left_side_encoder_count():.2f}")

   def isFinished(self) -> bool:
       if self.drivetrain.get_left_side_encoder_count() >= self.targetwheelcounts:
           return True
       else:
           return False
  
   def end(self, interrupted: bool):
       self.drivetrain.drive_teleop(0,0)


