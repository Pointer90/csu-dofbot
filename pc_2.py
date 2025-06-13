from modules.wifi import Wifi
from modules.parser.parser import Parser
from modules.movement import Car4WD

from time import sleep

sock = Wifi(1).connect('localhost')
car = Car4WD()

while True:
    data = sock.recv(2048)
    print(f'RECV: {data}')
    func, args = Parser().excute(data)
    car.func(args)
    sleep(5)
