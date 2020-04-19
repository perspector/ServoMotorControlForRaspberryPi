# ServoMotorControlForRaspberryPi
This simple Python code will let you control servo motors easily!
Look at your servo motor, or your servo motor datasheet.
Find the voltage needed, (mine was 6 volts), and get a battery with that voltage.
If your servo motor needs 5 volts, you can plug it directly into your Raspberry Pi 3B+.
Connect the VCC (+) wire to the VCC (+) of the battery, and do likewise with the GND (-).
Then, connect the PWM (yellow) wire from the servo motor to BCM pin #26 (normal pin #37) of your Raspberry Pi.
Then, run testServo.py. Your servo motor should work!
