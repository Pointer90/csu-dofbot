import socket
import json

from time import sleep

class Wifi():
    _type: int
    run: bool = True
    timeout: float = 5.0
    DEFAULT_PORT: 5050

    def __init__(self, type_connection: int = 0):
        self._type = type_connection # Type of connnection Master/Slave

    def connect(self, ip: str, port: int = DEFAULT_PORT) -> socket.socket:
        ''' Функция для подключения к роботу Slave'''
        
        if self._type == 0:
            raise ValueError
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                sock.connect((ip, port))
            
            except Exception as e:
                print(f'Connection failed')

        return sock

    def shutdown(self):
        self.run = False

    def stream(self, callback_func, port: int = DEFAULT_PORT, connect_count: int = 2) -> None:
        ''' Функция для вещания робота Master'''

        if self._type == 1:
            raise ValueError
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                sock.bind(('', port))
                sock.listen(connect_count)
                print("Server is running...\nconnection awaited", end='\r')

                conn, addr = sock.accept()

                while self.run:
                    try:
                        callback_func(conn)
                        print(f'Connection with {addr}:{port} alive', end='\r')

                    except Exception as e:
                        print(f'Connection with {addr}:{port} disconnect: {e}', end='\r')
                        raise

                    finally:
                        sock.close()
            
            except Exception as e:
                print(f'Server fatal error: {e}')
                raise
    
wifi = Wifi()
def test():
    count = 0
    print(f'It is alive!!!! {count}')
    count += 1
    sleep(5)

wifi.stream(test)