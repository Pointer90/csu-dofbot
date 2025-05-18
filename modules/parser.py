import json

class Parser():
    '''
    {
        'target': None / NameModule / NameClass,
        'cmd': 'run',
        'args': []
    }
    '''

    def send(data: dict):
        return json.dumps(data)

    def excute(data):
        data = json.loads(data)

        if data['target']:
            exec = getattr(data['target'], data['cmd'])
        else:
            exec = globals()[data['cmd']]
            
        exec(*data['args']) if data['args'] else exec()
