# Introduction
print("Welcome to the Adventure Game!")
print("You are a brave adventurer on a quest to defeat the evil dragon and save the kingdom.")

# First choice
print("You come to a fork in the road. Do you go left or right?")
choice = input("Type 'left' or 'right' to make your choice: ")

if choice == "left":
    print(
        "You follow the winding path to the left and come across a dark forest. Do you brave the unknown and enter the forest, or turn back and try the other path?")
    choice = input("Type 'enter' or 'turn back' to make your choice: ")

    if choice == "enter":
        print(
            "You venture into the forest and soon come across a clearing. In the clearing, you see a small cottage. Do you approach the cottage or turn back and try the other path?")
        choice = input("Type 'approach' or 'turn back' to make your choice: ")

        if choice == "approach":
            print(
                "As you approach the cottage, you see an old man sitting on the porch. He beckons you over and offers you a magic potion that will give you the strength to defeat the dragon. Do you accept the potion or decline?")
            choice = input("Type 'accept' or 'decline' to make your choice: ")

            if choice == "accept":
                print(
                    "You drink the potion and feel a surge of strength and power. Armed with new courage, you set out to defeat the dragon and save the kingdom. You are successful and are hailed as a hero.")
            else:
                print(
                    "You decline the old man's offer and continue on your journey. Without the magic potion, you are unable to defeat the dragon and the kingdom is lost. You are remembered as a coward.")

        else:
            print(
                "You turn back and try the other path. As you make your way through the forest, you come across a group of bandits. They demand all of your gold in exchange for safe passage. Do you give them your gold or fight them?")
            choice = input("Type 'give' or 'fight' to make your choice: ")

            if choice == "give":
                print(
                    "You give the bandits all of your gold and they allow you to pass. You continue on your journey, but without any gold to buy supplies, you are unable to defeat the dragon and the kingdom is lost. You are remembered as a fool.")
            else:
                print("You decide to fight the bandits. Despite being outnumbered, you are able to defeat them and continue on your journey. You eventually come across the dragon's lair and are able to defeat the dragon with your strength and bravery. You are hailed as a hero and the kingdom is saved.")

    else:
        print("You follow the path to the right and come across a river. Do you try to cross the river or turn back and try the other path?")
        choice = input("Type 'cross' or 'turn back' to make your choice: ")

        if choice == "cross":
            print("You try to cross the river, but halfway across you slip and fall into the water. Do you try to swim to shore or try to cling to a nearby log?")
            choice = input("Type 'swim' or 'cling' to make your choice: ")

        if choice == "swim":
            print(
                "You try to swim to shore, but the current is too strong and you are swept downstream. You eventually wash up on a sandy beach, but you are lost and have no supplies. Do you try to find your way back or give up and wait for rescue?")
            choice = input("Type 'find way back' or 'wait' to make your choice: ")

            if choice == "find way back":
                print(
            "You set out to find your way back to the kingdom. Despite facing many challenges, you are determined and eventually make it back to civilization. You continue on your journey and are able to defeat the dragon, saving the kingdom and becoming a hero.")
        else:
            print(
            "You decide to wait for rescue. Days go by and no one comes. You eventually succumb to starvation and are never heard from again. The kingdom is lost and you are remembered as a failure.")

else:
         print(
        "   You cling to the log and are able to float downstream until you reach a safe place to shore. You continue on your journey and eventually come across the dragon's lair. You are able to defeat the dragon with your cunning and resourcefulness, saving the kingdom and becoming a hero.")


print("You turn back and try the other path. As you make your way through the forest, you come across a group of friendly elves. They offer to guide you to the dragon's lair and help you defeat the dragon. Do you accept their offer or decline?")
choice = input("Type 'accept' or 'decline' to make your choice: ")

if choice == "accept":
  print("You accept the elves' offer and, with their help, are able to defeat the dragon and save the kingdom. You are hailed as a hero and the elves invite you to join their community, where you live out the rest of your days in peace and happiness.")
else:
  print("You decline the elves' offer and continue on your journey alone. As you make your way to the dragon's lair, you are ambushed by the dragon's minions. Without the help of the elves, you are unable to defeat the dragon and the kingdom is lost. You are remembered as a fool.")

print("The adventure is over. Thank you for playing!")

