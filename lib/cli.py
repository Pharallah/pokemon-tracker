# lib/cli.py

from helpers import (
    exit_program,
    create_trainer,
    view_all_trainers,
    delete_trainer,
    trainer_instance,
    update_trainer_name,
    return_current_trainer,
    catch_pokemon,
    delete_trainer_pokemon,
    clear_cli
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
        else:
            clear_cli()
            print("Invalid Choice, Please choose from the following options.")
            main()
            

def trainers_menu():
    print("*********************************************************************")
    print("                        Team Red Trainers:                           ")
    view_all_trainers()
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
    trainers_menu()
    while True:
        choice = input("> ")
        if choice == "b":
            clear_cli()
            main()
        elif choice == "a":
            create_trainer()
            trainers_main()
        elif choice == "v":
            trainer_selector()
        elif choice == "d":
            delete_trainer()
            trainers_main()
        elif choice == "e":
            clear_cli()
            exit_program()
        else:
            clear_cli()
            print("Invalid choice, try again")
            trainers_main()
            


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

def trainer_selector():
    trainer = trainer_instance()
    # clear_cli()
    trainer_profile(trainer)

def trainer_profile(trainer):
    trainer_page(trainer)
    while True:
        choice = input("> ")
        if choice == "b":
            clear_cli()
            trainers_main()
        elif choice == "u":
            update_trainer_name()
        elif choice == "c":
            trainer_battle_selector()
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
            trainer_profile(trainer)

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
    view_trainer_pokemon(trainer)
    while True:
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

def battle_cli(trainer):
    print("*********************************************************************")
    print(f"                         {trainer.name.upper()} WANTS TO FIGHT!   \n")
    print("                                       ,     ,                       ")
    print("                                     (\\____/)                       ")
    print("                                      (_oo_)                         ")
    print("                                        (O)                          ")
    print("                                      __||__    \\)                  ")
    print("..................................'    \\..'..\\..'./..................\n")
    print("          AN UNKNOWN POKEMON HAS APPEARED!!!                       \n")
    print("         /\_/\                                                       ")
    print("        ( o.o )                                                      ")
    print("         > ^ <                                                     \n")
    print("*********************************************************************")
    print("---------------------------------------------------------------------")
    print("|                     Please Choose Your Action:                    |")
    print("|                  1. Fight                2. Run                   |")
    print("---------------------------------------------------------------------")

def trainer_battle_selector():
    clear_cli()
    trainer = return_current_trainer()
    if len(trainer.pokemon()) >= 6:
        print(f"Max Roster Capacity Reached!\nRelease a Pokemon From Roster Before Catching Anymore!")
        trainer_profile(trainer)
    else:
        battle_profile(trainer)

def battle_profile(trainer):
    battle_cli(trainer)
    while True:
        choice = input("> ")
        if choice == "1" or choice == "Fight" or choice == "fight":
            catch_pokemon(trainer)
        elif choice == "2" or choice == "Run" or choice == "run":
            clear_cli()
            print(f"{trainer.name} got away from the wild Pokemon!")
            trainer_profile(trainer)
        else:
            clear_cli()
            print("Invalid choice, try again")
            trainer_profile(trainer)

if __name__ == "__main__":
    main()
