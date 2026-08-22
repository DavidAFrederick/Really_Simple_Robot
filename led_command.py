import wpilib
import wpilib.drive
from commands2 import Command
from led_subsystem import LEDSubsystem


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class LEDCommand(Command):
    def __init__(self, led: LEDSubsystem):
        self.led = led
        self.addRequirements(self.led)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    def initialize(self):
        pass        
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    def execute(self):
        self.led.rainbow()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    def isFinished(self) -> bool:
        return False

    def end(self, interrupted: bool):
        pass
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -









