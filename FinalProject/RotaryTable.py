from stepper import StepperObject
from BasicStepperGPIO import BatterPour
from AirtablePancake import at
import sys
import time
import RPi.GPIO as GPIO

stepper = StepperObject()
bp = BatterPour(5,12,6,13);
airtable = at()


#assume it goes like this in terms of status 00 is none. 
# 1 is right side set 01. 2 is other side set 10. 
# 3 is both set 11./.,
# assume this is out of the way, once this is set

#last bit is clearance for doing stuff.
# so 100, 1
def initialize():
    # IMPLEMENT SETUP FUNCTION
    airtable.checkValue("Cooking 1 Status")
    pass

def release_batter():
    bp.rotate_left(20,0.03)
    time.sleep(4.75)
    bp.rotate_right(20,0.03)
    time.sleep(1)

def dispense_skillet_a():  
    stepper.move_to_named_position("SKILLET A")
    release_batter()
    stepper.move_to_named_position("INITIAL")
    # allow it to update the airtable
    pass

def dispense_skillet_b():
    stepper.move_to_named_position("SKILLET B")  
    release_batter()
    stepper.move_to_named_position("INITIAL")
    # allow it to pour the batter
    pass

def dispense_skillet_both():
    stepper.move_to_named_position("SKILLET B")    
    stepper.move_to_named_position("SKILLET A")
    stepper.move_to_named_position("INITIAL")
    pass

def emergency_stop():
    print("SYSTEM EMERGENCY STOP")
    GPIO.cleanup()
    sys.exit(3)


def blocking_loop():
    # check both batter stations. this behavior is blocking, 
    # because there shouldn't need any other behavior 
    # will be back at the default state
    stepper.move_to_named_position("INITIAL")
    try:
        while True:
            if(airtable.checkValue("Cooking 1 Status")==1):
                dispense_skillet_a()
                dispense_skillet_b()
                airtable.changeValue("Cooking 1 Status", 2)
                airtable.changeValue("Cooking 2 Status", 2)
    except KeyboardInterrupt:
        stepper.move_to_named_position("INITIAL")
        GPIO.cleanup()

    GPIO.cleanup()

def test():
    dispense_skillet_b()
    dispense_skillet_a()
        

# Main program
def main():
    try:
        initialize()
        blocking_loop()
    except KeyboardInterrupt:
        stepper.move_to_named_position("INITIAL")
        GPIO.cleanup()

if __name__ == "__main__":
    main()