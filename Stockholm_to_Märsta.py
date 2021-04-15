# This is the video-game called "Stockholm to Märsta". It is a resource management, rougelike game where a player must
# survive the journey between the cities "Stockholm" and "Märsta" on train. In order to survive the journey the player
# must make sure that his/her food supply doesn't empty as well as deal with the random events that occur at every train
# station between Stockholm and Märsta.



# These are the packages we need to run the game
import random
from IPython.display import clear_output


def tåg(x):

    '''
    This function receives an element from the 'tågstationer' list in the form of a string, the string correpsonds to a train station. Using this argument the function returns the next train station in the list.
    '''
    ind_stn = tågstationer.index(x)
    return tågstationer[ind_stn+1]

def check_if_dead(mat):
    '''This function check the player's current supply of food. It takes the current food value as argument and if 
    it is 0 or less than zero the function returns a 0, otherwise it returns a 1.'''
    if mat<=0:
        return 0
    else:
        return 1

def check_if_märsta(current_stn):
    '''This function wokrs similar to the check_if_dead function. It takes the current train station as argument and check if
    it is Märsta. If it is the function returns a 1, otherwise returns a 0.'''
    if current_stn == "Märsta":
        return 1
    else:
        return 0

def state_of_play():
    '''This function display the relevant information a player would need.
    1) The current train station
    2) The current food supply
    3) The list of items'''
    print(f"You are at the following station: {current_stn}")
    print(f"You have this many units of food left: {mat}")
    print(f"You have the following items in your inventory list: {inventory}")

def event_picker():
    '''This function first generates a random number between all the index positions of the list 'lst_events'. Then it uses the
    .pop() method to remove that element from the list and returns it. Effectively this means that event_picker chooses an
    event at random and makes sure that the same event cannot be chosen again.'''
    rand_numb=random.randint(0, len(lst_events)-1)
    return lst_events.pop(rand_numb)()

def mat_diff(x):
    '''This function decides the initial food value that the game will use. Depending on player input (the argument) the
    function will return either 8, 6 or 4 which corresponds to easy, medium and hard versions of the game.'''
    if x.lower().startswith("e"):
        return 8
    elif x.lower().startswith("m"):
        return 6
    elif x.lower().startswith("h"):
        return 4
    
    
# The following functions all correspond to the events that can occur on the journey. Note that not all events will be
# shown in any given game but instead a random number between 1-10 (depending on how many stations) the player sees in
# any given game.

# All the functions follow a similar pattern:
# 1) The functions tells the player which station he/she arrives to as well as what they encounter there.
# 2) The functions generate a text menu using the print_menu function with at least two options (this changes from
# function to function).
# 3) The function creates a while loop where the player must choose an option. If the option doesn't exist in the menu
# the function will display an error message and the player doesn't leave the loop.
# 4) Depending on the choice made by the player, the function will print the consequences of said choice and return two
# objects. The first is an integer which correspond to the change in food due to the event. Note that the default always
# is -1 since it cost one food to reach the event in the first place. The second object is a string that can be empty. If
# it is non-empty it correponds to an item the player received.


# event nr 1
def event_ica_good():
    print("")
    print(f"You arrive at {current_stn}. You see an 'ICA'.\n")
    
    def print_menu():
        print (25 * "-" , "What do you do?" , 25 * "-")
        print ("1. I scavange for food")
        print ("2. I chill for a bit")
        print (67 * "-")
    loop=True
    while loop:
        print_menu()
        loopy=True
        while loopy:
            choice = input("Enter your choice [1-2]: ")
            print("")
            try:
                choice=int(choice)
                loopy=False
            except:
                print("Error: Wrong option selection.\n")
        if choice<1:
            print("Error: Wrong option selection.\n")
        elif choice>2:     
            print("Error: Wrong option selection.\n")
        else:
            loop=False
    
    if choice == 1:
        print("You find some additional food on your journey! You now have more food than what you had when you got here: ")
        print("Food +3")
        print("")
        return 2, ""
    elif choice == 2:
        print("You're being a lazy bastard and just waste food:")
        print("")
        return -1, ""
    
# event nr 2
def event_ica_bad():
    print("")
    print(f"You arrive at {current_stn}. You see an 'ICA'.\n")
    
    def print_menu():
        print (25 * "-" , "What do you do?" , 25 * "-")
        print ("1. I scavange for food")
        print ("2. I chill for a bit")
        print (67 * "-")
    loop=True
    while loop:
        print_menu()
        loopy=True
        while loopy:
            choice = input("Enter your choice [1-2]: ")
            print("")
            try:
                choice=int(choice)
                loopy=False
            except:
                print("Error: Wrong option selection.\n")
        if choice<1:
            print("Error: Wrong option selection.\n")
        elif choice>2:     
            print("Error: Wrong option selection.\n")
        else:
            loop=False
    
    if choice == 1 and "Weapon" in inventory:
        print("Oh no! The ICA was overrun by zombies! You use your weapon to clear the place out before finding food:")
        print("Food +3")
        print("")
        return 2, ""
    elif choice == 1 and "Human Companion" in inventory:
        print("Oh no! The ICA was overrun by zombies! Your friend sacrifices themselves for you:")
        print("Item lost: Human companion")
        print("Gained item: Zombie Companion")
        print("Food +1")
        print("")
        return 0, "Zombie Companion"
    elif choice == 1:
        print("Oh no! The ICA was overrun by zombies! They bite you:")
        print("Gained item: Zombie Bite")
        print("")
        return -1, "Zombie Bite"
    elif choice == 2:
        print("You're being a lazy bastard and just waste food:")
        print("")
        return -1, ""
    
