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
        def output(self,pin,mode):
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
    if pwm_right: pwm_right.stop()
    if pwm_left: pwm_left.stop()
    GPIO.cleanup()

atexit.register(cleanup) #ensure the cleanup runs when the system exits.
    


        
            
        