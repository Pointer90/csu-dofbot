from modules.movement import Car
from time import sleep

try:
    car = Car()
    car.run()
    sleep(3)
    car.pwm_off()

except KeyboardInterrupt:
    pass