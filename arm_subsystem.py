import wpilib
from commands2 import Subsystem
import wpilib.drive
from commands2 import Subsystem
from wpilib import SmartDashboard
from phoenix5 import TalonSRX, TalonSRXConfiguration, ControlMode, TalonSRXControlMode

import rev


'''
This Arm Subsystem consists of a standard 775 motor driving a Rev Robotics Gearbox.
The 775 motor is controlled by a CTRE Talon SRX.
Two shaft encoders are mounted on the output of the gearbox.
Two Beam Brakes are positioned at the ends of the range of motion (about 0 and 45 degrees).
The Beam Brakes provide a low signal on Digital Input/Output (DI/O) when the beam is broken.

One encoder is a Rev Robotics REV-11-1271 Through Bore Encoder. 
This encoder can operate in two modes; Absolute encoder mode and standard quadurature encoder.
The encoder cable breaks out the signals and they are connected to the RoboRIO inputs.

Absolute PWM = White, Red, Black
Quad A       = Blue, Red, Black
Quad B       = Yellow, Red, Black
Index signal = Green, Red, Black

The second encoder is a Rev Robotics MaxSpline encoder (REV-11-9008) that is read over the CAN bus.

The CAN address of the MaxSpline Encoder is set using the Rev Robotics Hardware Client Tool.
Since Rev Robotics is cheap, they did not put a USB-C connector on the device.  We can either 
a third party USB-CAN adaptor or place another Rev Robotics Device on the BUS and use it to
connect to the encoder.


Arm Software Requirements:
1) The right joystick vertical axis controls the position of the arm.
2) The arm rotation angle is limited to remain between the two beam breaks.


'''


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Arm(Subsystem):

    def __init__(self) -> None:
        super().__init__()         # Call the parent's (Super) initialization function

        # - - Initialize the Arm Motor Controller - - - - - - - - - - - - - - - - - - - - - - 
        self.Arm_Motor: TalonSRX = TalonSRX(31)  ## CAN Address (Set with Phoenix Tuner Application)
        self.Arm_Motor.configFactoryDefault()

        # - - Initialize the Rev Robotics REV-11-1271 Through Bore Encoder - - - - - - - - - - - - 

        # Initialize the REV Through Bore Encoder on Digital Input (DIO) channel 0
        # Make sure the physical switch on the encoder is set to 'A'
        self.encoder = wpilib.DutyCycleEncoder(0)

        # Optional: Set the scale / distance per rotation (default is 0.0 to 1.0 per turn)
        # To output in degrees (0.0 to 360.0):
        self.encoder.setPositionOffset(0.0) # set zero offset if needed
    

        # - - Initialize the MaxSpline Encoder - - - - - - - - - - - - - - - - - - - - - - 

        # Initialize the MAXSpline Encoder with its CAN device ID (e.g., ID 12)
        # Note: Ensure REVLib / RobotPy-REV is installed and your CAN bus is configured.
        self.spline_encoder = rev.SplineEncoder(12)
        
        # Optionally set a relative starting position (in rotations or units)
        self.spline_encoder.setPosition(0.0)

        # - - Initialize the Beam Break Digital I/O - - - - - - - - - - - - - - - - - 

        self.lowerlimit = wpilib.DigitalInput(1)
        self.upperlimit = wpilib.DigitalInput(2)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def spin_arm_motor(self, speed: float) -> None:
        self.Arm_Motor.set(TalonSRXControlMode.PercentOutput, speed)
        wpilib.SmartDashboard.putNumber("Arm Motor Speed", speed)

    def read_through_shaft_encoder(self):
        # Get the absolute position (returns a value from 0.0 to 1.0 for one full rotation)
        abs_position = self.encoder.get()

        # Convert to degrees if desired
        angle_degrees = abs_position * 360.0

        # Print or use the position values in your robot logic
        # print(f"Absolute Position: {abs_position:.3f} | Angle: {angle_degrees:.1f}°")
        wpilib.SmartDashboard.putNumber("Through Encoder Position", abs_position)
        wpilib.SmartDashboard.putNumber("Through Encoder Angle", angle_degrees)

    def read_can_shaft_encoder(self):
        # Retrieve values from the MAXSpline Encoder
        position = self.spline_encoder.getPosition()       # Relative position
        velocity = self.spline_encoder.getVelocity()       # Velocity
        absolute_angle = self.spline_encoder.getAbsolutePosition() # Absolute angle/position

        # Print values to the driver station log / console
        wpilib.SmartDashboard.putNumber("Spline Position", position)
        wpilib.SmartDashboard.putNumber("Spline Velocity", velocity)
        wpilib.SmartDashboard.putNumber("Spline Abs Angle", absolute_angle)

    def get_upper_limit_sensor(self):
        wpilib.SmartDashboard.putBoolean("Upper Limit", self.upperlimit)
        return self.upperlimit

    def get_lower_limit_sensor(self):
        wpilib.SmartDashboard.putBoolean("Lower Limit", self.upperlimit)
        return self.lowerlimit

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

