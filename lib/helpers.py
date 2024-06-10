# lib/helpers.py
from models.trainer import Trainer
from models.pokemon import Pokemon
from pokemon_list import pokemon_list
import random
import time
import os

current_trainer = []

def clear_cli():
    os.system('cls' if os.name == 'nt' else 'clear')

# Random Pokemon generator from pokemon_list
def random_pokemon():
    randomized_pokemon = random.choice(pokemon_list())
    return randomized_pokemon

def return_current_trainer():
    return current_trainer[0]

def view_all_trainers():
    trainers = Trainer.get_all()
    for index, trainer in enumerate(trainers, start=1):
        print(f"                  {index}. {trainer.name}")

def create_trainer():
    name = input("Enter Your New Trainer's Name: ")
    fresh_pokemon = random_pokemon()

    clear_cli()

    if isinstance(name, str) and 15 >= len(name) >= 5:
        new_trainer = Trainer.create(name.title())
        new_pokemon = Pokemon.create(fresh_pokemon[0], fresh_pokemon[1], new_trainer.id)
        print(f"{name.title()} Has Joined The Team!")
        print(f"Professor Oak Has Given {new_trainer.name} Their First Pokemon: {new_pokemon.name}")
    else:
        print("Please Enter A Name Between 5 And 15 Characters Long: ")
        create_trainer()

def delete_trainer():
    name = input("Enter Trainer's Name to Delete: ")
    trainers = Trainer.get_all()
    lowered_trainers = [trainer.name.lower() for trainer in trainers]

    if name.lower() not in lowered_trainers:
        print("Please Enter Valid Trainer Name. ")
    else:
        for trainer in trainers:
            if trainer.name.lower() == name.lower():
                # Deletes Trainer's pokemon from DB before deleting trainer
                for pokemon in trainer.pokemon():
                    pokemon.delete()
                trainer.delete()
        clear_cli()
        print(f"Trainer {trainer.name} Has Left The Team!")



def update_trainer_name():
    clear_cli()
    if trainer := Trainer.find_by_name(current_trainer[0].name):
        new_name = input("Enter New Name for Trainer: ").title()
        trainer.name = new_name
        trainer.update()
        print(f"Trainer Has Been Renamed To {trainer.name}!")
        
        from cli import trainer_profile
        trainer_profile(trainer)
    else:
        print("Unable To Update Trainer Name At This Time.")

def trainer_instance():
    name = input("Enter Trainer's Name From List: ")
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
    
    # Randomly generate a new wild pokemon not already in Trainer's roster
    if wild_pokemon not in trainer.pokemon():
        new_pokemon = Pokemon.create(wild_pokemon[0], wild_pokemon[1], trainer.id)
        current_pokemon.clear()
        current_pokemon.append(new_pokemon)
    
    # Avoids the new pokemon from being chosen to fight itself
    # Choose random pokemon from filtered roster to fight
    filtered_roster = [p for p in trainer.pokemon() if p != current_pokemon[0]]
    fighting_pokemon = random.choice(filtered_roster)
    opp_pokemon = current_pokemon[0].name
    trainers_chosen_pokemon = fighting_pokemon.name

    clear_cli()
    # Battle Scene Dialogue
    print(f"Battle With A Wild {opp_pokemon} Has Started!!!")
    time.sleep(2)
    print(f"Trainer {trainer.name} Chooses {trainers_chosen_pokemon} To Fight {opp_pokemon}!!!")
    time.sleep(2)
    print(f"{opp_pokemon} Attacks!!!")
    time.sleep(2)
    print(f"{trainers_chosen_pokemon} Attacks Back And Landed A Critical Hit!")
    time.sleep(2)
    print(f"Trainer {trainer.name} Throws A Master Ball At {opp_pokemon}!")
    period = "."
    for _ in range(5):
        print(period)
        period += "."
        time.sleep(1)

    # Create 50/50 chance of catching Pokemon
    catch_probability = random.random()
    if catch_probability > 0.5:
        print(f"Congratulations! {new_pokemon.name} Has Been Caught!!!")
        trainer_profile(trainer)
    else:
        print(f"Oh no! {new_pokemon.name} Broke Free And Ran Away!")
        new_pokemon.delete()
        trainer_profile(trainer)

def delete_trainer_pokemon(trainer):
    from cli import trainer_profile
    # Ensures Trainers can't delete their only Pokemon
    if len(trainer.pokemon()) == 1:
        print(f"Trainers Must Have At Least 1 Pokemon In Their Roster.")
    else:
        target_pokemon = input(f"Enter Pokemon's Name From Roster to Release: ")
        for pokemon in trainer.pokemon():
            if pokemon.name.lower() == target_pokemon.lower():
                pokemon.delete()
                print(f"Released {pokemon.name} Back To The Wild!")
    clear_cli()
    trainer_profile(trainer)

def exit_program():
    print("Thank You For Playing!")
    exit()