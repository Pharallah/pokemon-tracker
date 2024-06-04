from models.__init__ import CONN, CURSOR

class Pokemon:
    
    all = {}

    def __init__(self, name, pokemon_type, level=1, trainer_id, id=None):
        self.id = id
        self.name = name
        self.pokemon_type = pokemon_type
        self.level = level
        self.trainer_id = trainer_id

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def pokemon_type(self):
        return self._pokemon_type

    @pokemon_type.setter
    def pokemon_type(self, pokemon_type):
        valid_types = ["Fire", "Water", "Grass"]
        
        if pokemon_type in valid_types:
            self._pokemon_type = pokemon_type
        else:
            raise ValueError("Please enter valid Pokemon Type: Fire, Water, or Grass")