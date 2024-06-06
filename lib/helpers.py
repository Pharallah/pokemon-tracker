# lib/helpers.py
from models.trainer import Trainer
from models.pokemon import Pokemon
from pokemon_list import pokemon_list
import random
import time

current_trainer = []

def return_current_trainer():
    return current_trainer[0]

def random_pokemon():
    randomized_pokemon = random.choice(pokemon_list())
    return randomized_pokemon
    # generate random pokemon to be created
    # return it to 

# COMPLETE
def view_all_trainers():
    trainers = Trainer.get_all()
    for index, trainer in enumerate(trainers, start=1):
        print(f"                  {index}. {trainer.name}")

def view_all_pokemon():
    pass

# COMPLETE
def create_trainer():
    name = input("Enter your Trainer name: ")

    if isinstance(name, str) and 15 >= len(name) >= 5:
        Trainer.create(name.title())
        print(f"{name.title()} has joined the team!")
    else:
        print("Please enter a name between 5 and 15 characters long: ")
        create_trainer()

# COMPLETE
def delete_trainer():
    name = input("Enter Trainer's Name to Delete: ")
    trainers = Trainer.get_all()
    lowered_trainers = [trainer.name.lower() for trainer in trainers]

    if name.lower() not in lowered_trainers:
        print("Please Enter Valid Trainer Name: ")
    else:
        for trainer in trainers:
            if trainer.name.lower() == name.lower():
                trainer.delete()
                print(f"{trainer.name} Has Been Deleted!")


def update_trainer_name():
    if trainer := Trainer.find_by_name(current_trainer[0].name):
        new_name = input("Enter New Name for Trainer: ").title()
        trainer.name = new_name
        trainer.update()
        print(f"Trainer has been renamed to {trainer.name}!")
        
        from cli import trainer_profile
        trainer_profile(trainer)
    else:
        print("Unable to update Trainer name at this time.")
        

# COMPLETE
def trainer_instance():
    name = input("Enter Trainer's Name from List: ")
    all_trainers = Trainer.get_all()
    lowered_trainers = [trainer.name.lower() for trainer in all_trainers]

    if name.lower() not in lowered_trainers:
        print("Please Enter Valid Trainer Name: ")
    else:
        for trainer in all_trainers:
            if trainer.name.lower() == name.lower():
                current_trainer.clear()
                current_trainer.append(trainer)
                return trainer

def catch_pokemon(trainer):
    from cli import trainer_profile
    wild_pokemon = random_pokemon()
    current_pokemon = []
    

    # Randomly generate a wild pokemon
    if wild_pokemon not in trainer.pokemon():
        new_pokemon = Pokemon.create(wild_pokemon[0], wild_pokemon[1], trainer.id)
        current_pokemon.clear()
        current_pokemon.append(new_pokemon)

    # Choose random pokemon from trainer's roster to fight
    fighting_pokemon = random.choice(trainer.pokemon())
    opp_pokemon = current_pokemon[0].name
    trainers_chosen_pokemon = fighting_pokemon.name

    # Battle Scene Dialogue
    print(f"Battle with {opp_pokemon} has started!!!")
    time.sleep(2)
    print(f"Trainer {trainer.name} Chooses {trainers_chosen_pokemon} To Fight {opp_pokemon}!!!")
    time.sleep(2)
    print(f"{opp_pokemon} attacks!!!")
    time.sleep(2)
    print(f"{trainers_chosen_pokemon} Landed A Critical Hit!")
    time.sleep(2)
    print(f"{trainer.name} Throws a Master Ball at {opp_pokemon}!")
    period = "."
    for _ in range(5):
        print(period)
        period += "."
        time.sleep(1)

    # Create 50/50 chance of catching Pokemon
    catch_probability = random.random()
    if catch_probability > 0.5:
        print(f"{new_pokemon.name} has been caught!!!")
        trainer_profile(trainer)
    else:
        print(f"Oh no! {new_pokemon.name} broke free and ran away!")
        new_pokemon.delete()
        trainer_profile(trainer)

def exit_program():
    print("Thank you for playing!")
    exit()