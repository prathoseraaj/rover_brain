import time
import atexit

try:
    import RPi.GPIO as GPIO
    print("STATUS: Running on REAL Raspberry Pi Hardware.")
except:
    print("WARNING: RPi.GPIO not found. Using MOCK mode for simulation.")
     
    class MockGPIO:
         
        HIGH, LOW, OUT, BCM = 1, 0, 1, 1
         
        def setmode(self,mode):
            print("MOCK: GPIO mode set")
        def setup(self, pin, mode): 
            print(f"MOCK: Pin {pin} set up as OUTPUT.")
        def output(self,pin,value):
            state = "HIGH" if value == self.HIGH else "LOW"
            print(f"MOCK: Pin {pin} set to {state}.")
        
        def PWM(self, pin, freq):
            print(f"MOCK: PWM on Pin {pin} started with frequency {freq}Hz.")
            class MockPWM:
                def start(self, dc): 
                    print(f"MOCK: PWM started at {dc}% duty cycle.")
                def ChangeDutyCycle(self, dc): 
                    print(f"MOCK: Speed changed to {dc}%.")
                def stop(self):
                    pass 
            return MockPWM()
        
        def cleanup(self):
            print("--- MOCK: GPIO Cleanup complete. ---")
            
    import sys
    sys.modules['RPi'] = MockGPIO()
    sys.modules['RPi.GPIO'] = MockGPIO()
    GPIO = MockGPIO()

RIGHT_IN1 = 17
RIGHT_IN2 = 27
RIGHT_EN = 22

LEFT_IN3 = 23
LEFT_IN4 = 24
LEFT_EN = 25 #EN pin is used to get the PWM(pulse width modulation)'s output

pwm_right = None
pwm_left  = None

def init_motor_pins():
    global pwm_right, pwm_left
    
    if pwm_right is not None:
        return
    
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup([RIGHT_IN1, RIGHT_IN2, RIGHT_EN, LEFT_IN3, LEFT_IN4, LEFT_EN], GPIO.OUT)
    
    # Creates PWM objects on the enable pins at 100 Hz frequency.
    pwm_right = GPIO.PWM(RIGHT_EN, 100) 
    pwm_left = GPIO.PWM(LEFT_EN, 100)
    
    pwm_right.start(0)
    pwm_left.start(0)
    
def cleanup():
    global pwm_right, pwm_left
    if pwm_right: pwm_right.stop()
    if pwm_left: pwm_left.stop()
    GPIO.cleanup()

atexit.register(cleanup) #ensure the cleanup runs when the system exits.

# MAXIMIZED DEFAULT SPEED TO 100% to test power limits
def move_forward(speed=100):
    init_motor_pins()
    print(f"COMMAND: Moving forward at{speed}% speed.")
    
    # Right motors FORWARD
    GPIO.output(RIGHT_IN1, GPIO.HIGH)
    GPIO.output(RIGHT_IN2, GPIO.LOW)
    # Left motors FORWARD
    GPIO.output(LEFT_IN3, GPIO.HIGH)
    GPIO.output(LEFT_IN4, GPIO.LOW)   
    
    pwm_right.ChangeDutyCycle(speed)
    pwm_left.ChangeDutyCycle(speed)

# MAXIMIZED DEFAULT SPEED TO 100%
def move_backward(speed=100):
    init_motor_pins()
    print(f"COMMAND: Moving backward at{speed}% speed.")
    
    # Right motors BACKWARD
    GPIO.output(RIGHT_IN1, GPIO.LOW)
    GPIO.output(RIGHT_IN2, GPIO.HIGH)
    # Left motors BACKWARD
    GPIO.output(LEFT_IN3, GPIO.LOW)
    GPIO.output(LEFT_IN4, GPIO.HIGH)
    
    pwm_right.ChangeDutyCycle(speed)
    pwm_left.ChangeDutyCycle(speed)

# MAXIMIZED DEFAULT SPEED TO 100%
def turn_left(speed=100):
    init_motor_pins()
    
    print(f"COMMAND: Executing Pivot Turn Left at {speed}% speed.")
    
    # Action: Right Motors BACKWARD, Left Motors FORWARD
    
    # Right motors BACKWARD (Pulling the rover left for a tight pivot)
    GPIO.output(RIGHT_IN1, GPIO.LOW)
    GPIO.output(RIGHT_IN2, GPIO.HIGH)
    
    # Left motors FORWARD (Pushing the rover left for a tight pivot)
    GPIO.output(LEFT_IN3, GPIO.HIGH)
    GPIO.output(LEFT_IN4, GPIO.LOW)
    
    pwm_right.ChangeDutyCycle(speed)
    pwm_left.ChangeDutyCycle(speed)

# MAXIMIZED DEFAULT SPEED TO 100%
def turn_right(speed=100):
    init_motor_pins()
    
    print(f"COMMAND: Executing Pivot Turn Right at {speed}% speed.")
    
    # Action: Right Motors FORWARD, Left Motors BACKWARD

    # Right motors FORWARD (Pushing the rover right for a tight pivot)
    GPIO.output(RIGHT_IN1, GPIO.HIGH)
    GPIO.output(RIGHT_IN2, GPIO.LOW)
    
    # Left motors BACKWARD (Pulling the rover right for a tight pivot)
    GPIO.output(LEFT_IN3, GPIO.LOW)
    GPIO.output(LEFT_IN4, GPIO.HIGH)
    
    pwm_right.ChangeDutyCycle(speed)
    pwm_left.ChangeDutyCycle(speed)
    
def stop_rover_motion(speed=50):
    print("COMMAND: HALTING MOTION")
    
    GPIO.output([RIGHT_IN1, RIGHT_IN2, LEFT_IN3, LEFT_IN4], GPIO.LOW)
    
    global pwm_right,pwm_left
    if pwm_right:
        pwm_right.ChangeDutyCycle(0)
    if pwm_left:
        pwm_left.ChangeDutyCycle(0)

if __name__ == "__main__":
    print("---- Running Local Test ----")
    move_forward(70)
    time.sleep(1)
    turn_left(40)
    time.sleep(1)
    stop_rover_motion()
    time.sleep(1)
