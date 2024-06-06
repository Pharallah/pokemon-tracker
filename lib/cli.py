# lib/cli.py

from helpers import (
    exit_program,
    create_trainer,
    view_all_trainers,
    view_all_pokemon,
    delete_trainer,
    trainer_instance,
    update_trainer_name,
    return_current_trainer,
    catch_pokemon
)

def main_page():
    print("*********************************************************************")
    print("                                      ,'")
    print("    _.----.        ____         ,'  _\\   ___    ___     ____")
    print(" _,-'       `.     |    |  /`.   \\,-'    |   \\  /   |   |    \\  |`.")
    print("\\      __    \\    '-.  | /   `.  ___    |    \\/    |   '-.   \\ |  |")
    print(" \\.    \\ \\   |  __  |  |/    ,','_  `.  |          | __  |    \\|  |")
    print("   \\    \\/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |")
    print("    \\     ,-'/  /   \\    ,'   | \\/ / ,`.|         /  /   \\  |     |")
    print("     \\    \\ |   \\_/  |   `-.  \\    `'  /|  |    ||   \\_/  | |\\    |")
    print("      \\    \\ \\      /       `-.`.___,-' |  |/\\  ||\\      /  | |   |")
    print("       \\    \\ `.__,'|  |`-._    `|      |__|  \\_| `.__,'|  | |   |")
    print("        \\_.-'       |__|    `-._ |              '-.|     '-.| |   |")
    print("                                `'                            '-._|")
    print("*********************************************************************")
    print("*                     Pokemon Tracker CLI App                       *")
    print("*********************************************************************")
    print("                  Please choose from the following:              \n")
    print("                  Press t to View All Trainers                     ")
    print("                  Press p to View All Pokemon                      ")
    print("                  Press e to Exit                                  ")
    print("---------------------------------------------------------------------")

def main():
    while True:
        main_page()
        choice = input("> ")
        if choice == "e":
            exit_program()
        elif choice == "t":
            trainers_main()
        elif choice == "p":
            view_all_pokemon()
        else:
            print("Invalid choice")

def trainers_menu():
    print("*********************************************************************")
    print("                              Trainers:                              ")
    view_all_trainers()
    print("*********************************************************************")
    print("                  Please choose from the following:                  ")
    print("                  Press a to Add New Trainer                         ")
    print("                  Press v to View Trainer's Details                  ")
    print("                  Press d to Delete a Trainer                        ")
    print("                  Press b to Go Back                                 ")
    print("                  Press e to Exit                                    ")
    print("---------------------------------------------------------------------")

def trainers_main():
    while True:
        trainers_menu()
        choice = input("> ")
        if choice == "b":
            main()
        elif choice == "a":
            create_trainer()
        elif choice == "v":
            trainer_selector()
        elif choice == "d":
            delete_trainer()
            trainers_main()
        elif choice == "e":
            exit()
        else:
            print("Invalid choice, try again")
            trainers_main()


def trainer_page(trainer):
    print("*********************************************************************")
    print("                           Trainer Details                           ")
    print("*********************************************************************")
    print(f"                     Trainer Name: {trainer.name}                   ")
    if len(trainer.pokemon()) > 0:
        print("                     Pokemon Roster:                             ")
        for index, pokemon in enumerate(trainer.pokemon(), start=1):
            print(f"                       {index}. {pokemon.name}            ")
    else:
        print(f"                     No Pokemon in Trainer's Roster             ")
    print("*********************************************************************")
    print("                  Please choose from the following:                  ")
    print("                  Press u to Update Trainer's Name                   ")
    print("                  Press c to Go Catch Pokemon!                       ")
    print("                  Press b to Go Back                                 ")
    print("                  Press e to Exit                                    ")
    print("---------------------------------------------------------------------")

def trainer_selector():
    trainer = trainer_instance()
    trainer_profile(trainer)

def trainer_profile(trainer):
    trainer_page(trainer)
    while True:
        choice = input("> ")
        if choice == "b":
            trainers_main()
        elif choice == "u":
            update_trainer_name()
        elif choice == "c":
            trainer_battle_selector()
        elif choice == "d":
            delete_trainer()
            trainers_main()
        elif choice == "e":
            exit()
        else:
            print("Invalid choice, try again")
            trainers_main()

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
    trainer = return_current_trainer()
    if len(trainer.pokemon()) >= 6:
        print(f"{trainer.name}'s Roster is Full!\nRelease a Pokemon From Roster Before Catching Anymore!")
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
            print(f"{trainer.name} got away from the wild Pokemon!")
            trainer_profile(trainer)
        else:
            print("Invalid choice, try again")
            trainer_profile(trainer)

if __name__ == "__main__":
    main()
