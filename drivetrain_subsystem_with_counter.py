# Import the libraries that control the robot
import wpilib
from commands2 import Subsystem, Command
import wpilib.drive

# Import the libraries specific for our smart motors (Talon FX)
from phoenix6.configs import TalonFXConfiguration
from phoenix6.hardware.talon_fx import TalonFX
from phoenix6.signals.spn_enums import (InvertedValue, NeutralModeValue, FeedbackSensorSourceValue)
from phoenix6.controls import DutyCycleOut
from phoenix6 import StatusCode

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class DriveTrain(Subsystem):

    def __init__(self) -> None:
        super().__init__()         # Call the parent's (Super) initialization function

        # Apply all the configurations to the left and right side Talon motor controllers
        self.__configure_left_side_drive()
        self.__configure_right_side_drive()
        print ("DriveTrain  Subsystem Initialization complete")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def __configure_left_side_drive(self) -> None:
        self.left_leader_motor = TalonFX(1)     # 1 is the CAN bus address

        # Applying a new configuration will erase all other config settings since
        # we start with a blank config so each setting needs to be explicitly set
        # here in the config method
        config = TalonFXConfiguration()

        # Set the left side motors to be counter clockwise positive
        config.motor_output.inverted = InvertedValue.COUNTER_CLOCKWISE_POSITIVE

        # Set the motors to electrically stop instead of coast
        config.motor_output.neutral_mode = NeutralModeValue.BRAKE

        # This configuration item supports counting wheel rotations
        # This item sets the gear ratio between motor turns and wheel turns
        config.feedback.feedback_sensor_source = FeedbackSensorSourceValue.ROTOR_SENSOR
        config.feedback.sensor_to_mechanism_ratio = 10

        # Apply the configuration to the motors
        for i in range(6):  # Try 5 times
           ret = self.left_leader_motor.configurator.apply(config)

        self.left_leader_motor.set_position(0)    #  Reset the encoder to  zero

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def __configure_right_side_drive(self) -> None:
       
        self.right_leader_motor = TalonFX(2)     # 2 is the CAN bus address
        # Applying a new configuration will erase all other config settings since
        # we start with a blank config so each setting needs to be explicitly set
        # here in the config method
        config = TalonFXConfiguration()

        # Set the left side motors to be counter clockwise positive
        config.motor_output.inverted = InvertedValue.CLOCKWISE_POSITIVE

        # Set the motors to electrically stop instead of coast
        config.motor_output.neutral_mode = NeutralModeValue.BRAKE

        # This configuration item supports counting wheel rotations
        # This item sets the gear ratio between motor turns and wheel turns
        config.feedback.feedback_sensor_source = FeedbackSensorSourceValue.ROTOR_SENSOR
        config.feedback.sensor_to_mechanism_ratio = 10

        # # Apply the configuration to the motors
        for i in range(6):  # Try 5 times
           ret = self.right_leader_motor.configurator.apply(config)

        self.left_leader_motor.set_position(0)    #  Reset the encoder to  zero

   ########################### Drivetrain Drive methods #######################

    def drive_teleop(self, forward: float, turn: float):

        # This calculates the required wheel speeds to move the robot 
        # based on the desired forward speed and turn rate       
        speeds = wpilib.drive.DifferentialDrive.curvatureDriveIK(forward, turn, True)

        # FRC description of DifferentialDrive
        # https://docs.wpilib.org/en/stable/docs/software/hardware-apis/motors/wpi-drive-classes.html

        # print (f"[drive_teleop] forward:{forward:.1f} turn:{turn:.1f} \
        #        Wheel Speeds: Left:{speeds.left:.1f}  Right:{speeds.right:.1f}")

        self.left_percent_out: DutyCycleOut = DutyCycleOut(0)
        self.right_percent_out: DutyCycleOut = DutyCycleOut(0)

        self.left_percent_out.output = speeds.left
        self.right_percent_out.output = speeds.right

        self.left_leader_motor.set_control(self.left_percent_out)
        self.right_leader_motor.set_control(self.right_percent_out)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

   ###########################  Drive Encoder methods #######################

    def get_left_side_encoder_count(self):
        self.left_leader_motor.get_rotor_position()
        return self.left_leader_motor.get_position().value

    def get_right_side_encoder_count(self):
        self.right_leader_motor.get_rotor_position()
        return self.right_leader_motor.get_position().value
  
    def reset_left_side_encoder_count(self):
        self.left_leader_motor.set_position(0)    #  Reset the encoder to  zero

    def reset_right_side_encoder_count(self):
        self.right_leader_motor.set_position(0)    #  Reset the encoder to  zero

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