# event nr 3
def event_dog_follower():
    print("")
    print(f"You arrive at {current_stn}. You see a scary looking dog.\n")
    
    def print_menu():
        print (25 * "-" , "What do you do?" , 25 * "-")
        print ("1. I try to win over its trust with 1 unit of food")
        print ("2. I stay the hell away from it")
        print ("3. [If you have the 'Weapon' item] I'm hungry, desperate and the dog is made of food...")
        print (67 * "-")
    loop=True
    while loop:
        print_menu()
        loopy=True
        while loopy:
            choice = input("Enter your choice [1-3]: ")
            print("")
            try:
                choice=int(choice)
                loopy=False
            except:
                print("Error: Wrong option selection.\n")
        if choice<1:
            print("Error: Wrong option selection.\n")
        elif choice>3:     
            print("Error: Wrong option selection.\n")
        elif choice==1 and mat<1:
            print("You don't have enough food available!")
        elif choice==3 and "Weapon" not in inventory:
            print("You don't have that item!")
        else:
            loop=False
    
    if choice == 1:
        print("You squat down and raise your fist towards the dog filled with food. It approaches you carefully but starts munching on the food as soon as it smells it. I think you just made a friend for life:")
        print("Gained item: Dog Companion")
        print("")
        return -2, "Dog Companion"
    elif choice == 2:
        print("Better not take any chances with this doggy:")
        print("")
        return -1, ""
    elif choice == 3:
        print("The fight is short but bloody. You can eat tonight, but at what cost?:")
        print("Food +1")
        print("")
        return 0, ""
    
# event nr 4
def event_food_merchant():
    print("")
    print(f"You arrive at {current_stn}. You see a stall where a merchant trades items for food.\n")
    
    def print_menu():
        print (25 * "-" , "What do you do?" , 25 * "-")
        print ("1. I buy the 'Weapon' item for 2 units of food")
        print ("2. I buy the 'Super Train Fuel' item for 4 units of food ")
        print ("3. I buy the 'Zombie Bite Antidote' item for 1 units of food ")
        print ("4. [If you have the 'Weapon' item] I yell 'This is a robbery! Give me everything you own!' ")
        print ("5. I ignore the merchant.")
        print (67 * "-")
    loop=True
    while loop:
        print_menu()
        loopy=True
        while loopy:
            choice = input("Enter your choice [1-5]: ")
            print("")
            try:
                choice=int(choice)
                loopy=False
            except:
                print("Error: Wrong option selection.\n")
        if choice<1:
            print("Error: Wrong option selection.\n")
        elif choice>5:     
            print("Error: Wrong option selection.\n")
        elif choice==1 and mat<2:
            print("You don't have enough food available!")
        elif choice==2 and mat<4:
            print("You don't have enough food available!")
        elif choice==3 and mat<1:
            print("You don't have enough food available!")
        elif choice==4 and "Weapon" not in inventory:
            print("You don't have that item!")
        else:
            loop=False
    
    if choice == 1:
        print("The transaction goes flawlessly:")
        print("Gained item: Weapon")
        print("")
        return -3, "Weapon"
    elif choice == 2:
        print("The transaction goes flawlessly:")
        print("Gained item: Super Train Fuel (with the super fuel you now skip every other station)")
        print("")
        return -5, "Super Train Fuel"
    elif choice == 3:
        print("The transaction goes flawlessly:")
        print("Gained item: Zombie Bite Antidote")
        print("")
        return -2, "Zombie Bite Antidote"
    elif choice == 4:
        print("The merchant pulls up a hidden rifle. 'You think you're the first punk trying these shenanigans?' he says whilst instead robbing you:")
        print("Food -2")
        print("")
        return -3, ""
    elif choice == 5:
        print("You barely have enough food as it is, not way you're going to spend it here:")
        print("")
        return -1, ""
    
# event nr 5
def event_zombie_ambush():
    print("")
    print(f"You arrive at {current_stn}. You don't really see anything in particular. This is probably a good place to stay the night. However, as you're sleeping you get ambushed by a zombie!\n")
    
    def print_menu():
        print (25 * "-" , "What do you do?" , 25 * "-")
        print ("1. [If you have the 'Weapon' item] I sleep with my Weapon under my pillow. The zombie doesn't stand a chance")
        print ("2. [If you have the 'Dog Companion' item] Nope! My Dog Companion wakes me up before any ambush!")
        print ("3. [If you have the 'Human Companion' item] Rather them than me!")
        print ("4. Well... Hopefully I taste nice...")
        print (67 * "-")
    loop=True
    while loop:
        print_menu()
        loopy=True
        while loopy:
            choice = input("Enter your choice [1-4]: ")
            print("")
            try:
                choice=int(choice)
                loopy=False
            except:
                print("Error: Wrong option selection.\n")
        if choice<1:
            print("Error: Wrong option selection.\n")
        elif choice>4:     
            print("Error: Wrong option selection.\n")
        elif choice==1 and "Weapon" not in inventory:
            print("You don't have that item!")
        elif choice==2 and "Dog Companion" not in inventory:
            print("You don't have that item!")
        elif choice==3 and "Human Companion" not in inventory:
            print("You don't have that item!")
        else:
            loop=False
    
    if choice == 1:
        print("You kill the zombie before anything bad can happen")
        print("")
        return -1, ""
    elif choice == 2:
        print("You escape the situation before anything bad can happen")
        print("")
        return -1, ""
    elif choice == 3:
        print("Your friends get bitten and turned into a zombie. That doesn't mean he isn't your friend though!")
        print("Lost item: Human Companion")
        print("Gained item: Zombie Companion")
        print("")
        return -1, "Zombie Companion"
    elif choice == 4:
        print("Zombie do what zombie do best. Consider yourself bitten:")
        print("Gained item: Zombie Bite")
        print("")
        return -1, "Zombie Bite"
    
