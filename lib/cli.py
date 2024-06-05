# lib/cli.py

from helpers import (
    exit_program,
    create_trainer,
    view_all_trainers,
    view_all_pokemon,
    view_trainer_details,
    delete_trainer
)

def main_page():
    print("********************************************")
    print("*         Pokemon Tracker CLI App          *")
    print("********************************************")
    print("     Please choose from the following:    \n")
    print("     Press t to View All Trainers            ")
    print("     Press p to View All Pokemon             ")
    print("     Press e to Exit                         ")
    print("--------------------------------------------")

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
    print("********************************************")
    print("                 Trainers:                  ")
    view_all_trainers()
    print("********************************************")
    print("     Please choose from the following:      ")
    print("     Press a to Add New Trainer             ")
    print("     Press v to View Trainer's Details      ")
    print("     Press d to Delete a Trainer            ")
    print("     Press b to Go Back                     ")
    print("     Press e to Exit                        ")
    print("--------------------------------------------")

def trainers_main():
    while True:
        trainers_menu()
        choice = input("> ")
        if choice == "b":
            main()
        elif choice == "a":
            create_trainer()
        elif choice == "v":
            view_trainer_details()
        elif choice == "d":
            delete_trainer()
            trainers_main()
        elif choice == "e":
            exit()
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
