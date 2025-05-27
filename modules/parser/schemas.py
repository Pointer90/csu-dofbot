from pydantic import BaseModel


class BaseDTO(BaseModel):
    '''
    {
        'target': None / NameModule / NameClass,
        'cmd': 'run',
        'args': []
    }
    '''
    target: None | str = None
    cmd: str
    args: list = []