# event nr 6
def event_human_companion_good():
    print("")
    print(f"You arrive at {current_stn}. You see another human being. It seems that they want to be your friend and travel with you. They are even willing to share their food supply with you\n")
    
    def print_menu():
        print (25 * "-" , "What do you do?" , 25 * "-")
        print ("1. I join up with the human.")
        print ("2. I don't join up with the human.")
        print ("3. [If you have the 'Weapon' item] I don't want the human to follow me but I'm not against taking their food.")
        print (67 * "-")
    loop=True
    while loop:
        print_menu()
        loopy=True
        while loopy:
            choice = input("Enter your choice [1-3]: ")
            print("")
            try:
                choice=int(choice)
                loopy=False
            except:
                print("Error: Wrong option selection.\n")
        if choice<1:
            print("Error: Wrong option selection.\n")
        elif choice>3:     
            print("Error: Wrong option selection.\n")
        elif choice==3 and "Weapon" not in inventory:
            print("You don't have that item!")
        else:
            loop=False
    
    if choice == 1:
        print("You now have a friend to travel with! They also eat food though:")
        print("Food +4")
        print("Gained item: Human Companion")
        print("")
        return 3, "Human Companion"
    elif choice == 2:
        print("Who knows, they might be infected or worse:")
        print("")
        return -1, ""
    elif choice == 3:
        print("Just a look at your fearsome weapon is enough to make the human run away:")
        print("Food +3")
        print("")
        return 2, ""
    
# event nr 7
def event_farm():
    print("")
    print(f"You arrive at {current_stn}. Remarkably there seem to be a farm built here with people working in it.\n")
    
    def print_menu():
        print (25 * "-" , "What do you do?" , 25 * "-")
        print ("1. I ask if the farmers want another helping hand.")
        print ("2. I ignore the farm and move on.")
        print ("3. [If you have the 'Human Companion' item] I ask if the farmers want two additional helping hands.")
        print (67 * "-")
    loop=True
    while loop:
        print_menu()
        loopy=True
        while loopy:
            choice = input("Enter your choice [1-3]: ")
            print("")
            try:
                choice=int(choice)
                loopy=False
            except:
                print("Error: Wrong option selection.\n")
        if choice<1:
            print("Error: Wrong option selection.\n")
        elif choice>3:     
            print("Error: Wrong option selection.\n")
        elif choice==3 and "Human Companion" not in inventory:
            print("You don't have that item!")
        else:
            loop=False
    
    if choice == 1:
        print("You spend a day working hard at the farm. As payment for your hard work you receive some food for the journey:")
        print("Food +3")
        print("")
        return 2, ""
    elif choice == 2:
        print("You hate vegetables anyway:")
        print("")
        return -1, ""
    elif choice == 3:
        print("You and your friend spend a day working hard at the farm. As payment for your hard work you receive some food for the journey:")
        print("Food +5")
        print("")
        return 4, ""
    
# event nr 8
def event_parent():
    print("")
    print(f"You arrive at {current_stn}. You witness a scene of horror. A parent is looking over their child that is about to turn into a zombie.\n")
    
    def print_menu():
        print (25 * "-" , "What do you do?" , 25 * "-")
        print ("1. I avert my gaze and move on.")
        print ("2. [If you have the 'Dog Companion Item']. Maybe my dog can help?")
        print ("3. [If you have the 'Zombie Bite Antidote' item] I offer the parent my zombie bite antidote.")
        print (67 * "-")
    loop=True
    while loop:
        print_menu()
        loopy=True
        while loopy:
            choice = input("Enter your choice [1-3]: ")
            print("")
            try:
                choice=int(choice)
                loopy=False
            except:
                print("Error: Wrong option selection.\n")
        if choice<1:
            print("Error: Wrong option selection.\n")
        elif choice>3:     
            print("Error: Wrong option selection.\n")
        elif choice==2 and "Dog Companion" not in inventory:
            print("You don't have that item!")
        elif choice==3 and "Zombie Bite Antidote" not in inventory:
            print("You don't have that item!")
        else:
            loop=False
    
    if choice == 1:
        print("There's nothing you can do:")
        print("")
        return -1, ""
    elif choice == 2:
        print("It's not like your dog is a doctor, I don't know what you expected. The parent offers you some food for your effort though:")
        print("Food +1")
        return 0, ""
    elif choice == 3:
        print("You offer up your own antidote. Hopefully you won't need it yourself. The parent offer you a heartfelt 'thank you' and some food:")
        print("Food +1")
        print("Gained item: Saved a child")
        print("")
        zombie_index = inventory.index("Zombie Bite Antidote")
        inventory.pop(zombie_index)
        return 0, "Saved a child"
    
    
# event nr 9
def event_human_companion_bad():
    print("")
    print(f"You arrive at {current_stn}. You see another human being. It seems that they want to be your friend and travel with you. They are even willing to share their food supply with you\n")
    
    def print_menu():
        print (25 * "-" , "What do you do?" , 25 * "-")
        print ("1. I join up with the human.")
        print ("2. I don't join up with the human.")
        print ("3. [If you have the 'Weapon' item] I don't want the human to follow me but I'm not against taking their food.")
        print (67 * "-")
    loop=True
    while loop:
        print_menu()
        loopy=True
        while loopy:
            choice = input("Enter your choice [1-3]: ")
            print("")
            try:
                choice=int(choice)
                loopy=False
            except:
                print("Error: Wrong option selection.\n")
        if choice<1:
            print("Error: Wrong option selection.\n")
        elif choice>3:     
            print("Error: Wrong option selection.\n")
        elif choice==3 and "Weapon" not in inventory:
            print("You don't have that item!")
        else:
            loop=False
    
    if choice == 1:
        print("You sure are gullible. The human was a thief:")
        print("Food -2")
        print("")
        return -3, ""
    elif choice == 2:
        print("Who knows, they might be infected or worse:")
        print("")
        return -1, ""
    elif choice == 3:
        print("Just a look at your fearsome weapon is enough to make the human run away:")
        print("Food +3")
        print("")
        return 2, ""
    
    
# event nr 10
def event_storage():
    print("")
    print(f"You arrive at {current_stn}. You see an unlooted Bauhaus store. You go in to see if you find something useful.\n")
    
    def print_menu():
        print (25 * "-" , "What do you do?" , 25 * "-")
        print ("1. I pick up a Weapon.")
        print ("2. I pick up a Zombie Bite Antidote.")
        print ("3. I pick up some energy bars.")
        print (67 * "-")
    loop=True
    while loop:
        print_menu()
        loopy=True
        while loopy:
            choice = input("Enter your choice [1-3]: ")
            print("")
            try:
                choice=int(choice)
                loopy=False
            except:
                print("Error: Wrong option selection.\n")
        if choice<1:
            print("Error: Wrong option selection.\n")
        elif choice>3:     
            print("Error: Wrong option selection.\n")
        else:
            loop=False
    
    if choice == 1:
        print("This weapon will surely be useful:")
        print("Gained item: Weapon")
        print("")
        return -1, "Weapon"
    elif choice == 2:
        print("This antidote will surely be useful:")
        print("Gained item: Zombie Bite Antidote")
        print("")
        return -1, "Zombie Bite Antidote"
    elif choice == 3:
        print("When in doubt, get food:")
        print("Food +2")
        print("")
        return 1, ""
    
# event nr 11
def event_prophet():
    print("")
    print(f"You arrive at {current_stn}. You are greeted by a prophet. He asks you a simple question: 'Are you a good person?'.\n")
    
    def print_menu():
        print (25 * "-" , "What do you say?" , 25 * "-")
        print ("1. Yes.")
        print ("2. No.")
        print (67 * "-")
    loop=True
    while loop:
        print_menu()
        loopy=True
        while loopy:
            choice = input("Enter your choice [1-2]: ")
            print("")
            try:
                choice=int(choice)
                loopy=False
            except:
                print("Error: Wrong option selection.\n")
        if choice<1:
            print("Error: Wrong option selection.\n")
        elif choice>2:     
            print("Error: Wrong option selection.\n")
        else:
            loop=False
    
    if choice == 1 and "Saved a child" in inventory:
        print("You are a good person, you saved a child:")
        print("Food +10")
        print("")
        return 9, ""
    elif choice == 1 and "Dog Companion" in inventory:
        print("You are a good person, you helped a dog:")
        print("Food +5")
        print("")
        return 4, ""
    elif choice == 1 and "Helped Old Lady" in inventory:
        print("You did help an old lady:")
        print("Food +2")
        print("")
        return 1, ""
    elif choice == 1 and "Zombie Companion" in inventory:
        print("A good person wouldn't let their friends sacrifice themselves to become a zombie:")
        print("")
        return -1, ""
    elif choice == 1 and "Weapon" in inventory:
        print("Would a good person run around with a weapon?:")
        print("")
        return -1, ""    
    elif choice == 1:
        print("The prophet shrugs. He assumes you're telling the truth and hands you some food:")
        print("Food +1")
        print("")
        return 0, ""
    elif choice == 2 and "Zombie Companion" in inventory:
        print("At least you're being honest. A good person wouldn't let their friends sacrifice themselves to become a zombie. Have a reward for your honesty:")
        print("Food +1")
        print("")
        return 0, ""
    elif choice == 1 and "Weapon" in inventory:
        print("At least you're being honest. A good person wouldn't run around with weapons. Have a reward for your honesty:")
        print("Food +1")
        print("")
        return 0, ""  
    elif choice == 2:
        print("'You should become good', the prophet says, 'I reward good deeds':")
        print("")
        return -1, ""
    
