from models.__init__ import CONN, CURSOR
from models.trainer import Trainer


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

    @property
    def trainer_id(self):
        return self._trainer_id

    @trainer_id.setter
    def trainer_id(self, id):
        if type(id) is int and Trainer.find_by_id(id):
            self._trainer_id = id
        else:
            raise ValueError("Trainer ID must reference a trainer in the database")
    
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Department instances """
        sql = """
            CREATE TABLE IF NOT EXISTS pokemon (
            id INTEGER PRIMARY KEY,
            name TEXT,
            type TEXT,
            level INTEGER,
            trainer_id INTEGER,
            FOREIGN KEY (trainer_id) REFERENCES trainer(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Department instances """
        sql = """
            DROP TABLE IF EXISTS pokemon;
        """
        CURSOR.execute(sql)
        CONN.commit()