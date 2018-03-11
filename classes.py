from player import Position

class Obj(object):
    def __init__(self,dict):
        self.position=Position(dict['position'])
        self.type=dict['type']
        self.dict=dict
        self.id=dict['id']





