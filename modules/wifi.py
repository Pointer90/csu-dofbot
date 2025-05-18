import socket

DEFAULT_PORT: int = 5050
CONNECTION_COUNT: int = 2

class Wifi():
    _type: int
    run: bool = True
    timeout: float = 5.0

    def __init__(self, type_connection: int = 0):
        ''' 
        Модуль подключения по WiFi

            type_connection:    0 - Master,
                                1 - Slave
        '''

        self._type = type_connection

    def connect(self, ip: str, port: int = DEFAULT_PORT) -> socket.socket:
        ''' Функция для подключения к роботу Slave'''
        
        if self._type == 0:
            raise ValueError
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                sock.connect((ip, port))
            
            except Exception as e:
                print(f'Connection failed: {e}')

        return sock

    def stream(
            self, callback_func, port: int = DEFAULT_PORT,
            connection_count: int = CONNECTION_COUNT) -> None:
        ''' Функция для вещания робота Master'''

        if self._type == 1:
            raise ValueError
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                sock.bind(('', port))
                sock.listen(connection_count)
                print("Server is running...\nconnection awaited", end='\r')

                conn, addr = sock.accept()

                while self.run:
                    try:
                        callback_func(conn)
                        print(f'Connection with {addr}:{port} alive')

                    except Exception as e:
                        print(f'Connection with {addr}:{port} disconnect: {e}', end='\r')
                        raise
            
            except Exception as e:
                print(f'Server fatal error: {e}')
                raise
    
    def shutdown(self):
        self.run = False
