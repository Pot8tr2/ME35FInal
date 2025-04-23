import time
import threading
import RPi.GPIO as GPIO

class StepperObject:
    # Define GPIO pins and constants
    OUT1, OUT2, OUT3, OUT4 = 18, 17, 22, 27
    ROT_A, ROT_B, ROT_BUTTON = 23, 24, 10

    STEPS = [
        [GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.LOW],
        [GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.LOW],
        [GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.HIGH],
        [GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH],
    ]

    STEP_ANGLE = 0.35
    
    """
    SAVED POSITIONS FOR GIVEN ANGLES: 
        SKILLET A is a 45 degree left
        SKILLET B is a 45 degree right

        NOTE: Positions must be divisble by 4 to ensure proper stepping.

    """
    POSITION_ARR = {"INITIAL": 0, "SKILLET A": -312, "SKILLET B": 312}

    def __init__(self):
        self.current_step = 0
        self.current_position = 0
        self.stop_flag = threading.Event()
        self._initialize_gpio()

    def _initialize_gpio(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup([self.OUT1, self.OUT2, self.OUT3, self.OUT4], GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup([self.ROT_A, self.ROT_B], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def _get_direction(self, delta):
        if delta > 0:
            return 1
        elif delta < 0:
            return -1
        return 0

    def move_to_position(self, target_position):
        direction = self._get_direction(target_position - self.current_position)
        step_delay = 0.01

        try:
            while self.current_position != target_position:
                for i, pin in enumerate([self.OUT1, self.OUT2, self.OUT3, self.OUT4]):
                    GPIO.output(pin, self.STEPS[self.current_step][i])
                time.sleep(step_delay)
                self.current_step = (self.current_step + direction) % 4
                self.current_position += direction
        finally:
            self.stop_motor()
        time.sleep(0.5)

    def stop_motor(self):
        GPIO.output([self.OUT1, self.OUT2, self.OUT3, self.OUT4], GPIO.LOW)

    def move_to_named_position(self, name):
        if name not in self.POSITION_ARR:
            raise ValueError(f"Invalid position name: {name}")
        self.move_to_position(self.POSITION_ARR[name])

    def cleanup(self):
        GPIO.cleanup()