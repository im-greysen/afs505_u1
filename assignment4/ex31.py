print("Welcome to the strange trails textr adventure beta")
print("This text adventure is unfinished, but I will get to it later.")

print("""You are a hopeless romantic named Buck Vernon.

You are in love with a girl named Lily,

but she is currently seeing a man named Big Jim.

You also like another girl Louisa 'Lee' Green and she

has asked you to meet her in the woods to show you her magical abilities.

Do you want to:

(1) Go to the bar George's Place to fight Big Jim or
(2) Meet Lee in the woods?""")

place = input("> ")

print()

if place == "1":
    print("There's a giant bear in here eating a cheese cake.")
    print()
    print("What do you do?")
    print()
    print("1. Take the cake.")
    print()
    print("2. Scream at the bear.")

    print()

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif place == "2":
    print("You are are at the trailhead and there is a fork in the path ahead.")
    print()
    print("(1) Head right on the well beaten trail.")
    print("(2) Head left down a strange trail.")
    print("(3) This place gives me the creeps! I'm going to George's Place instead.")

    trail = input("> ")

    if trail == "1" or trail == "3":
        print("A bear spots you. You are mauled to death")
        print("Good job!")
    else:
        print("You make your way to a moonlit clearing and find Lee waiting for you.")
        print("Good job!")

else:
    print("You stumble around and fall on a knife and die. Good job!")
