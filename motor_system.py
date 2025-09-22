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
        
        
            
        