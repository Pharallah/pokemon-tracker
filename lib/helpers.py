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
    uncaught_pokemon = [pokemon for pokemon in Pokemon.get_all() if pokemon.trainer_id == 0]
    randomized_pokemon = random.choice(uncaught_pokemon)
    return randomized_pokemon

def return_current_trainer():
    return current_trainer[0]

def view_all_trainers():
    trainers = Trainer.get_all()
    for index, trainer in enumerate(trainers, start=1):
        print(f"                  {index}. {trainer.name}")

def create_trainer():
    from cli import trainers_menu
    name = input("Enter Your New Trainer's Name: ")
    uncaught_pokemon = random_pokemon()

    clear_cli()

    # Filter thru all Trainers 
    trainer_list = [trainer.name.lower() for trainer in Trainer.get_all() if name.lower() == trainer.name.lower()]

    # breakpoint()
    if name.lower() in trainer_list:
        print("That Trainer Name Already Exists, Please Try Again.")
        trainers_menu()
        create_trainer()
    else:
        if isinstance(name, str) and 15 >= len(name) >= 5:
            new_trainer = Trainer.create(name.title())
            uncaught_pokemon.trainer_id = new_trainer.id
            uncaught_pokemon.update()

            clear_cli()

            print(f"{name.title()} Has Joined The Team!")
            print(f"Professor Oak Has Given {new_trainer.name} Their First Pokemon: {uncaught_pokemon.name}")
        else:
            clear_cli()
            print("Please Enter A Name Between 5 And 15 Characters Long: ")
            trainers_menu()
            create_trainer()
        # breakpoint()

    

def delete_trainer():
    from cli import trainers_main
    
    name = input("Enter Trainer's Name to Delete: ")
    trainers = Trainer.get_all()
    lowered_trainers = [trainer.name.lower() for trainer in trainers]

    if name.lower() not in lowered_trainers:
        print("Please Enter Valid Trainer Name. ")
        trainers_main()
    else:
        for trainer in trainers:
            if trainer.name.lower() == name.lower():
                # Deletes Trainer's pokemon from DB before deleting trainer
                for pokemon in trainer.pokemon():
                    pokemon.delete()
                trainer.delete()
            else:
                clear_cli()
                print("No Trainer Found By That Name.")
                trainers_main()

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
        print("Please Enter Valid Trainer Name. Name must be between 5 and 15 characters long.")
        trainer_instance()
    else:
        clear_cli()
        for trainer in all_trainers:
            if trainer.name.lower() == name.lower():
                current_trainer.clear()
                current_trainer.append(trainer)
                return trainer
            

def catch_pokemon(trainer):
    from cli import trainer_profile
    current_pokemon = []
    wild_pokemon = random_pokemon()
    
    
    # Ensures wild_pokemon not already in Trainer's Roster
    if wild_pokemon not in trainer.pokemon():
        wild_pokemon.trainer_id = trainer.id
        wild_pokemon.update()
        current_pokemon.clear()
        current_pokemon.append(wild_pokemon)
    
    # Filter avoids the new pokemon from being chosen to fight itself
    filtered_roster = [p for p in trainer.pokemon() if p != current_pokemon[0]]
    
    # Choose random pokemon from filtered roster to fight
    fighting_pokemon = random.choice(filtered_roster).name
    opp_pokemon = current_pokemon[0].name

    clear_cli()
    
    # Battle Scene Dialogue
    print(f"Battle With A Wild {opp_pokemon} Has Started!!!")
    time.sleep(2)
    print(f"Trainer {trainer.name} Chooses {fighting_pokemon} To Fight {opp_pokemon}!!!")
    time.sleep(2)
    print(f"{opp_pokemon} Attacks!!!")
    time.sleep(2)
    print(f"{fighting_pokemon} Attacks Back And Landed A Critical Hit!")
    time.sleep(2)
    print(f"Trainer {trainer.name} Throws A Pokéball Ball At {opp_pokemon}!")
    
    period = "."
    for _ in range(5):
        print(period)
        period += "."
        time.sleep(1)

    # Create 70% chance of catching the wild Pokemon
    catch_probability = random.random()
    if catch_probability > 0.3:
        clear_cli()
        print(f"Congratulations! {wild_pokemon.name} Has Been Caught!!!")
        trainer_profile(trainer)
    else:
        clear_cli()
        print(f"Oh no! {wild_pokemon.name} Broke Free And Ran Away!")
        wild_pokemon.trainer_id = 0
        wild_pokemon.delete()
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
    main_page()
    valid_types = ["Fire", "Water", "Grass", "Electric"]

    name = input("Enter New Pokemon Name: ").title()
    
    clear_cli()
    main_page()
    
    # Ensures New Pokemon doesn't already exist in DB
    matching_pokemon = [existing_pokemon for existing_pokemon in Pokemon.get_all() if existing_pokemon.name == name]

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
        _all_pokemon = Pokemon.get_all()
        clear_cli()
        print(f"{pokemon_list[0].name.title()} Has Been Deleted!")
        all_pokemon_menu(all_trainers, _all_pokemon)
    else:
        clear_cli()                          
        print(f"Pokémon Name Not Found In The Wild")
        delete_pokemon(all_trainers, all_pokemon)

def exit_program():
    print("Thank You For Playing!")
    exit()