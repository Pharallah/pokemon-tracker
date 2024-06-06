from models.trainer import Trainer
from models.pokemon import Pokemon

def seed_database():
    Trainer.drop_table()
    Pokemon.drop_table()
    Trainer.create_table()
    Pokemon.create_table()

    ash_ketchum = Trainer.create("Ash Ketchum")
    misty = Trainer.create("Misty")

    pikachu = Pokemon.create("Pikachu", "Electric", 1)
    charmander = Pokemon.create("Charmander", "Fire", 1)
    bulbasaur = Pokemon.create("Bulbasaur", "Grass", 2)
    squirtle = Pokemon.create("Squirtle", "Water", 2)


seed_database()
print("Seeded!")