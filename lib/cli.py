# lib/cli.py

from models.trainer import Trainer
from models.pokemon import Pokemon
from helpers import (
    exit_program,
    create_trainer,
    delete_trainer,
    trainer_selector,
    update_trainer_name,
    battle_scene,
    delete_trainer_pokemon,
    clear_cli,
    create_pokemon,
    delete_pokemon,
    get_all,
    create_wild_pokemon
)

def main_page():
    print("*********************************************************************")
    print("|                                      ,'                           |")
    print("|    _.----.        ____         ,'  _\\   ___    ___     ____       |")
    print("| _,-'       `.     |    |  /`.   \\,-'    |   \\  /   |   |    \\  |`.|")
    print("|\\      __    \\    '-.  | /   `.  ___    |    \\/    |   '-.   \\ |  ||")
    print("| \\.    \\ \\   |  __  |  |/    ,','_  `.  |          | __  |    \\|  ||")
    print("|   \\    \\/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  ||")
    print("|    \\     ,-'/  /   \\    ,'   | \\/ / ,`.|         /  /   \\  |     ||")
    print("|     \\    \\ |   \\_/  |   `-.  \\    `'  /|  |    ||   \\_/  | |\\    ||")
    print("|      \\    \\ \\      /       `-.`.___,-' |  |/\\  ||\\      /  | |   ||")
    print("|       \\    \\ `.__,'|  |`-._    `|      |__|  \\_| `.__,'|  | |   |||")
    print("|        \\_.-'       |__|    `-._ |              '-.|     '-.| |   ||")
    print("|                                `'                            '-._||")
    print("*********************************************************************")
    print("*                     Team Red Tracker CLI App                      *")
    print("*********************************************************************")
    print("*                 Please choose from the following:                 *")
    print("*********************************************************************")
    print("|                  Press v to View Team's Tracker                   |")
    print("|                  Press c to Create New Pokemon                    |")
    print("|                  Press p to View PokéDex                          |")
    print("|                  Press e to Exit App                              |")
    print("---------------------------------------------------------------------")

def main():
    while True:
        main_page()
        choice = input("> ")
        if choice == "e":
            clear_cli()
            exit_program()
        elif choice == "v":
            clear_cli()
            trainers_main()
        elif choice == "c":
            clear_cli()
            create_pokemon()
        elif choice == "p":
            clear_cli()
            all_pokemon_menu(get_all(Trainer), get_all(Pokemon))
        else:
            clear_cli()
            print("Invalid Choice, Please choose from the following options.")
            main()

def all_pokemon_menu(all_trainers, all_pokemon):
    while True:
        all_pokemon_page(all_trainers, all_pokemon)
        choice = input("> ")
        if choice == "e":
            clear_cli()
            exit_program()
        elif choice == "d":
            clear_cli()
            delete_pokemon(all_trainers, all_pokemon)
        elif choice == "b":
            clear_cli()
            main()
        else:
            clear_cli()
            print("Invalid Choice, Please choose from the following options.")

def all_pokemon_page(all_trainers, all_pokemon):
    print("*********************************************************************")
    print(f"                             POKÉDEX                                ")
    print("*********************************************************************")
    if len(all_pokemon) > 0:
        # Create a dictionary mapping trainer IDs to trainer names
        trainer_dict = {trainer.id: trainer.name for trainer in all_trainers}
        # Iterate through the Pokémon and print their corresponding Trainer if Caught, else Uncaught
        for index, pokemon in enumerate(all_pokemon, start=1):
            trainer_name = trainer_dict.get(pokemon.trainer_id)
            if trainer_name:
                print(f"{index}. {pokemon.name} | {pokemon.pokemon_type} | Trainer: {trainer_name}")
            else:
                print(f"{index}. {pokemon.name} | {pokemon.pokemon_type} | Uncaught")
    else:
        print(f"             No Pokémon Found In The Wild.                      ")
    print("*********************************************************************")
    print("                  Please choose from the following:                  ")
    print("*********************************************************************")
    print("                  Press d to Delete a Pokémon                        ")
    print("                  Press b to Go Back                                 ")
    print("                  Press e to Exit App                                ")
    print("---------------------------------------------------------------------")     

def trainers_menu():
    print("*********************************************************************")
    print("                        Team Red Trainers:                           ")
    for index, trainer in enumerate(get_all(Trainer), start=1):
        print(f"                  {index}. {trainer.name}")
    print("*********************************************************************")
    print("                  Please choose from the following:                  ")
    print("*********************************************************************")
    print("                  Press a to Add New Trainer                         ")
    print("                  Press v to View Trainer's Profile                  ")
    print("                  Press d to Delete a Trainer                        ")
    print("                  Press b to Go Back                                 ")
    print("                  Press e to Exit App                                ")
    print("---------------------------------------------------------------------")

