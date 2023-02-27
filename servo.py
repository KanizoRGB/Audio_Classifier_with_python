import RPi.GPIO as GPIO
import time

# Set the GPIO mode and pins
GPIO.setmode(GPIO.BOARD)
servo_pin = 12
GPIO.setup(servo_pin, GPIO.OUT)

# Create a PWM object and set the frequency
pwm = GPIO.PWM(servo_pin, 50)

# Start the PWM with 0 duty cycle
pwm.start(0)

# Define a function to set the servo angle
def set_angle(angle):
    duty_cycle = angle / 18 + 2
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(1)
    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(0)

# Set the servo angle to 0 degrees
set_angle(0)

# Wait for 1 second
time.sleep(1)

# Set the servo angle to 90 degrees
set_angle(90)

# Wait for 1 second
time.sleep(1)

# Set the servo angle to 180 degrees
set_angle(180)

# Cleanup the GPIO pins
pwm.stop()
GPIO.cleanup()
