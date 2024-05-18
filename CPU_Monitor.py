#!/usr/bin/env python3
import RPi.GPIO as GPIO
import psutil

LED1 = 21
LED2 = 20
LED3 = 16
LED4 = 26
LED5 = 19
LED6 = 13
LED7 = 6
LED8 = 5

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)
GPIO.setup(LED4, GPIO.OUT)
GPIO.setup(LED5, GPIO.OUT)
GPIO.setup(LED6, GPIO.OUT)
GPIO.setup(LED7, GPIO.OUT)
GPIO.setup(LED8, GPIO.OUT)


try:
    while (1):
        cpu_pc = psutil.cpu_percent(interval=1)
        print("CPU = " + str(cpu_pc) + "%")
        if cpu_pc <= 10:
            GPIO.output(LED1, False)
            GPIO.output(LED2, False)
            GPIO.output(LED3, False)
            GPIO.output(LED4, False)
            GPIO.output(LED5, False)
            GPIO.output(LED6, False)
            GPIO.output(LED7, False)
            GPIO.output(LED8, False)
        if 10 < cpu_pc < 20:
            GPIO.output(LED1, True)
            GPIO.output(LED2, False)
            GPIO.output(LED3, False)
            GPIO.output(LED4, False)
            GPIO.output(LED5, False)
            GPIO.output(LED6, False)
            GPIO.output(LED7, False)
            GPIO.output(LED8, False)
        if 20 < cpu_pc < 30:
            GPIO.output(LED1, True)
            GPIO.output(LED2, True)
            GPIO.output(LED3, False)
            GPIO.output(LED4, False)
            GPIO.output(LED5, False)
            GPIO.output(LED6, False)
            GPIO.output(LED7, False)
            GPIO.output(LED8, False)
        if 30 < cpu_pc < 40:
            GPIO.output(LED3, True)
            GPIO.output(LED2, True)
            GPIO.output(LED3, True)
            GPIO.output(LED4, False)
            GPIO.output(LED5, False)
            GPIO.output(LED6, False)
            GPIO.output(LED7, False)
            GPIO.output(LED8, False)
        if 40 < cpu_pc < 50:
            GPIO.output(LED4, True)
            GPIO.output(LED2, True)
            GPIO.output(LED3, True)
            GPIO.output(LED4, True)
            GPIO.output(LED5, False)
            GPIO.output(LED6, False)
            GPIO.output(LED7, False)
            GPIO.output(LED8, False)
        if 50 < cpu_pc < 60:
            GPIO.output(LED5, True)
            GPIO.output(LED2, True)
            GPIO.output(LED3, True)
            GPIO.output(LED4, True)
            GPIO.output(LED5, True)
            GPIO.output(LED6, False)
            GPIO.output(LED7, False)
            GPIO.output(LED8, False)
        if 60 < cpu_pc < 70:
            GPIO.output(LED6, True)
            GPIO.output(LED2, True)
            GPIO.output(LED3, True)
            GPIO.output(LED4, True)
            GPIO.output(LED5, True)
            GPIO.output(LED6, True)
            GPIO.output(LED7, False)
            GPIO.output(LED8, False)
        if 70 < cpu_pc < 80:
            GPIO.output(LED7, True)
            GPIO.output(LED2, True)
            GPIO.output(LED3, True)
            GPIO.output(LED4, True)
            GPIO.output(LED5, True)
            GPIO.output(LED6, True)
            GPIO.output(LED7, True)
            GPIO.output(LED8, False)
        if 80 < cpu_pc < 90:
            GPIO.output(LED8, True)
            GPIO.output(LED2, True)
            GPIO.output(LED3, True)
            GPIO.output(LED4, True)
            GPIO.output(LED5, True)
            GPIO.output(LED6, True)
            GPIO.output(LED7, True)
            GPIO.output(LED8, True)
        if 90 < cpu_pc < 100:
            GPIO.output(LED8, True)
            GPIO.output(LED2, False)
            GPIO.output(LED3, True)
            GPIO.output(LED4, False)
            GPIO.output(LED5, True)
            GPIO.output(LED6, False)
            GPIO.output(LED7, True)
            GPIO.output(LED8, False)

except KeyboardInterrupt:
    GPIO.cleanup()
    print  ("Thank you for using CPU Monitor")