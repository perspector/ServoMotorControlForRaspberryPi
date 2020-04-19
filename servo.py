def Servo(turn):
    try:
        import sys
        import RPi.GPIO as GPIO
        import time
        from time import sleep
        
        servoPIN = 26
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(servoPIN, GPIO.OUT)
        
        p = GPIO.PWM(servoPIN, 50) # GPIO 2 for PWM with 50Hz
        p.start(7.6) # Initialization
        
        if turn == "r":
            p.ChangeDutyCycle(5)
            sleep(0.5)
        elif turn == "l":
            p.ChangeDutyCycle(10)
            sleep(0.5)
        elif turn == "s":
            p.ChangeDutyCycle(7.5)
            sleep(0.5)
        elif turn == "stop":
            p.stop()
            GPIO.cleanup()
            sys.exit()
            
    
    except KeyboardInterrupt:
        p.stop()
        GPIO.cleanup()
