import time
import atexit

try:
    import RPi.GPIO as GPIO
    print("STATUS: Running on REAL Raspberry Pi Hardware.")
except:
