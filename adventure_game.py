import time
import random

monsters = ['pirate', 'gorgon', 'troll', 'wicked fairie']


def print_pause(message):
    print(message)
    time.sleep(2)


def intro(monster):
    print_pause("You find yourself standing in an open field, filled with "
                "grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {monster} is "
                "somewhere around here, and has been terrifying the near by "
                "village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) "
                "dagger.\n")


def valid_input(prompt, opt1, opt2):
    while True:
        response = input(prompt)
        if response == opt1:
            break
        elif response == opt2:
            break
    return response


def field():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")


def house(item, monster):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out steps a "
                f"{monster}.")
    print_pause(f"Eep! This is the {monster}'s house!")
    print_pause(f"The {monster} attacks you!")
    if "sword" in item:
        option = valid_input("Would you like to (1) fight or (2) run away?",
                             "1", "2")
        if option == "1":
            print_pause(f"As the {monster} moves to "
                        "attack, you unsheath your new sword.")
            print_pause("The Sword of Ogoroth shines brightly in your hand as "
                        "you brace yourself for the attack.")
            print_pause(f"But the {monster} takes one "
                        "look at your shiny new toy and runs away!")
            print_pause(f"You have rid the town of the {monster}. You are "
                        "victorious!")
        elif option == "2":
            print_pause("You run back into the field. Luckily, you don't seem "
                        "to have been followed.\n")
            field()
            main(item)
    else:
        print_pause("You feel a bit under-prepared for this, what with only "
                    "having a tiny dagger.")
        option = valid_input("Would you like to (1) fight or (2) run away?",
                             "1", "2")
        if option == "1":
            print_pause("You do your best...")
            print_pause("but your dagger is no match for the "
                        f"{monster}.")
            print_pause("You have been defeated!")
        elif option == "2":
            print_pause("You run back into the field. Luckily, you don't seem "
                        "to have been followed.\n")
            field()
            main(item, monster)


def cave(item, monster):
    if "sword" in item:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all the good stuff. "
                    "It's just an empty cave now.")
        print_pause("You walk back out to the field.\n")
        field()
        main(item, monster)
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take the sword "
                    "with you.")
        item.append("sword")
        print_pause("You walk back out to the field.\n")
        field()
        main(item, monster)


def main(item, monster):
    option = valid_input("What would you like to do? \n"
                         "(Please enter 1 or 2).\n", "1", "2")
    if option == "1":
        house(item, monster)
    elif option == "2":
        cave(item, monster)


def play_again():
    option = valid_input("Would you like to play again? (y/n)", "y", "n")
    if option == "y":
        print_pause("Excellent! Restarting the game ... \n")
        play_game()
    elif option == "n":
        print_pause("Thanks for playing! See you next time.")


def play_game():
    item = []
    monster = random.choice(monsters)
    intro(monster)
    field()
    main(item, monster)
    play_again()


play_game()