# event nr 12
def event_nod_1():
    print("")
    print(f"You arrive at {current_stn}. You see the guys from Nod Analytics Bootcamp. They ask you if a string is a data type or a data structure.\n")
    
    def print_menu():
        print (25 * "-" , "What do you do?" , 25 * "-")
        print ("1. Data Type.")
        print ("2. Data Structure.")
        print (67 * "-")
    loop=True
    while loop:
        print_menu()
        loopy=True
        while loopy:
            choice = input("Enter your choice [1-2]: ")
            print("")
            try:
                choice=int(choice)
                loopy=False
            except:
                print("Error: Wrong option selection.\n")
        if choice<1:
            print("Error: Wrong option selection.\n")
        elif choice>2:     
            print("Error: Wrong option selection.\n")
        else:
            loop=False
    
    if choice == 1:
        print("The guys nods (get it?) appreciatively. They give you some food as a reward:")
        print("Food +1")
        print("Gained item: Nod Analytics right answer [1]")
        print("")
        return 0, "Nod Analytics Right Answer [1]"
    elif choice == 2:
        print("The guys shake their heads:")
        print("")
        return -1, ""
    
# event nr 13
def event_gang_attack():
    print("")
    print(f"You arrive at {current_stn}. You immediately see a gang of bandits. They try to rob you.\n")
    
    def print_menu():
        print (25 * "-" , "What do you do?" , 25 * "-")
        print ("1. Best to not resist.")
        print ("2. [If you have the 'Zombie Companion' item] Say hello to my little friend!.")
        print ("3. [If you have the 'Weapon' item] We'll see who robs who.")
        print (67 * "-")
    loop=True
    while loop:
        print_menu()
        loopy=True
        while loopy:
            choice = input("Enter your choice [1-3]: ")
            print("")
            try:
                choice=int(choice)
                loopy=False
            except:
                print("Error: Wrong option selection.\n")
        if choice<1:
            print("Error: Wrong option selection.\n")
        elif choice>3:     
            print("Error: Wrong option selection.\n")
        elif choice==2 and "Zombie Companion" not in inventory:
            print("You don't have that item!")
        elif choice==3 and "Weapon" not in inventory:
            print("You don't have that item!")
        else:
            loop=False
    
    if choice == 1:
        print("The gang appreciate you not giving them trouble. They don't steal as much as they would otherwise do:")
        print("Food -1")
        print("")
        return -2, ""
    elif choice == 2:
        print("These punks are not about to mess with someone who hangs around with zombies. Instead they offer you their food to get on your good side:")
        print("Food +4")
        print("")
        return 3, ""
    elif choice == 3:
        print("Are you crazy? You are being severly outnumbered! They steal more from you now:")
        print("Food -3")
        return -4, ""
    
# event nr 14
def event_nod_2():
    print("")
    print(f"You arrive at {current_stn}. You see the guys from Nod Analytics Bootcamp. They ask you what the output will be from the following code 'print(len([1, [2, 3]]))'.\n")
    
    def print_menu():
        print (25 * "-" , "What do you do?" , 25 * "-")
        print ("1. The output will be '2'.")
        print ("2. The output will be '3'.")
        print (67 * "-")
    loop=True
    while loop:
        print_menu()
        loopy=True
        while loopy:
            choice = input("Enter your choice [1-2]: ")
            print("")
            try:
                choice=int(choice)
                loopy=False
            except:
                print("Error: Wrong option selection.\n")
        if choice<1:
            print("Error: Wrong option selection.\n")
        elif choice>2:     
            print("Error: Wrong option selection.\n")
        else:
            loop=False
    
    if choice == 1:
        print("The guys nods (get it?) appreciatively. They give you some food as a reward:")
        print("Food +1")
        print("Gained item: Nod Analytics right answer [2]")
        print("")
        return 0, "Nod Analytics Right Answer [2]"
    elif choice == 2:
        print("The guys shake their heads:")
        print("")
        return -1, ""
    
# event nr 15
def event_nod_3():
    print("")
    print(f"You arrive at {current_stn}. You see the guys from Nod Analytics Bootcamp. They ask you what to write if you want to find your current working directory.\n")
    
    def print_menu():
        print (25 * "-" , "What do you do?" , 25 * "-")
        print ("1. import pandas as pd -> pd.getcwd().")
        print ("2. import os -> os.getcwd().")
        print (67 * "-")
    loop=True
    while loop:
        print_menu()
        loopy=True
        while loopy:
            choice = input("Enter your choice [1-2]: ")
            print("")
            try:
                choice=int(choice)
                loopy=False
            except:
                print("Error: Wrong option selection.\n")
        if choice<1:
            print("Error: Wrong option selection.\n")
        elif choice>2:     
            print("Error: Wrong option selection.\n")
        else:
            loop=False
    
    if choice == 1:
        print("The guys shake their heads:")
        print("")
        return -1, ""
    elif choice == 2:
        print("The guys nods (get it?) appreciatively. They give you some food as a reward:")
        print("Food +1")
        print("Gained item: Nod Analytics right answer [3]")
        print("")
        return 0, "Nod Analytics Right Answer [3]"
    
# event nr 16
def event_granny_good():
    print("")
    print(f"You arrive at {current_stn}. You see an old lady trying to cross the road.\n")
    
    def print_menu():
        print (25 * "-" , "What do you do?" , 25 * "-")
        print ("1. I help her.")
        print ("2. I ignore her.")
        print (67 * "-")
    loop=True
    while loop:
        print_menu()
        loopy=True
        while loopy:
            choice = input("Enter your choice [1-2]: ")
            print("")
            try:
                choice=int(choice)
                loopy=False
            except:
                print("Error: Wrong option selection.\n")
        if choice<1:
            print("Error: Wrong option selection.\n")
        elif choice>2:     
            print("Error: Wrong option selection.\n")
        else:
            loop=False
    
    if choice == 1:
        print("The old lady thanks you for your help and gives you some cookies:")
        print("Food +2")
        print("Gained item: Helped Old Lady")
        print("")
        return 1, "Helped Old Lady"
    elif choice == 2:
        print("The situation seems shady, best to leave her alonde:")
        print("")
        return -1, ""
    
