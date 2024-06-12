# Pokémon Trainer CLI Application

## Overview

The Pokémon Trainer CLI Application is a text-based simulation game where users can interact with a command-line interface (CLI) to manage their Pokémon trainer profiles, catch wild Pokémon, and engage in simulated battles. The game explores the one-to-many relationship between Trainers and Pokémon, where each trainer can have multiple Pokémon, but each Pokémon belongs to only one trainer.

## Features

- **Trainer Management**: Create and manage Pokémon trainers.
- **Catch Wild Pokémon**: Encounter and attempt to catch wild Pokémon with a 70/30 chance of success.
- **Battle Simulation**: Engage in simulated battles with a randomly generated Pokémon from the Wild using a random Pokémon from the Trainer's Pokémon roster.
- **Suspenseful Catching Animation**: Experience a suspenseful animation when attempting to catch a wild Pokémon.
- **Viewing the Pokédex**: Gotta catch em all! Track your progress by viewing all the Pokémon out in the wild to see which ones are already caught, by which Trainer, and which are yet to have been caught.

## Example Function

`catch_pokemon()`

Simulates an encounter with a wild Pokémon, where the trainer can attempt to catch it. If successful, the Pokémon is added to the trainer's roster. If not, the Pokémon runs away.

```python
def catch_pokemon(trainer):
    from cli import trainer_profile
    wild_pokemon = random_pokemon()
    current_pokemon = []
    
    # Randomly generate a new wild pokemon not already in Trainer's roster
    if wild_pokemon not in trainer.pokemon():
        new_pokemon = Pokemon.create(wild_pokemon[0], wild_pokemon[1], trainer.id)
        current_pokemon.clear()
        current_pokemon.append(new_pokemon)
    
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
        print(f"Congratulations! {new_pokemon.name} Has Been Caught!!!")
        trainer_profile(trainer)
    else:
        print(f"Oh no! {new_pokemon.name} Broke Free And Ran Away!")
        new_pokemon.delete()
        trainer_profile(trainer)
```

## Requirements

No additional packages are required beyond the Python standard library.

## Installation/Setup

Clone the repository and navigate to the project directory. 

## Usage
Run the following code to start the CLI application:

```sh
python lib/cli.py
```
## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for review.

## Ideas for Improvement

1. Pokémon Leveling System: Implement a leveling system for Pokémon that allows them to gain experience points and level up after battles.

2. Battle Mechanics: Add more detailed battle mechanics, such as different types of attacks, special abilities, and health points (HP) for Pokémon.

3. Trainer Customization: Allow users to customize their trainers with different attributes and items.

4. Pokédex Feature: Implement a Pokédex that keeps track of all the Pokémon a trainer has encountered and caught.

5. Multiplayer Mode: Develop a multiplayer mode where trainers can battle against each other over a network.

## Contact
For any questions or feedback, please contact harrycsanjuan@gmail.com