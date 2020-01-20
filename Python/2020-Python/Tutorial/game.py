import time #Imports a module to add to the game.

#Figuring out how the users might respond.
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

#Grabbing objects
sword = 0
flower = 0

required = ("\n User only A, B, or C\n") # Cutting down on duplication.
#The story is broken into sections, starting with "intro"
def intro():
    print ("After a drunken night out with friends, you awaken the "
    "next morning in a thick, damn forest. Head spinning and "
    "fighting the urge to voimt, you stand and marvel at your new, "
    "unfamilier setting. The peace quickly fades when you hear a "
    "grotesque sound emitting behind you. A slobbering orc is "
    "running towards you. You will :")
    time.sleep(1)
    print( """ A. Grab a nearby rock and throw it at the orc.
    B. Lie down and wait to be mauled
    C. Run """)
    choice = input(">>> ") #Here is your first choice.
    if choice in answer_A:
        option_rock()
    elif choice in answer_B:
        print ("\nWelp, that was quick. "
        "\n\n You died!")
    elif choice in answer_C:
        option_run()
    else:
        print (required)
        intro()

def option_rock():
    print ("\n The orc is stunned, but regains control. he begins running towards you again. Will you: ")
    time.sleep(1)
    print(""" A. Run
    B. Throw another rock
    C. Run towards a nearby cave""")
    choice = input(">>> ")
    if choice in answer_A:
        option_run()
    elif choice in answer_B:
        print("\n You decided to throw another rock as if the first rock thrown did much damage. The rock flew well over the "
        "orcs head. You missed. \n\n You died!")
    elif choice in answer_C:
        option_cave()
    else:
        print (required)
        option_rock()

def option_cave():
    print ("\n You were hesitant, since the cave was ark and "
    "omnious. Before you fully enter, you notice a shiny sword on "
    " the ground. Do you pick up a sword. Y/N?")
    choice = input(">>> ")
    if choice in yes:
        sword = 1 # adds a sword
    else:
        sword = 0
    print ("\n What do you do next?")
    time.sleep(1)
    print (""" A. Hide in silence
    B. Fight
    C. Run""")
    choice = input(">>> ")
    if choice in answer_A:
        print ("\nReally? You're going to hide in the dark? I think"
        "orcs can see very well in the dark, right? Not sure, but "
        " I'm going with YES, so ... \n\nYou died!")
    elif choice in answer_B:
        if sword > 0:
            print ("\n You laid in wait. The shimmering sword attracted "
            "the orc, which thought you were no match. As he walked "
            " close and lcose, your heard beat rapidly. As the orc "
            "reached out to grab the sword, you pierced the blade into "
            "its chest. \n\nYou survived!")
        else: #The user didn't grab the sword
            print("\nYou should have picked up that sword. You're defenseless. \n\nYou died!")
    elif choice in answer_C:
        print ("As the orc enters the dark cave, you silently "
        "sneak out. You're several feet away, but the orc turns "
        "around and sees you running.")
        option_run()
    else:
        print (required)
        option_cave()

def option_run():
    print ("\n You run as quickly as possible, but the orc's "
    "speed is too great. You will:")
    time.sleep(1)
    print (""" A. Hide behind boulder
    B. Trapped, so you fight
    C. Run towards abandoned town""")
    choice = input(">>> ")
    if choice in answer_A:
        print ("You're easily spotted. "
        "\n\n You died!")
    elif choice in answer_B:
        print ("\nYou're no match for an orc."
        "\n\n You died!")
    elif choice in answer_C:
        option_town()
    else:
        print (required)
        option_run()

def option_town():
    print ("\n While frantically running, you notice a rusted "
    "sword lying in the mud. You quickly reach down and grab it, "
    "but miss. You try to calm your heavy breathing as you hide "
    "charging around the corner. You notice a purple flower "
    "near your foot. Do you pick it up? Y/N")
    choice = input(">>> ")
    if choice in yes:
        flower = 1 #adds a flower
    else:
        flower = 0
    print ("You hear its heavy footsteps and ready yourself for the impending orc.")
    time.sleep(1)
    if flower > 0:
        print ("\n You quickly hold out the purple flower, somehow hoping it will stop the orc "
        "It does! The orc was looking fo rlove. \n\nThis got weird, but you survived!")
    else: #If the user didn't grab the sword
        print ("\n Maybe you should have picked up the flower. "
        "\n\n You died!")

intro()