# event nr 17
def event_granny_bad():
    print("")
    print(f"You arrive at {current_stn}. You see an old lady trying to cross the road.\n")
    
    def print_menu():
        print (25 * "-" , "What do you do?" , 25 * "-")
        print ("1. I help her.")
        print ("2. I ignore her.")
        print (67 * "-")
    loop=True
    while loop:
        print_menu()
        loopy=True
        while loopy:
            choice = input("Enter your choice [1-2]: ")
            print("")
            try:
                choice=int(choice)
                loopy=False
            except:
                print("Error: Wrong option selection.\n")
        if choice<1:
            print("Error: Wrong option selection.\n")
        elif choice>2:     
            print("Error: Wrong option selection.\n")
        else:
            loop=False
    
    if choice == 1 and "Dog Companion" in inventory:
        print("The old lady turns out to be a thief in disguise but your dog warns you before it's too late:")
        print("")
        return -1, ""
    elif choice == 1:
        print("The old lady turns out to be a thief in disguise!:")
        print("Food -1")
        print("")
        return -2, ""
    elif choice == 2:
        print("The situation seems shady, best to leave her alonde:")
        print("")
        return -1, ""
    
# event nr 18
def event_hunter():
    print("")
    print(f"You arrive at {current_stn}. You see an hunter sitting by a campfire. They invites you over to share in their meal.\n")
    
    def print_menu():
        print (25 * "-" , "What do you do?" , 25 * "-")
        print ("1. I join them and take some food for the journey.")
        print ("2. [If you have the 'Zombie Bite' item] I ask them if they can do something about my Zombie Bite.")
        print ("3. I ask them if they want to follow me on my journey.")
        print ("4. I ignore them.")
        print (67 * "-")
    loop=True
    while loop:
        print_menu()
        loopy=True
        while loopy:
            choice = input("Enter your choice [1-4]: ")
            print("")
            try:
                choice=int(choice)
                loopy=False
            except:
                print("Error: Wrong option selection.\n")
        if choice<1:
            print("Error: Wrong option selection.\n")
        elif choice>4:     
            print("Error: Wrong option selection.\n")
        elif choice==2 and "Zombie Bite" not in inventory:
            print("You don't have that item!")
        else:
            loop=False
    
    if choice == 1:
        print("You partake in the hunter's stew:")
        print("Food +2")
        return 1, ""
    elif choice == 2:
        print("The hunter gives you an antidote for your bite:")
        print("Food +1")
        print("Gained item: Zombie Bite Antidote")
        print("")
        return 0, "Zombie Bite Antidote"
    elif choice == 3 and "Zombie Companion" in inventory:
        print("The hunter absolutely wants to follow the person who can tame a zombie:")
        print("Gain item: Hunter Companion (The hunter will give you +1 food whenever you enter a station)")
        print("Food +1")
        return 0, "Hunter Companion"
    elif choice == 3 and "Dog Companion" in inventory and "Weapon" in inventory:
        print("The hunter thinks you seem well prepared for the apocalypse with your dog and weapon and wants to tag along:")
        print("Gain item: Hunter Companion (The hunter will give you +1 food whenever you enter a station)")
        print("Food +1")
        return 0, "Hunter Companion"
    elif choice == 3:
        print("The hunter think you seem unprepared for the apocalypse and doesn't want to tag along:")
        print("Food +1")
        return 0, ""
    elif choice == 4:
        print("Best to not get involved with strangers:")
        print("")
        return -1, ""
    
# event nr 19
def event_hospital():
    print("")
    print(f"You arrive at {current_stn}. You see a manned hospital next to the station.\n")
    
    def print_menu():
        print (25 * "-" , "What do you do?" , 25 * "-")
        print ("1. I look around the hospital for food.")
        print ("2. [If you have the 'Zombie Bite' item] I ask them if they can do something about my Zombie Bite.")
        print ("3. [If you have the 'Zombie Companion' item] I ask them if they can cure my friend.")
        print ("4. I ask them if I can buy a Zombie Bite Antidote for 1 unit of food.")
        print ("5. I ignore the hospital and move on.")
        print (67 * "-")
    loop=True
    while loop:
        print_menu()
        loopy=True
        while loopy:
            choice = input("Enter your choice [1-5]: ")
            print("")
            try:
                choice=int(choice)
                loopy=False
            except:
                print("Error: Wrong option selection.\n")
        if choice<1:
            print("Error: Wrong option selection.\n")
        elif choice>5:     
            print("Error: Wrong option selection.\n")
        elif choice==2 and "Zombie Bite" not in inventory:
            print("You don't have that item!")
        elif choice==3 and "Zombie Companion" not in inventory:
            print("You don't have that item!")
        else:
            loop=False
    
    if choice == 1:
        print("You sneak around and see if you can find food. You mostly find blood bags. If they work for vampires they should work for you as well:")
        print("Food +2")
        return 1, ""
    elif choice == 2:
        print("The staff immediately see that you require aid and give you an antidote:")
        print("Gained item: Zombie Bite Antidote")
        print("")
        return -1, "Zombie Bite Antidote"
    elif choice == 3:
        print("The staff is baffled by the state of your friend. They cannot help, unfortunately, but they pay you some food in return for taking a DNA sample of your Zombie Companion:")
        print("")
        print("Food +4")
        return 3, ""
    elif choice == 4:
        print("They are willing to trade one unit of food for an antidote:")
        print("Gained item: Zombie Bite Antidote")
        print("Food -1")
        return -2, "Zombie Bite Antidote"
    elif choice == 5:
        print("You never liked hospitals. Too many needles:")
        print("")
        return -1, ""
    
