import RPi.GPIO as GPIO
from modules.const import TRIBOT_LEFT_WHEEL, TRIBOT_MIDLE_WHEEL, TRIBOT_RIGHT_WHEEL, PinEnum as Pin, MOVEMENT_SPEED
from abc import ABC, abstractmethod


class BaseCar(ABC):
    def __init__(self):
        ''' Motor pins are initialized into output mode
            Key pin is initialized into input mode
            Ultrasonic pin initialization
        '''

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
        GPIO.setup(Pin.TX, GPIO.OUT)
        GPIO.setup(Pin.EP, GPIO.IN)
        GPIO.setup(Pin.TP, GPIO.OUT)

        pwm_ENA = GPIO.PWM(Pin.ENA, 2000)
        pwm_ENB = GPIO.PWM(Pin.ENB, 2000)
        pwm_ENA.start(0)
        pwm_ENB.start(0)
        pwm_SP = GPIO.PWM(Pin.SP, 50)
        pwm_SP.start(0)

    @abstractmethod
    def run():
        pass

    @abstractmethod
    def back():
        pass

    @abstractmethod
    def left():
        pass

    @abstractmethod
    def right():
        pass


class Car4WD(BaseCar):
    ''' Четырёхколёсный робот '''

    def pwm_off():
        ''' Выключить питание моторов '''

        pwm_ENA.stop()
        pwm_ENB.stop()
        GPIO.cleanup()

    def run(speed: int = MOVEMENT_SPEED):
        ''' Функция движения вперед, defaut speed = 10'''

        GPIO.output(Pin.IN1, GPIO.HIGH)
        GPIO.output(Pin.IN2, GPIO.LOW)
        GPIO.output(Pin.IN3, GPIO.HIGH)
        GPIO.output(Pin.IN4, GPIO.LOW)

        pwm_ENA.ChangeDutyCycle(speed)
        pwm_ENB.ChangeDutyCycle(speed)

    def back(speed: int = MOVEMENT_SPEED):
        ''' Функция движения назад, defaut speed = 10'''

        GPIO.output(Pin.IN1, GPIO.LOW)
        GPIO.output(Pin.IN2, GPIO.HIGH)
        GPIO.output(Pin.IN3, GPIO.LOW)
        GPIO.output(Pin.IN4, GPIO.HIGH)

        pwm_ENA.ChangeDutyCycle(speed)
        pwm_ENB.ChangeDutyCycle(speed)

    def left(speed: int = MOVEMENT_SPEED):
        '''
        Функция поворота направо.

        rotation_coefficient - коэффициент поворота, характеризующий скорость поворота
        '''

        rotation_coefficient = 1.25
        GPIO.output(Pin.IN1, GPIO.HIGH)
        GPIO.output(Pin.IN2, GPIO.LOW)
        GPIO.output(Pin.IN3, GPIO.HIGH)
        GPIO.output(Pin.IN4, GPIO.LOW)
        pwm_ENA.ChangeDutyCycle(speed)
        pwm_ENB.ChangeDutyCycle(speed * rotation_coefficient)

    def right(speed: int = MOVEMENT_SPEED):
        '''
        Функция поворота направо.
        
        rotation_coefficient - коэффициент поворота, характеризующий скорость поворота
        '''

        rotation_coefficient = 1.25
        GPIO.output(Pin.IN1, GPIO.HIGH)
        GPIO.output(Pin.IN3, GPIO.HIGH)
        GPIO.output(Pin.IN4, GPIO.LOW)
        GPIO.output(Pin.IN2, GPIO.LOW)
        pwm_ENA.ChangeDutyCycle(speed * rotation_coefficient)
        pwm_ENB.ChangeDutyCycle(speed)


class TriBot(Car4WD):
    ''' Трёхколёсный робот'''
    def run(self):
        self.pwm_servo.ChangeDutyCycle(2.5 + 10 * TRIBOT_MIDLE_WHEEL / 180)
        super().run()

    def back(self):
        self.pwm_servo.ChangeDutyCycle(2.5 + 10 * TRIBOT_MIDLE_WHEEL / 180)
        super().back()

    def right(self):
        self.pwm_servo.ChangeDutyCycle(2.5 + 10 * TRIBOT_RIGHT_WHEEL / 180)
        super().right()

    def left(self):
        self.pwm_servo.ChangeDutyCycle(2.5 + 10 * TRIBOT_LEFT_WHEEL / 180)
        super().left()
