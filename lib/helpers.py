# lib/helpers.py
from models.trainer import Trainer
from models.pokemon import Pokemon
import random
import time
import os

def clear_cli():
    os.system('cls' if os.name == 't' else 'clear')

# Random Pokemon generator from pokemon_list
def random_pokemon():
    # Ensures random Pokemon is an Uncaught / Without a Trainer
    uncaught_pokemon = [pokemon for pokemon in Pokemon.get_all() if pokemon.trainer_id == 0]
    randomized_pokemon = random.choice(uncaught_pokemon)
    return randomized_pokemon

def get_all(model):
    if model == Trainer:
        all_trainers = Trainer.get_all()
        return all_trainers
    elif model == Pokemon:
        all_pokemon = Pokemon.get_all()
        return all_pokemon

def create_trainer():
    from cli import trainers_menu
    name = input("Enter Your New Trainer's Name: ").title()
    uncaught_pokemon = random_pokemon()

    clear_cli()

    # Checks input from existing Trainer in DB
    # Walrus operator assigns & returns the value of expression concurrently
    if trainer_in_db:= Trainer.find_by_name(name):
        print("That Trainer Name Already Exists, Please Try Again.")
        trainers_menu()
        create_trainer()
    else:
        try:
            new_trainer = Trainer.create(name.title())
            uncaught_pokemon.trainer_id = new_trainer.id
            uncaught_pokemon.update()

            clear_cli()

            print(f"{name.title()} Has Joined The Team!")
            print(f"Professor Oak Has Given {new_trainer.name} Their First Pokemon: {uncaught_pokemon.name}")
        except:
            clear_cli()
            print("Please Enter A Name Between 5 And 15 Characters Long. ")
            trainers_menu()
            create_trainer()

def delete_trainer():
    from cli import trainers_main
    name = input("Enter Trainer's Name to Delete: ").title()

    # Checks if input is doesn't exist in the DB
    if Trainer.find_by_name(name) == None:
        print("Please Enter Valid Trainer Name. ")
        trainers_main()
    else:
        for trainer in get_all(Trainer):
            if trainer.name == name:
                # Resets trainer's pokemon trainer_id to 0
                for pokemon in trainer.pokemon():
                    pokemon.trainer_id = 0
                    pokemon.update()
                trainer.delete()
                print(f'{trainer.name} Has Left The Team!')
                break # Stops loop once matching trainer is found & deleted
        else:
            # breakpoint()
            clear_cli()
            print("No Trainer Found By That Name.")
            trainers_main()
            
        clear_cli()
        print(f"Trainer {trainer.name} Has Left The Team!")

def update_trainer_name(trainer):
    from cli import trainer_page, trainer_profile
    
    clear_cli()
    trainer_page(trainer)

    # Checks if the current Trainer actually exists in the DB
    if trainer := Trainer.find_by_name(trainer.name):
        new_name = input("Enter New Name for Trainer: ").title()
        trainer.name = new_name
        trainer.update()
        
        clear_cli()
        
        print(f"Trainer Has Been Renamed To {trainer.name}!")
        trainer_profile(trainer)
    else:
        print("Cannot Update Trainer. Trainer Doesn't Exist.")

def trainer_selector():
    from cli import trainer_profile
    name = input("Enter Trainer's Name From List: ").title()
    
    # Checks user input against DB & returns Trainer object with matching name
    if Trainer.find_by_name(name):
        clear_cli()
        for trainer in get_all(Trainer):
            if trainer.name == name:
                trainer_profile(trainer)
    else:
        print("Please Enter Valid Trainer Name From The List Above.")
        trainer_selector() # Rerun method
        
def create_wild_pokemon(trainer):
    wild_pokemon = random_pokemon()
    return wild_pokemon