# event nr 20
def event_food_merchant_sell():
    print("")
    print(f"You arrive at {current_stn}. You see a stall where a merchant trades food for items.\n")
    
    def print_menu():
        print (25 * "-" , "What do you do?" , 25 * "-")
        print ("1. [If you have the 'Weapon' item] I sell the 'Weapon' item for 3 units of food")
        print ("2. [If you have the 'Super Train Fuel' item] I sell the 'Super Train Fuel' item for 5 units of food ")
        print ("3. [If you have the 'Zombie Bite Antidote' item] I sell the 'Zombie Bite Antidote' item for 2 units of food ")
        print ("4. [If you have the 'Dog Companion' item] I sell the 'Dog Companion' item for 3 units of food ")
        print ("5. [If you have the 'Weapon' item] I yell 'This is a robbery! Give me everything you own!' ")
        print ("6. I ignore the merchant.")
        print (67 * "-")
    loop=True
    while loop:
        print_menu()
        loopy=True
        while loopy:
            choice = input("Enter your choice [1-6]: ")
            print("")
            try:
                choice=int(choice)
                loopy=False
            except:
                print("Error: Wrong option selection.\n")
        if choice<1:
            print("Error: Wrong option selection.\n")
        elif choice>6:     
            print("Error: Wrong option selection.\n")
        elif choice==1 and "Weapon" not in inventory:
            print("You don't have that item!")
        elif choice==2 and "Super Train Fuel" not in inventory:
            print("You don't have that item!")
        elif choice==3 and "Zombie Bite Antidote" not in inventory:
            print("You don't have that item!")
        elif choice==4 and "Dog Compainon" not in inventory:
            print("You don't have that item!")
        elif choice==5 and "Weapon" not in inventory:
            print("You don't have that item!")
        else:
            loop=False
    
    if choice == 1:
        print("The transaction goes flawlessly:")
        print("Lost item: Weapon")
        print("")
        return 2, "Sold Weapon"
    elif choice == 2:
        print("The transaction goes flawlessly (with the super fuel you now skip every other station):")
        print("Lost item: Super Train Fuel")
        print("")
        return 4, "Sold Super Train Fuel"
    elif choice == 3:
        print("The transaction goes flawlessly:")
        print("Lost item: Zombie Bite Antidote")
        print("")
        return 1, "Sold Zombie Bite Antidote"
    elif choice == 4:
        print("The transaction goes flawlessly:")
        print("Lost item: Dog Companion")
        print("")
        return 1, "Sold Dog Companion"
    elif choice == 5:
        print("The merchant pulls up a hidden rifle. 'You think you're the first punk trying these shenanigans?' he says whilst instead robbing you:")
        print("Food -2")
        print("")
        return -3, ""
    elif choice == 6:
        print("You love your things, no way you're going to sell them:")
        print("")
        return -1, ""
   

# The game loop controls the flow of the game and calls the functions above.

