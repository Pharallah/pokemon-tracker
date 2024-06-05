# lib/helpers.py
from models.trainer import Trainer
from models.pokemon import Pokemon


def view_all_trainers():
    trainers = Trainer.get_all()
    for index, trainer in enumerate(trainers, start=1):
        print(f"     {index}. {trainer.name}")

def view_all_pokemon():
    pass

def create_trainer():
    name = input("Enter your Trainer name: ")
    if isinstance(name, str) and 15 >= len(name) >= 5:
        Trainer.create(name.capitalize())
        print(f"{name.capitalize()} has joined the team!")
    else:
        print("Please enter a name between 5 and 15 characters long: ")
        create_trainer()

def view_trainer_details():
    number = input("     Select trainer number to view detail: ")
    trainers = Trainer.get_all()
    for index, trainer in enumerate(trainers, start=1):
        if number == index:
            trainer.pokemon()

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
        

    


def exit_program():
    print("Goodbye!")
    exit()
