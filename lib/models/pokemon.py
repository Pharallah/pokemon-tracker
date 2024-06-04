from models.__init__ import CONN, CURSOR

class Pokemon:
    
    all = {}

    def __init__(self, name, pokemon_type, level=1, trainer_id, id=None):
        self.id = id
        self.name = name
        self.pokemon_type = pokemon_type
        self.level = level
        self.trainer_id = trainer_id
        