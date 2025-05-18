from enum import Enum

class PinEnum(Enum):
    IN1 = 20
    IN2 = 21
    IN3 = 19
    IN4 = 26
    ENA = 16
    ENB = 13

    RX = 8      # Define UART RX pin
    SP = 23     # Define Servo Pin (SP)
    EP = 0      # Define Echo Pin (EP)
    TP = 1      # Define Trig Pin (TP)


class WifiEnum(Enum):
    DEFAULT_PORT = 5050
    CONNECTION_COUNT = 2

MOVEMENT_SPEED = 10
