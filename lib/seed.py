from models.trainer import Trainer
from models.pokemon import Pokemon
from pokemon_list import pokemon_list

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

    for monster in pokemon_list():
        Pokemon.create(monster[0], monster[1], 0)

seed_database()
print("Seeded!")