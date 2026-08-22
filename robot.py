#!/usr/bin/env python3

import wpilib
import wpilib.drive
from commands2 import Command, CommandScheduler, TimedCommandRobot
from commands2.button import JoystickButton

from led_subsystem import LEDSubsystem
from led_command import LEDCommand
from drivetrain_subsystem import DriveTrain
from teleop_drive_command import TeleopDrive
from one_button_drive_command import DriveShortDistance

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class MyRobot(TimedCommandRobot):
    """Main robot class"""

    def robotInit(self):
        """Robot-wide initialization code should go here"""

        # Create a joystick object
        self.leftstick = wpilib.Joystick(0)

        # Create a drivetrain object
        self.drivetrainSubSys: DriveTrain = DriveTrain()
        self.drivetrainSubSys.setDefaultCommand(TeleopDrive(self.drivetrainSubSys, self.leftstick))

        self.led = LEDSubsystem()
        self.led.setDefaultCommand(LEDCommand(self.led))

        # Create a button object
        self.button_1 = JoystickButton(self.leftstick, 1)
        self.button_1.onTrue(DriveShortDistance(self.drivetrainSubSys))


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    def getAutonomousCommand(self) -> Command:
        return DriveShortDistance(self.drivetrainSubSys)

    def autonomousInit(self):
        """Called when autonomous mode is enabled"""

        self._auto_command = self.getAutonomousCommand()
        if self._auto_command is not None:
           self._auto_command.schedule()
        
        CommandScheduler.getInstance().removeDefaultCommand(self.drivetrainSubSys)

    def autonomousPeriodic(self):
        pass

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    def teleopInit(self):
       pass

    def teleopPeriodic(self):
       """Called when operation control mode is enabled"""
       pass

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


