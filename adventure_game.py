import time

def print_pause(message):
    print(message)
    time.sleep(2)

def intro():
    print_pause("You find yourself standing in an open field, filled with "
                "grass and yellow wildflowers.")
    print_pause("Rumor has it that a pirate/gorgon/troll/wicked fairie is "
                "somewhere around here, and has been terrifying the near by "
                "village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) "
                 "dagger.")

intro()
