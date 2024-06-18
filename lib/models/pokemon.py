from models.__init__ import CONN, CURSOR
from models.trainer import Trainer


class Pokemon:
    
    all = {}

    def __init__(self, name, pokemon_type, trainer_id=0, id=None):
        self.id = id
        self.name = name
        self.pokemon_type = pokemon_type
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
        valid_types = ["Fire", "Water", "Grass", "Electric"]
        
        if pokemon_type in valid_types:
            self._pokemon_type = pokemon_type
        else:
            raise ValueError("Please enter valid Pokemon Type: Fire, Water, Electric, or Grass")

    @property
    def trainer_id(self):
        return self._trainer_id

    @trainer_id.setter
    def trainer_id(self, id):
        if isinstance(id, int):
            self._trainer_id = id
        else:
            raise ValueError("Trainer ID must be an integer")
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS pokemon (
            id INTEGER PRIMARY KEY,
            name TEXT,
            pokemon_type TEXT,
            trainer_id INTEGER,
            FOREIGN KEY (trainer_id) REFERENCES trainer(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS pokemon;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO pokemon (name, pokemon_type, trainer_id)
            VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.pokemon_type, self.trainer_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, pokemon_type, trainer_id):
        pokemon = cls(name, pokemon_type, trainer_id)
        pokemon.save()
        return pokemon
    
    def update(self):
        sql = """
            UPDATE pokemon
            SET name = ?, pokemon_type = ?, trainer_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.pokemon_type, self.trainer_id, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM pokemon
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        # Check the dictionary for an existing instance using the row's primary key
        pokemon = cls.all.get(row[0])
        if pokemon:
            # ensure attributes match row values in case local instance was modified
            pokemon.name = row[1]
            pokemon.pokemon_type = row[2]
            pokemon.trainer_id = row[3]
        else:
            # not in dictionary, create new instance and add to dictionary
            pokemon = cls(row[1], row[2], row[3])
            pokemon.id = row[0]
            cls.all[pokemon.id] = pokemon
        return pokemon

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM pokemon
        """

        rows = CURSOR.execute(sql).fetchall()
    
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM pokemon
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM pokemon
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
