print("Welcome to my first word game")
name = input("What is your name? ")
age = int(input("What is your age? "))
print("Welcome ", name, "you are ", age, "years old")
health = 10
if age >= 18:
    print("You are old enough to play")

    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("Great lets get to it then. You have", health, "health")

        ans = input("You start walking and immedietly find a tiger... Do you fight or run (fight/run)? ").lower()
        if ans == "fight":
            print("As soon as you apprach the tiger you scare it away unscathed")
        else:
            print("As you start to run away the tiger jumps on you... somehow you manage to get away but you loose 2 health")
            health -= 2
            print("You now have ", health, "health")

        ans = input("I'ts getting cold and you need to find shelter. You see a cave near by and a stretch of forrest with plenty of tress to cut down. Do you enter the cave or cut the tress (cave/trees)? ")
        if ans == "cave":
            print("You enter the cave and find an old campsite and you start at fire.")
        else:
            print("As you walk it keeps getting colder and you shiver and are unable to cut down the trees. You head back to the cave and loose 2 health")
            health -= 2
            print("You now have ", health, "health")

        ans = input("The next day you wake up hungry and walk for about 2 hours. You come up to a lake, where on the other side you see a small cabin. Do you fish here now or swim across (fish/across)? ")
        if ans == "across":
            print("You manage to get to the other side and find that the cabin has a canned food, you gorge yourself and regain your health")
            health = 10
            print("You now have ", health, "health")
        else:
            print("Since you don't have a fishing rod you realize that you have to try to trap fish with your shirt. You cath one fish and have to eat it raw and regain 1 health and swim to the cabin")
            health += 1
            print("You now have ", health, "health")

        ans = input("The next day you wake up shivering and hear people approaching. You are afraid.. Do you run away or wait (run/wait)? ")
        if ans == "run":
            print("You run away but are too weak and end up falling. You die of an infection alone on the woods.")
            health = 0

        else:
            print("The strangers are park rangers and take you to safety where you make a full recovery")
            health = 10
            print("You won!!!")

    else:
        print("Ok goodbye")
            

else:
    print("You are not old enough to play")