game_on=True
while game_on==True: # This while loop will remain True as long as the player want to play
    # Below are all the stations the player can visit in a list
    tågstationer = ["Stockholm City", "Stockholm Odenplan", "Solna", "Ulriksdal", "Helenelund", "Sollentuna", "Häggvik", "Norrviken", "Rotebro", "Upplands Väsby", "Rosersberg", "Märsta", "You were driving so fast that you skipped Märsta!"]
    
    # Below are all the events the player may encounter in a list
    lst_events = [event_ica_bad, event_ica_good, event_dog_follower, event_food_merchant, event_zombie_ambush, event_human_companion_good, event_farm, event_parent, event_human_companion_bad, event_storage, event_prophet, event_gang_attack, event_nod_1, event_nod_2, event_nod_3, event_granny_good, event_granny_bad, event_hunter, event_hospital, event_food_merchant_sell]
    
    # The two variables below are starting values that will change during the course of the game.
    current_stn = "Stockholm City"
    inventory=[]
    
    # The variable below will only be taken into account if the player receives the item "Zombie Bite"
    zombie_bite_counter=0
    
    # This is the introduction to the game
    print("Welcome to the apocalypse! Stockholm is overrun by zombies and you need to get out. Being the smart person that you are you figure that the best way to go about it is to take the train to Märsta. Märsta is probably zombie free right?\n")

    # These while loops will make appearances throughout the game as a way to limit the amount of information the player
    # receives at any given time as to not make them feel overwhelmed. The loop will pause the game until the player wants
    # to proceed
    cont=""
    while cont.lower().startswith("y")==False:
        cont=input("Continue? [Yes/No]: ").lower()
        print("")
    
    # The following loop allows the player to choose the difficulty level of the game which corresponds to the amount of
    # food the player starts with. Then the function mat_diff is called to provide the actual numerical food value to the
    # variable "mat"
    mat=""
    while mat.lower().startswith("e")==False and mat.lower().startswith("m")==False and mat.lower().startswith("h")==False:
        mat=input("Please choose the difficulty level [Easy, Medium, Hard]: ").lower()
        print("")
    mat=mat_diff(mat)

    # Here we call the state_of_play() function for the first time to allow the player to see what he/she starts with in
    # terms of food and items
    print("You start the game with the following information:\n")
    state_of_play()
    print("")
    
    # Here the rules of the game are explained and the game will starts once the player gives the correct input
    cont=""
    while cont.lower().startswith("y")==False:
        cont=input("You don't want to run out of food! As a rule thumb it will cost you one unit of food to get to the next station. Also, you may at most have 1 of any given item at a time, if you obtain another it will automatically removed. Ready to get this show on the rails? [Yes/No]: ").lower()
        print("")




    # The loop below will continue until the current train station becomes "Rosersberg".
    while not current_stn == "Rosersberg":
        # We call the "tåg" station to move the player from station to station
        current_stn=tåg(current_stn)
        
        # The following if statement is necessary in case the player skips over Rosersberg immediately to Märsta or further
        if current_stn == "Märsta":
            current_stn = "Rosersberg"
            break
        elif current_stn == tågstationer[-1]:
            current_stn = "Märsta"
            break

        # If the player have the "Super Train Fuel" item he/she will call the "tåg" function an additional time
        if "Super Train Fuel" in inventory:
            current_stn=tåg(current_stn)
        
        # After we arrive to a station the event_picker() function will be called to generate a random event to occur
        ny_mat, ny_item = event_picker()
        
        # We adjust the new food levels from the event. We also take into consideration if the Hunter or Human companion
        # is in the inventory list as these items affect the change of food
        mat+=ny_mat
        if "Hunter Companion" in inventory:
            mat+=1
        if "Human Companion" in inventory:
            mat=mat-1
            
        # We append any new items to the inventory list
        inventory.append(ny_item)

        # The game doesn't allow for the player to have both the Human Companion and the Zombie Companion at the same time.
        # Therefore we remove the Human Companion if this would happen
        if "Human Companion" in inventory and "Zombie Companion" in inventory:
            x=0
            for i in inventory:
                if i=="Human Companion":
                    inventory[x]=""
                x+=1
        
        # If the player obtains the Zombie Bite item the zombie_bite_counter will start to increase. If the counter reaches
        # 3 one of two things will happen. Either the counter is reset and both the Zombie Bite Antidote and the Zombie
        # Bite items are removed or the player loses the game
        if "Zombie Bite" in inventory:
            zombie_bite_counter+=1
            if zombie_bite_counter==3 and "Zombie Bite Antidote" in inventory:
                print("Your zombie bite is acting up. It's probably best to apply the antidote.\n")
                zombie_bite_counter=0
                x=0
                for i in inventory:
                    if i=="Zombie Bite":
                        inventory[x]=""
                    elif i=="Zombie Bite Antidote":
                        inventory[x]=""
                    x+=1
            elif zombie_bite_counter ==3:
                print("You didn't take care of your zombie bite in time! Unfortunately you have now joined the undead horde. Game Over.")
                break
                
        # If the player obtains all three versions of the Nod Analytics Right Answers they get the secret ending
        if "Nod Analytics Right Answer [1]" in inventory and "Nod Analytics Right Answer [2]" in inventory and "Nod Analytics Right Answer [3]" in inventory:
            print("You have answered so many coding questions correctly that the Nod guys have decided to hack the game for you.\n")
            current_stn="Rosersberg"
            break
        
        # In case the player have an item and the "Sold" version of the item both will be removed from the inventory list.
        x=0
        for i in inventory:
            if i in inventory and "Sold "+i in inventory:
                inventory[x]=""
            x+=1
        x=0
        for i in inventory:
            if i.startswith("Sold ")==True:
                inventory[x]=""
            x+=1
        
        # This for loops makes sure that any multiple of an item get removed from the inventory
        count=0
        x=0
        for i in inventory:
            count=inventory.count(i)
            if count > 1:
                inventory[x]=""
            x+=1
        
        # This line makes sure that all empty strings get removed from the inventory
        inventory = list(filter(lambda u: len(u)>0, inventory))

        # After the event and the clean up thereafter we show the player the relevant information by calling the
        # state_of_play function
        print("This is your status after the event:\n")
        state_of_play()
        print("")

        # We check if the player's food supply is empty using the check_if_dead function
        dead=check_if_dead(mat)
        if dead==0:
            print("I am sorry, your choices led to your demise. Game Over.")
            break

        # We allow the player to stop playing here
        cont=""
        while cont.lower().startswith("y")==False and cont.lower().startswith("n")==False:
            cont=input("Want to continue playing? [Yes/No]: ").lower()
            print("")
        if cont.lower().startswith("n")==True:
            print("You have given up..")
            break

    # Once we're out of the previous for loop we increase the train station by one step and check if that corresponds to
    # "Märsta", if it does it means the player won
    current_stn=tåg(current_stn)
    märs=check_if_märsta(current_stn)
    if märs==1:
        print("You did it! You escaped the zombies of Stockholm and will live a long and healthy life (unless you are bitten)!")

    # These two lines below will only be used if the player manages to drive past Märsta
    if current_stn==tågstationer[-1]:
        print("You were driving so fast that you skipped the Märsta station! If this is considered to be a win or not is up to you.")

    # Finally, the player have the option to play again. If he/she does, we clear the previous output and start from the top
    game_on=input("Do you want to restart? [Yes/No]: ").lower()
    if game_on.lower().startswith("y")==True:
        game_on = True
        clear_output(wait = True)
    else:
        game_on = False