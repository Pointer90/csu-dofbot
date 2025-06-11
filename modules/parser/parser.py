from .schemas import BaseDTO
import importlib


class Parser():
    '''
    {
        'target': None / NameModule / NameClass,
        'cmd': 'run',
        'args': []
    }
    '''

    def send(self, data: BaseDTO):
        return data.model_dump_json().encode('utf-8')

    def excute(self, data: bytes):
        data: BaseDTO = BaseDTO.model_validate_json(data.decode('utf-8'))
        # data = json.loads(data.decode('utf-8'))

        module = importlib.import_module(data.target)

        exec = getattr(module, data.cmd)
        return exec, data.args

        # exec(*data.args) if data.args else exec()