def trainers_main():
    while True:
        trainers_menu()
        choice = input("> ")
        if choice == "b":
            clear_cli()
            main()
        elif choice == "a":
            create_trainer()
        elif choice == "v":
            trainer_selector()
        elif choice == "d":
            delete_trainer()
        elif choice == "e":
            clear_cli()
            exit_program()
        else:
            clear_cli()
            print("Invalid choice, try again")

def trainer_page(trainer):
    print("*********************************************************************")
    print(f"                     TRAINER {trainer.name.upper()}'S PROFILE       ")
    print("*********************************************************************")
    print(f"                     Name: {trainer.name}                   ")
    if len(trainer.pokemon()) > 0:
        print("                     Pokemon Roster:                             ")
        for index, pokemon in enumerate(trainer.pokemon(), start=1):
            print(f"                       {index}. {pokemon.name}              ")
    else:
        print(f"                     No Pokemon in Trainer's Roster             ")
    print("*********************************************************************")
    print("                  Please choose from the following:                  ")
    print("*********************************************************************")
    print("                  Press c to Go Catch Pokemon!                       ")
    print("                  Press r to Release A Pokemon!                      ")
    print("                  Press u to Update Trainer's Name                   ")
    print(f"                  Press v to View Trainer's Pokemon Roster          ")
    print("                  Press b to Go Back                                 ")
    print("                  Press e to Exit App                                ")
    print("---------------------------------------------------------------------")

def trainer_profile(trainer):
    while True:
        trainer_page(trainer)
        choice = input("> ")
        if choice == "b":
            clear_cli()
            trainers_main()
        elif choice == "u":
            update_trainer_name(trainer)
        elif choice == "c":
            trainer_battle_selector(trainer)
        elif choice == "r":
            delete_trainer_pokemon(trainer)
        elif choice == "d":
            delete_trainer()
            trainers_main()
        elif choice == "v":
            clear_cli()
            view_all_pokemon(trainer)
        elif choice == "e":
            clear_cli()
            exit_program()
        else:
            clear_cli()
            print("Invalid choice, try again")

def view_trainer_pokemon(trainer):
    print("*********************************************************************")
    print(f"                        TRAINER {trainer.name.upper()}'S ROSTER     ")
    print("*********************************************************************")
    if len(trainer.pokemon()) > 0:
        num = 1
        for index, pokemon in enumerate(trainer.pokemon(), start=1):
            print(f"                  Pokemon #{num}                            ")
            print(f"                     Name: {pokemon.name}                   ")
            print(f"                     Type: {pokemon.pokemon_type}           ")
            print(f"                     Trainer: {trainer.name}                ")
            num += 1
    print("*********************************************************************")
    print("                  Please choose from the following:                  ")
    print("*********************************************************************")
    print("                  Press b to Go Back                                 ")
    print("                  Press e to Exit App                                ")
    print("---------------------------------------------------------------------")

def view_all_pokemon(trainer):
    clear_cli()
    while True:
        view_trainer_pokemon(trainer)
        choice = input("> ")
        if choice == "b":
            clear_cli()
            trainer_profile(trainer)
        elif choice == "e":
            clear_cli()
            exit_program()
        else:
            clear_cli()
            print("Invalid choice, try again")
            trainer_profile(trainer)

def battle_cli(trainer, wild_pokemon):
    print("*********************************************************************")
    print(f"                    A WILD {wild_pokemon.name.upper()} HAS APPEARED!!!    ")
    print("                                       ,     ,                       ")
    print("                                     (\\____/)                       ")
    print("                                      (_oo_)                         ")
    print("                                        (O)                          ")
    print("                                      __(O)__    \\                   ")
    print("..................................'    \\..'..\\..'./..................\n")
    print(f"             {trainer.name.upper()} WANTS TO FIGHT!   \n")
    print("         /\_/\                                                       ")
    print("        ( o.o )                                                      ")
    print("         > ^ <                                                     \n")
    print("*********************************************************************")
    print("---------------------------------------------------------------------")
    print("|                     Please Choose Your Action:                    |")
    print("|                  1. Fight                2. Run                   |")
    print("---------------------------------------------------------------------")

def trainer_battle_selector(trainer):
    clear_cli()
    if len(trainer.pokemon()) >= 6:
        print(f"Max Roster Capacity Reached!\nRelease a Pokemon From Roster Before Catching Anymore!")
        trainer_profile(trainer)
    else:
        battle_profile(trainer)

def battle_profile(trainer):
    wild_pokemon = create_wild_pokemon()
    battle_cli(trainer, wild_pokemon)
    while True:
        choice = input("> ")
        if choice == "1" or choice == "Fight" or choice == "fight":
            battle_scene(trainer, wild_pokemon)
        elif choice == "2" or choice == "Run" or choice == "run":
            clear_cli()
            print(f"{trainer.name} got away from the wild Pokemon!")
            trainer_profile(trainer)
        else:
            clear_cli()
            print("Invalid choice, try again")
            trainer_profile(trainer)

if __name__ == "__main__":
    clear_cli()
    main()
