# lib/helpers.py
from models.trainer import Trainer
from models.pokemon import Pokemon
from pokemon_list import pokemon_list

current_trainer = []


# COMPLETE
def view_all_trainers():
    trainers = Trainer.get_all()
    for index, trainer in enumerate(trainers, start=1):
        print(f"     {index}. {trainer.name}")

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

# def view_trainer_details():
#     number = input("     Select trainer number to view detail: ")
#     trainers = Trainer.get_all()
#     for index, trainer in enumerate(trainers, start=1):
#         if number == index:
#             trainer.pokemon()

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

def post_trainer_update():
    all_trainers = Trainer.get_all()
    for trainer in all_trainers:
        if trainer.name == current_trainer[0].name:
            return trainer
        
def catch_pokemon():
    pass

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

def exit_program():
    print("Goodbye!")
    exit()