def battle_scene(trainer, wild_pokemon):
    from cli import trainer_profile
    # Filter avoids the new pokemon from being chosen to fight itself
    filtered_roster = [p for p in trainer.pokemon() if p != wild_pokemon]
    # Choose random pokemon from filtered roster to fight
    chosen_pokemon = random.choice(filtered_roster).name

    clear_cli()
    
    # Battle Scene Dialogue
    print(f"Battle With A Wild {wild_pokemon.name} Has Started!!!")
    time.sleep(2)
    print(f"Trainer {trainer.name} Chooses {chosen_pokemon} To Fight {wild_pokemon.name}!!!")
    time.sleep(2)
    print(f"{wild_pokemon.name} Attacks!!!")
    time.sleep(2)
    print(f"{chosen_pokemon} Attacks Back And Landed A Critical Hit!")
    time.sleep(2)
    print(f"Trainer {trainer.name} Throws A Pokéball Ball At {wild_pokemon.name}!")
    
    period = "."
    for _ in range(5):
        print(period)
        period += "."
        time.sleep(1)

    # Create 70% chance of catching the wild Pokemon
    catch_probability = random.random()
    if catch_probability > 0.3:
        wild_pokemon.trainer_id = trainer.id
        wild_pokemon.update()
        clear_cli()
        print(f"Congratulations! {wild_pokemon.name} Has Been Caught!!!")
        trainer_profile(trainer)
    else:
        clear_cli()
        print(f"Oh no! {wild_pokemon.name} Broke Free And Ran Away!")
        trainer_profile(trainer)

def delete_trainer_pokemon(trainer):
    from cli import trainer_profile
    # Ensures Trainers can't delete their only Pokemon
    if len(trainer.pokemon()) == 1:
        clear_cli()
        print(f"Trainers Must Have At Least 1 Pokemon In Their Roster To Fight With!")
        trainer_profile(trainer)
    else:
        target_pokemon = input(f"Enter Pokemon's Name From Roster to Release: ")
        
        clear_cli()
        
        trainers_pokemon = [p.name.lower() for p in trainer.pokemon()]

        if target_pokemon.lower() in trainers_pokemon:
            for pokemon in trainer.pokemon():
                if pokemon.name.lower() == target_pokemon.lower():
                    pokemon.trainer_id = 0
                    pokemon.update()
                    print(f"Released {pokemon.name} Back To The Wild!")
        else:
            print(f"No Pokemon By That Name Found. Please Try Again.")
        
        trainer_profile(trainer)
    
    trainer_profile(trainer)

def create_pokemon():
    from cli import main_page, main
    valid_types = ["Fire", "Water", "Grass", "Electric"]

    main_page()

    name = input("Enter New Pokemon Name: ").title()
    
    clear_cli()
    main_page()
    
    # Ensures New Pokemon doesn't already exist in DB
    matching_pokemon = [existing_pokemon for existing_pokemon in get_all(Pokemon) if existing_pokemon.name == name]

    if len(matching_pokemon) == 0:
        pokemon_type = input("Fire | Water | Electric | Grass\nChoose Your New Pokemon's Type From Above: ").title()
        if pokemon_type in valid_types:
            if 3 <= len(name) <= 10:
                clear_cli()
                new_pokemon = Pokemon.create(name, pokemon_type, 0)
                print(f"Congratulations! {new_pokemon.name} Has Been Created And Released To The Wild!")
                main()
            else:
                clear_cli()
                print("Invalid Entry. Pokemon Name Must Be Between 3 And 10 Characters Long")
                create_pokemon()
        else:
            clear_cli()
            print("Invalid Pokemon Type. Please Try Again.")
            create_pokemon()
    else:
        clear_cli()
        print(f"A Pokemon With That Name Already Exists In The Wild. Please Create A Unique Pokemon.")
        create_pokemon()

def delete_pokemon(all_trainers, all_pokemon):
    from cli import all_pokemon_page, all_pokemon_menu
    all_pokemon_page(all_trainers, all_pokemon)
    
    pokemon_name = input("Enter Pokémon Name To Delete: ").lower()
    pokemon_list = [pokemon for pokemon in all_pokemon if pokemon_name == pokemon.name.lower()]
    

    if len(pokemon_list) > 0:
        pokemon_list[0].delete()
        clear_cli()
        print(f"{pokemon_list[0].name.title()} Has Been Deleted!")
        all_pokemon_menu(all_trainers, get_all(Pokemon))
    else:
        clear_cli()                          
        print(f"Pokémon Name Not Found In The Wild")
        delete_pokemon(all_trainers, all_pokemon)

def exit_program():
    print("Thank You For Playing!")
    exit()