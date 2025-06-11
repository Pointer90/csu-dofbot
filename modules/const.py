from enum import Enum

class PinEnum(Enum):
    IN1 = 20
    IN2 = 21
    IN3 = 19
    IN4 = 26
    ENA = 16
    ENB = 13

    RX = 8      # Define Bluetooth input
    TX = 10     # Define Bluetooth output
    SP = 23     # Define Servo Pin (SP)
    EP = 0      # Define Echo Pin (EP)
    TP = 1      # Define Trig Pin (TP)


MOVEMENT_SPEED = 10

TRIBOT_RIGHT_WHEEL = 0
TRIBOT_MIDLE_WHEEL = 55
TRIBOT_LEFT_WHEEL = 110
