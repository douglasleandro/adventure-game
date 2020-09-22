import time

def print_pause(message):
    print(message)
    time.sleep(0)

def intro():
    print_pause("You find yourself standing in an open field, filled with "
                "grass and yellow wildflowers.")
    print_pause("Rumor has it that a pirate/gorgon/troll/wicked fairie is "
                "somewhere around here, and has been terrifying the near by "
                "village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) "
                "dagger.\n")

def valid_input(prompt, opt1, opt2):
    while True:
        option = input(prompt)
        if option == '1':
            return option
        elif option == '2':
            return option
        else:
            return prompt

intro()

print_pause("Enter 1 to knock on the door of the house."
            "Enter 2 to peer into the cave."
            "What would you like to do? ")

while True:

    option = valid_input("(Please enter 1 or 2).\n", '1', '2')

    if option == '1':
        print ("You approach the door of the house.")
        break
    elif option == '2':
        print ("You peer cautiously into the cave. "
               "It turns out to be only a very small cave. "
               "Your eye catches a glint of metal behind a rock."
               "You have found the magical Sword of Ogoroth!"
               "You discard your silly old dagger and take the sword with you."
               "You walk back out to the field.")
        break
    else:
        option = valid_input("(Please enter 1 or 2).\n", '1', '2')
