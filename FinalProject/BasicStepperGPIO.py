''' Author: Briana Bouchard
This script moves a stepper motor a set number of steps. 
'''  
import RPi.GPIO as GPIO
import time


# Define the GPIO pins for the L298N motor driver


class BatterPour:
    def  __init__(self,OUT1,OUT2,OUT3,OUT4):
        print("WTF")
        self.OUT1 = OUT1#29#GPIO5
        self.OUT2 = OUT2#32#GPIO12
        self.OUT3 = OUT3#31#GPIO6
        self.OUT4 = OUT4#33#GPIO13

        GPIO.setmode(GPIO.BCM)
    # Set the GPIO pins as output
        GPIO.setup(self.OUT1, GPIO.OUT)
        GPIO.setup(self.OUT2, GPIO.OUT)
        GPIO.setup(self.OUT3, GPIO.OUT)
        GPIO.setup(self.OUT4, GPIO.OUT)
        
        # Set initial state of pins to low
        GPIO.output(self.OUT1,GPIO.LOW)
        GPIO.output(self.OUT2,GPIO.LOW)
        GPIO.output(self.OUT3,GPIO.LOW)
        GPIO.output(self.OUT4,GPIO.LOW)



    def rotate_right(self,num_steps,step_delay):
       current_step = 0
          
       for x in range(num_steps):
           if current_step == 0:
               GPIO.output(self.OUT1,GPIO.HIGH)
               GPIO.output(self.OUT2,GPIO.LOW)
               GPIO.output(self.OUT3,GPIO.HIGH)
               GPIO.output(self.OUT4,GPIO.LOW)
               time.sleep(step_delay)
               #print("step 0")
           elif current_step == 1:
               GPIO.output(self.OUT1,GPIO.LOW)
               GPIO.output(self.OUT2,GPIO.HIGH)
               GPIO.output(self.OUT3,GPIO.HIGH)
               GPIO.output(self.OUT4,GPIO.LOW)
               time.sleep(step_delay)
               #print("step 1")
           elif current_step == 2:
               GPIO.output(self.OUT1,GPIO.LOW)
               GPIO.output(self.OUT2,GPIO.HIGH)
               GPIO.output(self.OUT3,GPIO.LOW)
               GPIO.output(self.OUT4,GPIO.HIGH)
               time.sleep(step_delay)
           elif current_step == 3:
               GPIO.output(self.OUT1,GPIO.HIGH)
               GPIO.output(self.OUT2,GPIO.LOW)
               GPIO.output(self.OUT3,GPIO.LOW)
               GPIO.output(self.OUT4,GPIO.HIGH)
               time.sleep(step_delay)
           if current_step == 3:
               current_step = 0
               continue
           current_step = current_step + 1


    def rotate_left(self,num_steps,step_delay):
       current_step = 0
          
       for x in range(num_steps):
           if current_step == 0:
               GPIO.output(self.OUT1,GPIO.HIGH)
               GPIO.output(self.OUT2,GPIO.LOW)
               GPIO.output(self.OUT3,GPIO.LOW)
               GPIO.output(self.OUT4,GPIO.HIGH)
               time.sleep(step_delay)
               #print("step 0")
           elif current_step == 1:
               GPIO.output(self.OUT1,GPIO.LOW)
               GPIO.output(self.OUT2,GPIO.HIGH)
               GPIO.output(self.OUT3,GPIO.LOW)
               GPIO.output(self.OUT4,GPIO.HIGH)
               time.sleep(step_delay)
               #print("step 1")
           elif current_step == 2:
               GPIO.output(self.OUT1,GPIO.LOW)
               GPIO.output(self.OUT2,GPIO.HIGH)
               GPIO.output(self.OUT3,GPIO.HIGH)
               GPIO.output(self.OUT4,GPIO.LOW)
               time.sleep(step_delay)
           elif current_step == 3:
               GPIO.output(self.OUT1,GPIO.HIGH)
               GPIO.output(self.OUT2,GPIO.LOW)
               GPIO.output(self.OUT3,GPIO.HIGH)
               GPIO.output(self.OUT4,GPIO.LOW)
              
               time.sleep(step_delay)
           if current_step == 3:
               current_step = 0
               continue
           current_step = current_step + 1
    
# # Sets number of steps to move
# num_steps = 35

# # Sets delay between steps
# step_delay = 0.03

# # Try-Except block asks program to complete try tasks until keyboard interrupt (CNTL-C)
# try:
#     batterpour = batterpour(5,12,6,13);

#         #     self.OUT1 = OUT1#29#GPIO5
#         # self.OUT2 = OUT2#32#GPIO12
#         # self.OUT3 = OUT3#31#GPIO6
#         # self.OUT4 = OUT4#33#GPIO13
#     print("turned left")
#     batterpour.rotate_left(num_steps,step_delay)
#     time.sleep(3)
#     print("turened right")
#     batterpour.rotate_right(num_steps,step_delay)
#     GPIO.cleanup()
                    
# except KeyboardInterrupt:
#     GPIO.cleanup()

