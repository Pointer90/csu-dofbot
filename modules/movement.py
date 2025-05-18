import RPi.GPIO as GPIO
from modules.const import PinEnum as Pin, MOVEMENT_SPEED


class Car():
    def __init__():
        ''' Motor pins are initialized into output mode
            Key pin is initialized into input mode
            Ultrasonic pin initialization
        '''

        GPIO.setmode(GPIO.BCM)      # Set the GPIO port to BCM encoding mode.
        GPIO.setwarnings(False)     # Ignore warning information

        global pwm_ENA
        global pwm_ENB
        global pwm_SP

        GPIO.setup(Pin.ENA, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(Pin.IN1, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(Pin.IN2, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(Pin.ENB, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(Pin.IN3, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(Pin.IN4, GPIO.OUT, initial=GPIO.LOW)

        GPIO.setup(Pin.SP, GPIO.OUT)
        GPIO.setup(Pin.RX, GPIO.IN)
        GPIO.setup(Pin.EP, GPIO.IN)
        GPIO.setup(Pin.TP, GPIO.OUT)

        pwm_ENA = GPIO.PWM(Pin.ENA, 2000)
        pwm_ENB = GPIO.PWM(Pin.ENB, 2000)
        pwm_ENA.start(0)
        pwm_ENB.start(0)
        pwm_SP = GPIO.PWM(Pin.SP, 50)
        pwm_SP.start(0)

    def pwm_off():
        ''' Выключить питание моторов '''

        pwm_ENA.stop()
        pwm_ENB.stop()
        GPIO.cleanup()

    def run(left_speed: int = MOVEMENT_SPEED, right_speed: int = MOVEMENT_SPEED):
        ''' Функция движения вперед '''

        GPIO.output(Pin.IN1, GPIO.HIGH)
        GPIO.output(Pin.IN2, GPIO.LOW)
        GPIO.output(Pin.IN3, GPIO.HIGH)
        GPIO.output(Pin.IN4, GPIO.LOW)

        pwm_ENA.ChangeDutyCycle(left_speed)
        pwm_ENB.ChangeDutyCycle(right_speed)

    def back(left_speed: int = MOVEMENT_SPEED, right_speed: int = MOVEMENT_SPEED):
        ''' Функция движения назад '''

        GPIO.output(Pin.IN1, GPIO.LOW)
        GPIO.output(Pin.IN2, GPIO.HIGH)
        GPIO.output(Pin.IN3, GPIO.LOW)
        GPIO.output(Pin.IN4, GPIO.HIGH)

        pwm_ENA.ChangeDutyCycle(left_speed)
        pwm_ENB.ChangeDutyCycle(right_speed)
