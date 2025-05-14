import RPi.GPIO as GPIO
from modules.const import ENA, ENB, IN1, IN2, IN3, IN4, SP, RX, EP, TP, MOVEMENT_SPEED


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

        GPIO.setup(ENA, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(ENB, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(IN3, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(IN4, GPIO.OUT, initial=GPIO.LOW)

        GPIO.setup(SP, GPIO.OUT)
        GPIO.setup(RX, GPIO.IN)
        GPIO.setup(EP, GPIO.IN)
        GPIO.setup(TP, GPIO.OUT)

        pwm_ENA = GPIO.PWM(ENA, 2000)
        pwm_ENB = GPIO.PWM(ENB, 2000)
        pwm_ENA.start(0)
        pwm_ENB.start(0)
        pwm_SP = GPIO.PWM(SP, 50)
        pwm_SP.start(0)

    def pwm_off():
        ''' Выключить питание моторов '''

        pwm_ENA.stop()
        pwm_ENB.stop()
        GPIO.cleanup()

    def run(left_speed: int = MOVEMENT_SPEED, right_speed: int = MOVEMENT_SPEED):
        ''' Функция движения вперед '''

        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN3, GPIO.HIGH)
        GPIO.output(IN4, GPIO.LOW)

        pwm_ENA.ChangeDutyCycle(left_speed)
        pwm_ENB.ChangeDutyCycle(right_speed)

    def back(left_speed: int = MOVEMENT_SPEED, right_speed: int = MOVEMENT_SPEED):
        ''' Функция движения назад '''

        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.HIGH)
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.HIGH)

        pwm_ENA.ChangeDutyCycle(left_speed)
        pwm_ENB.ChangeDutyCycle(right_speed)
