from models.__init__ import CONN, CURSOR

class Trainer:
    
    all = {}

    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 15 >= len(name) >= 5:
            self._name = name
        else:
            raise ValueError("Please Enter A Name Between 5 And 15 Characters Long.")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS trainers (
            id INTEGER PRIMARY KEY,
            name TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS trainers;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO trainers (name)
            VALUES (?)
        """

        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    @classmethod
    def create(cls, name):
        trainer = cls(name)
        trainer.save()
        return trainer

    def update(self):
        sql = """
            UPDATE trainers
            SET name = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM trainers
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        # Check the dictionary for an existing instance using the row's primary key
        trainer = cls.all.get(row[0])
        if trainer:
            # ensure attributes match row values in case local instance was modified
            trainer.name = row[1]
        else:
            # not in dictionary, create new instance and add to dictionary
            trainer = cls(row[1])
            trainer.id = row[0]
            cls.all[trainer.id] = trainer
        return trainer
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM trainers
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM trainers
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM trainers
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    
    def pokemon(self):
        # Import from here to avoid circular imports (endless loop)
        from models.pokemon import Pokemon
        sql = """
            SELECT * FROM pokemon
            WHERE trainer_id = ?
        """
        CURSOR.execute(sql, (self.id,))

        rows = CURSOR.fetchall()
        return [
            Pokemon.instance_from_db(row) for row in rows
        ]