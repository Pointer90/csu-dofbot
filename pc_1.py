from modules.wifi import Wifi
from modules.parser.parser import Parser
from modules.parser.schemas import BaseDTO


def callback(conn):
    conn.send(Parser().send(
        BaseDTO(
            target='__main__',
            cmd='run',
            args=[]
        )
    ))


try:
    t = Wifi()
    t.stream(callback)
except Exception as e:
    print(e)
