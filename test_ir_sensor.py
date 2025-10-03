import time
import RPi.GPIO as GPIO
#-------------------
#GPIO Setup
#-------------------
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

IR_LEFT = 24   # Venstre IR
IR_RIGHT = 26  # Højre IR

GPIO.setup(IR_LEFT, GPIO.IN)
GPIO.setup(IR_RIGHT, GPIO.IN)

print("Starter IR sensor test. Tryk CTRL+C for at stoppe.")

try:
    while True:
        left_state = GPIO.input(IR_LEFT)
        right_state = GPIO.input(IR_RIGHT)

        # Print status (du kan holde noget foran sensoren for at teste)
        print(f"Venstre IR: {left_state} | Højre IR: {right_state}")

        time.sleep(0.2)

except KeyboardInterrupt:
    print("Test afsluttet")
    GPIO.cleanup()
