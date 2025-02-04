import os, random, math

run = True
menu = True
play = False
rules = False
key = False
fight = False
standing = True
buy = False
speak = False
boss = False

HP = 50
HPMAX = 50
ATK = 3
pot = 1
elix = 0
gold = 0
x = 0
y = 0

Limiter = 0
Friend = False
PreviousUsed = "1 "
currentLocX = 2
currentLocY = 3
currentCoords = [currentLocX,currentLocY]
townCoords = [2,3]
directionList = ["north","northeast","east","southeast","south","southwest","west","northwest"]
nameList = [["Bartholomew Donaldson","Nigel Higgenbottom","Claire Presley","Elvis Rosinkranz","William de Meij",],
            ["Julia McKenna","Declan Fronteo","Kelsey Cook","Vance Watson","Patrick Joy"],
            ["Mickey Heem","Baz Moriondo","Khai Price","Rosa Coggins","Hallie Walton"],
            ["Blake Dunbar","Isaac Miles","Grady Jon","Cody Mantra","Brian Brooks"],
            ["Peter Williams","Phillip Hyde","Ellie Stevens","Teddy Mala","Billie Sufjan"]]

#  x = 0       x = 1       x = 2       x = 3       x = 4       x = 5         x = 6
map = [["plains", "plains", "plains", "plains", "forest", "mountain", "cave"],  # y = 0
       ["forest", "forest", "forest", "forest", "forest", "hills", "mountain"],  # y = 1
       ["forest", "fields", "bridge", "plains", "hills", "forest", "hills"],  # y = 2
       ["plains", "shop", "town", "mayor", "plains", "hills", "shop"],  # y = 3
       ["plains", "fields", "fields", "plains", "hills", "mountain", "mountain"]]  # y = 4

y_len = len(map) - 1
x_len = len(map[0]) - 1

biom = {
    "plains": {
        "t": "PLAINS",
        "e": True},
    "forest": {
        "t": "WOODS",
        "e": True},
    "fields": {
        "t": "FIELDS",
        "e": False},
    "bridge": {
        "t": "BRIGE",
        "e": True},
    "town": {
        "t": "TOWN CENTRE",
        "e": False},
    "shop": {
        "t": "SHOP",
        "e": False},
    "mayor": {
        "t": "MAYOR",
        "e": False},
    "cave": {
        "t": "CAVE",
        "e": False},
    "mountain": {
        "t": "MOUNTAIN",
        "e": True},
    "hills": {
        "t": "HILLS",
        "e": True,
    }
}

e_list = ["Goblin", "Orc", "Slime"]
e_listUncommon = ["Kobold", "Hobgoblin"]
e_listRare = ["Owlin", "Dark Elf"]
e_listEpic = ["Goliath", "Minotaur"]
e_listFriendlys = ["Satyr", "Human", "Gnome"]

mobs = {
    "Goblin": {
        "hp": 15,
        "at": 3,
        "go": 8
    },
    "Orc": {
        "hp": 35,
        "at": 5,
        "go": 18
    },
    "Slime": {
        "hp": 30,
        "at": 2,
        "go": 12
    },
    "Kobold": {
        "hp": 30,
        "at": 7,
        "go": 22
    },
    "Hobgoblin": {
        "hp": 45,
        "at": 5,
        "go": 25
    },
    "Owlin": {
        "hp": 10,
        "at": 10,
        "go": 30
    },
    "Dark Elf": {
        "hp": 30,
        "at": 7,
        "go": 27
    },
    "Goliath": {
        "hp": 50,
        "at": 5,
        "go": 35
    },
    "Minotaur": {
        "hp": 50,
        "at": 5,
        "go": 35
    },
    "Dragon": {
        "hp": 100,
        "at": 8,
        "go": 100
    },
    "Satyr": {
        "hp": 35,
        "at": 3,
        "go": 0
    },
    "Human": {
        "hp": 15,
        "at": 2,
        "go": 0
    },
    "Gnome": {
        "hp": 20,
        "at": 5,
        "go": 5
    }
}


def art1():
    print("""
}}}}}}#@@@@}}}@}}}}}@@@@@@@{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}%@@@@@@%@@@@@}#}}@@@
}}}}}}@@@@{}@@@@@@@@@@@@@@@@@@@#}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}@@}}}}}@@@@}}}}#@@
}}}}}#@@@@@@}}}{#}@}}{@@@@@@@#}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}@@{}}}@@@@}}}{@@@
}}}}}{@@@@}}}}}}}{#}}}}%}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}@@@@@@@@}}}}@@@
}}}}}%@@@}}}}}}%@@@@@@@@@@#}}}}}}}}}}}}}}}}}}](([))([}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}@@@@#}}}@@@
{}}}}@@@%}}}@%@@@@@@@@@@@@@@@@}}}}}}}^:::::::::::::::::-:-^(}}}}}}}}}}}}}}}}}}}}}}}}}}}}}{@@@#}}}#@@
}}}}}@@@@{}}}}}}}}}}}}}%@@@@@@@@@%*:::::::::::::::::::::-:::::*}}}}}}}}}}}}}}}}}}}}}}}}}}{@@@}%}}#@@
}}}}}@@@}}}}}}}}%@@@{#}%@@@@@@@@@@@@<~*:::::::::::::::::--:::::::=}}}}}}}}}}}}}}}}}}}}}}}#@@@}}}%@@@
}}}}}@@@}}}}}}}}{@@@@@@@@@{{>(]*([)^<)^~:::::::::::::::::::::::::::)}}}}}}{@%}}}}}}}}}}}}{@@@}}}}@@@
}}}}}@@%}}}}}}}}}}}}}}}}@}#[]=+==+==:::::::::::::=::::::::::::::~*)%@@@@@@@@@@@@%@#}}}}}}}@@@}}}}#@@
}}}}}@@@}}}}}}}}}}}}}}}{+:::~>^=*=-:::::::::::::::---::::::::::::-:<%%@@#}}}}}}}}}}}}}}}}{@@@}}}}#@@
}}}}#@@@}}}}}}}%#@@%@@@=~::=<=::-=+=-::::::::::::::::::::+::::+--+{@@@@@@@@}}}}}}}}}}}}}}#@@@}{%@@@@
{}}@@@@@}}{@@@}}}}}}}*::::::::::::::::::::::::::::::::::::::~<#%@@@@@@@{{]}}}}}}}}}}}@}}}@@@@}}}}@@@
%}}}@@@@@@@}}}}}}}}}+-*:~:::::::-~::::::::::::::::::::::::^[@@@#%([{@%>))#@@@@{}}}}}}}}%@@@@@}}}}@@@
}}}}@@@@{}}}}}}}}}}:::::::-::::~:::::::::::::::::::::::::::::::::^}}}}(::>*}{@}}}}}}}}}}]@@@@}}}}#@@
}}}}#@@@}}}}}}}}}}^-:::::::::-:::::::::::::::::::::::::::::::::::*}}}[=:::::}}}#}}}}}}}}]@@@@}}}}#@@
}}}}{@@@}}}{#}}}}}*=::::::::^::::::::::::::::::+@}:::::::::::::::]}}}}[^::::-}}}}}%{{}}}[@@@@}}}}@@@
@%##@@@{}}}}}}}}}>~:::::=:::::~:::::::::::::::}@@@}^:::::::::::::*+}}}}}^~:::]}}}}}}}#%@}[@@@}}}}#@@
}}}}@@@#}}}}}}}}[-::*~:-:::::*^::::::::::::::(@@@@@}::::::::::::~]}}}}}}[-::::}}}}}}}}}}}}%@@#}}}%@@
}}}}@@@@}}}}}}}}<:::=:::::-::(]::::::::::::::{@@@@@@):::::::::::::}}}}):::::::(}}}}}}}}}}{%@@{}}}#@@
}}}}@@@%}}}}}}}}::-:^+::::::-]}):::::::::::=]@@@@@@@@>+~::::::::::}}}}}<::::::*}}}}}}}}}}}@@@}}}}@@@
{}}}@@@#}}}}}}}}(:-:)[:::+=::(}*:::::::+}#@@@@@@@@@@@@%#(*~:::::*}}}}}}}})-:~+^}}}}}}}}}}}@@@#}}#@@@
#%}}@@@%}}}}}}}}}]^~[}(+:}):}}}}+::::::::::-@@@@@@@@@%*::::::::=]}}}}}}}}<=+}])}}}}}}{%@@[@@@@@@@@@@
@@@@@@@%}}}}}}}}}}]}}}}^:}}[}}}[:::::::::::(@@@@@@@@@@}^:::::::~(}}}}}}}}]>:[}[}}}%@@@@@@(@@@@@@@@@@
{{}}@@@#}}}}}}}}}}}}}}}[<}}>:}}}~>:-::::::+^[@@@@@@@@@@[-::::::::*}}}}}}}+<}}}{@@@@@@@@@%(@@@@@@@@@@
}}}}@@@%[}}}}}}}}}}}}}}}}}}}}}}[><:^::::::*#@@@@@@@@@@@@]-:::::^}}}}}}}}}[[}}}}#{###%%%{}@@@@@@@@@@@
}}}%@@@@[}}}}}}}}}}}}}}}}}}}}}}}[>]<::::)@@@@@@@@@@@@@@@@[::::=}}}[](]}{{}}}}}}}}%@@@@@@#@@@@@##{@@@
}}{%@@@@}}}}}}}}}}}}}}}}}}}}}}}}}}^^:::(@@@@@@@@@@@@@@@@@@%~*}}}[[}#@@@@@@@@@%}{@%%%{{@@@#@@@@{{{@@@
}}}@@@@%}}}}}}}}}}}}}}}}}}}}}}}}}}}]+:=]{@@@@@@@@@@@@@@@@@@<>}}}@@@@@@{}#}}}}#@@@@@@@%%%%}@@@@%{}@@@
@@@@@@@@}}}}}}}}}}}}}}}}}}}}}}}}}}}]<%#]@@@@@@@@@@@@@@@@@@@[:({}}{}}}}}}}}}}}}}}}}}}}}}}{[@@@@@@@@@@
#{@@@@@%{{}}}}}}}}}}}}}}}}}}}}}}}]#@@@}{@@@@@@@@@@@@@@@@@@@#*=]}}}}}}}}}}}}}}}}}}}{{}}}}#(@@@@@#{@@@
#}#@@@@[%}}}}}}}}}}}}}}}}}}}[[]}%@@@@@}@@@@@@@@@@%@@@@@@@@@@{}}}}}}}}}}}}}}}}}}}}}{{{}}}{(@@@@@#{@@@
{{#@@@%)%}}}}}}}}}}}}}}}}}}}[@@@@@@@@%{@@@@@@@@@@@@@@@@@@@@@@{}}}}}}}}}}}}}{}}}}}}}}{}}{{}{@@@@#{@@@
{}#@@@#)%}}}}#}}}#{}}}}}}}}}}}}@@@@@@#@@@@@@@@@@@@@@@@@@@@@@@%{}}}}}}}}}}}}}}{}}}}}}{{}}{}}@@@@{{@@@
{}%@@@@)#{}}}{}{%}}}}}}}}}}}}}}}}@#@@@@@@@@@@@@@@@@@@@@@@@@@@@}}}}}}}}}}}}}}}}}%@%}{{}}}{}{@@@@}{@@@
{}@@@@@<#}}}}#}#{}}}}}}}}}}}}}}}}{@@@@@@@@@@@@@@@@@@@@@@@@@@@}}}}}}}}}}}}}}}}}}}}#%{#{}}}}}@@@@#}@@@
#}@@@@@#@%@@@%#{}}}}}}}}}}}}}}}}}}@@@@@@@@@@@@@@@@@@@@@@@@}}}}}}}}}}}}}}}{}}}}}}}#{%@@@@@%@@@@@%}@@@
%{@@@@]#}}}}{%##}}}}}}}}}}}}}}}}}}}@@@@@@@@@@@@@@@@@@@@@@%}}}}}}}}}}}}}}}}}}}}}}}{{{{}}}}@%{@@@@{@@@
%%@@@@[<{}}}}%{{}}}}}}}}}}}}}}}}}}}}}#@@@@@@@@@@@@@@@@@@@%}}}}}}}}}}}}}}}}}}{}}}}}{{#}}}}{({@@@@{@@@
@@@@@@[{#}}}}%#{}}}}}}}}}}}}}}}}}}}}}}@@@@@@@@@@@@@@@@@@@#}}}}}}}}}}}}}}}}}}{}}}}}{%{{}}{%[@@@@@#@@@
@@@@@@#%@@{}{##}{}}}}}{}}}}}}}}}}}}}}}@@@@@@@@@@@@@@@@@@@%}}}}}}}}}}}}}}}#}}}{}}}}}%}{%@@%{@@@@@@@@@
@@@@@@#{@@@#{{##}}}}#%}}}}}}}}}}}}}}}}@@@@@@@@@@@@@@@@@@@#}}}}}}}}}}}}}}}{#}}#}}}}}}#@@@@}%@@@@@@@@@
@@@@@@#[@@@@@@{}}}}#}#}}}}}}}}}}}}}}}}@@@@@@@@@@@@@@@@@@@@}}}}}}}}}}}}}}{#}#{#}}{#%@@@@@@@[@@@@@@@@@
@@@@@@#@@@@@@@@@%#}}{%}}}{}}}}}}}}}}}}#@@@@@@@@@@@@@@@@@@@[}}}}}}}}}{}}}}##{{##%@@@@@@@@@@#%@@@@@@@@
@@@@@@[@@@@@@@@@@@#[}}}}}{}}}}{}}}}}}}{@@@@@@@@@@@@@@@@@@@[}}}}}{}}}}#}}}#{{}#@@@@@@@@@@@@#[@@@@@@@@
@@@@@@]@@@@@@#@@@@%%{}}#{}}}}}{}}#}}}}#@@@@@@@@@@@@@@@@@@@{}}}#}}{}}{#{{}}{{%@@@@@%%@@@@@@[%@@@@@@@@
@@@@@@]@@@@@@@@@@@@@%}}{{}}}{}{}#}}{}}#@@@@@@@@@@@@@@@@@@@}[}}}{}#}{{#}##}{%@@@@@@@{@@@@@@}@@@@@@@@@
@@@@@@}@@@@@@@@@@@@@@@@%}[}[}#}#}{{{}}#@@@@@@@@@@@@@@@@@@@@{{}}{}#}{}][}{%@@@@@@@@@@@@@@@@}@@@@@@@@@
@@@@@@@%@@@@@@@@@@@@@@@@@@%{}{#{#}{{}}@@@@@@@@@@@@@@@@@@@@@{{}}#}#}}[#%@@@@@@@@@@@@@@@@@@@{@@@@@@@@@
@@@@@@@@@@@@@@@@@}@@@@@@@@@@@#}}}{}{{{@@@@@@@@@@@@@@@@@@@@@@#}{#}}}#%@@@@@@@@@@}@@@@@@@@@#@@@@@@@@@@
@@@@@@@%@@@@@#{@@@@@@@@@@@@@@%#}}{}}#}@@@@@@@@@@@@@@@@@@@@@@@%#}{}}%@@@@@@[@@@@@@@##@@@@@@{@@@@@@@@@
@@@@@@}@@@@%@@@#}[#}@@@@@@@@@@%#}{{{{}@@@@@@@@@@@@@@@@@@@@@@@@{}{{%@@@@@@@@@@[%[{%%@@%@@@@}@@@@@@@@@
    """)


def clear():
    print(100 * "\n")


def draw():
    print("xX--------------------xX")


def save():
    list = [
        name,
        str(HP),
        str(ATK),
        str(pot),
        str(elix),
        str(gold),
        str(x),
        str(y),
        str(key)
    ]

    file = open("load.txt", "w")

    for item in list:
        file.write(item + "\n")
    file.close()


def heal(amount):
    global HP
    if HP + amount < HPMAX:
        HP += amount
    else:
        HP = HPMAX
    print(name + "'s HP refilled to " + str(HP) + "!")

def battle():
    global fight, play, run, HP, pot, elix, gold, boss, Friend, Limiter, x, y, currentLocX, currentLocY, currentCoords, townCoords

    if not boss:
        random_int = random.randint(1, 1000)
        if random_int < 25:
            enemy = random.choice(e_listEpic)
        elif random_int in range(25, 150):
            enemy = random.choice(e_listRare)
        elif random_int in range(150, 400):
            enemy = random.choice(e_listUncommon)
        else:
            if random_int > 400 and random_int % 7 == 0:
                enemy = random.choice(e_listFriendlys)
            else:
                enemy = random.choice(e_list)
    else:
        enemy = "Dragon"
    hp = mobs[enemy]["hp"]
    hpmax = hp
    atk = mobs[enemy]["at"]
    g = mobs[enemy]["go"]

    if enemy == ["Satyr", "Human", "Gnome"]:
        Friend = True

    while fight:
        clear()
        draw()
        if not Friend:
            print("Defeat the " + enemy + "!")
            draw()
            print(enemy + "'s HP: " + str(hp) + "/" + str(hpmax))
            print(name + "'s HP: " + str(HP) + "/" + str(HPMAX))
            print("POTIONS: " + str(pot))
            print("ELIXIR: " + str(elix))
            draw()
            print("1 - ATTACK")
            if pot > 0:
                print("2 - USE POTION (30HP)")
            if elix > 0:
                print("3 - USE ELIXIR (50HP)")
            draw()

        else:
            print("A " + enemy + " approaches you")
            draw()
            choice = input("# ")
            if enemy == "Satyr":
                print("\"These woods are not safe for your kind\"\n1: \"I must push forward\"\n2: Turn Back\n"+"3: Attack!")
                if choice == "1":
                    potionsgiven = random.randint(1, 4)
                    print("\"If you must, take these\"\n+"+str(potionsgiven)+" Potions Received")
                    pot += potionsgiven
                elif choice == "2":
                    Limiter = 1
                    fight = False
                elif choice == "3":
                    friend = False

            elif enemy == "Human":
                print("\"Thank goodness you're here!\"\n1: \"Who are you?\"\n2: \"Empty your pockets or I'll gut you like a fish\"")
                if choice == "1":
                    givename = nameList[random.randint(0,4)][random.randint(0,4)]
                    distance = str(int(math.dist(currentCoords,townCoords)))
                    direction = directionList[1]
                    if currentLocY-3 == 0:
                        if currentLocX-2>0:
                            direction = directionList[3]
                        else:
                            direction = directionList[7]
                    elif currentLocX-2 == 0:
                        if currentLocY-3>0:
                            direction = directionList[5]
                        else:
                            direction = directionList[1]
                    elif currentLocY-3>0:
                        if currentLocX-2>0:
                            direction = directionList[4]
                        else:
                            direction = directionList[6]
                    else:
                        if currentLocX-2>0:
                            direction = directionList[2]
                        else:
                            direction = directionList[8]
                    print("\"My name is "+givename+", I had too much mead last night and now I can't find the town!\"\n1: \"I'll help you, for a price\n2: The town is "+distance+" miles "+direction+"\n3: \"I'll take you there\"\n4: Fight!")
                    if choice == "1":
                        print("\"I don't have much, but you can have what's left\"")
                        goldgift=int(random.randint(1,5))
                        gold+=goldgift
                        print("You received "+str(goldgift)+" gold!")
                        fight = False
                    elif choice == "2":
                        fight = False
                    elif choice == "3":
                        x = 2
                        y = 3
                        currentCoords = [2,3]

            elif enemy == "Gnome":
                print("...")

        choice = input("# ")

        if choice == "1":
            hp -= ATK
            print(name + " dealt " + str(ATK) + " damage to the " + enemy + ".")
            if hp > 0:
                HP -= atk
                print(enemy + " dealt " + str(atk) + " damage to " + name + ".")
            input("> ")

        elif choice == "2":
            if pot > 0:
                pot -= 1
                heal(30)
                HP -= atk
                print(enemy + " dealt " + str(atk) + " damage to " + name + ".")
            else:
                print("No potions!")
            input("> ")

        elif choice == "3":
            if elix > 0:
                elix -= 1
                heal(50)
                HP -= atk
                print(enemy + " dealt " + str(atk) + " damage to " + name + ".")
            else:
                print("No elixirs!")
            input("> ")

        if HP <= 0:
            print(enemy + " defeated " + name + "...")
            draw()
            fight = False
            play = False
            run = False
            print("GAME OVER")
            input("> ")

        if hp <= 0:
            print(name + " defeated the " + enemy + "!")
            draw()
            fight = False
            gold += g
            print("You've found " + str(g) + " gold!")
            if random.randint(0, 100) < 30:
                pot += 1
                print("You've found a potion!")
            if enemy == "Dragon":
                clear()
                draw()
                art1()
                print("=======================================")
                print("=        CONGRATULATIONS!!!           =")
                print("==You've just beaten this awesome RPG!=")
                print("=======================================")
                print("==Please give me a star on GitHub======")
                print("=======================================")
                draw()
                boss = False
                play = False
                run = False
            input("> ")


def shop():
    global buy, gold, pot, elix, ATK

    while buy:
        clear()
        draw()
        print("Welcome to the shop!")
        draw()
        print("GOLD: " + str(gold))
        print("POTIONS: " + str(pot))
        print("ELIXIRS: " + str(elix))
        print("ATK: " + str(ATK))
        draw()
        print("1 - BUY POTION (30HP) - 5 GOLD")
        print("2 - BUY ELIXIR (MAXHP) - 8 GOLD")
        print("3 - UPGRADE WEAPON (+2ATK) - 10 GOLD")
        print("4 - LEAVE")
        draw()

        choice = input("# ")

        if choice == "1":
            if gold >= 5:
                pot += 1
                gold -= 5
                print("You've bought a potion!")
            else:
                print("Not enough gold!")
            input("> ")
        elif choice == "2":
            if gold >= 8:
                elix += 1
                gold -= 8
                print("You've bought an elixir!")
            else:
                print("Not enough gold!")
            input("> ")
        elif choice == "3":
            if gold >= 10:
                ATK += 2
                gold -= 10
                print("You've upgraded your weapon!")
            else:
                print("Not enough gold!")
            input("> ")
        elif choice == "4":
            buy = False


def mayor():
    global speak, key

    while speak:
        clear()
        draw()
        print("Hello there, " + name + "!")
        if ATK < 10:
            print("You're not strong enough to face the dragon yet! Keep practicing and come back later!")
            key = False
        else:
            print("You might want to take on the dragon now! Take this key but be careful with the beast!")
            key = True

        draw()
        print("1 - LEAVE")
        draw()

        choice = input("# ")

        if choice == "1":
            speak = False


def cave():
    global boss, key, fight

    while boss:
        clear()
        draw()
        print("Here lies the cave of the dragon. What will you do?")
        draw()
        if key:
            print("1 - USE KEY")
        print("2 - TURN BACK")
        draw()

        choice = input("# ")

        if choice == "1":
            if key:
                fight = True
                battle()
        elif choice == "2":
            boss = False


while run:
    while menu:
        print("1, NEW GAME")
        print("2, LOAD GAME")
        print("3, RULES")
        print("4, QUIT GAME")

        if rules:
            clear()
            draw()
            print("Rules!")
            draw()
            print("1. Use the Number Keys to Determine Where to Go!")
            print(
                "2. Be sure to not stray off too far in the early game, the end of the map is where the Orcs spawn the most!")
            print(
                "3. Don't spam the buttons! This could not only damage the scripts, but also your internal machine, we don't want that!")
            draw()
            print("Speedrunning!")
            draw()
            print("- The timer starts when you hit enter on the name select screen.")
            print("- The timer ends upon the last hit of fighting the dragon.")
            print("The current World Record is 1:25.48, can you beat it?!")
            draw()
            print("Press Enter to Continue...")
            rules = False
            choice = ""
            input("> ")
            clear()
        else:
            choice = input("# ")

        if choice == "1":
            clear()
            name = input("# What's your name, hero? ")
            menu = False
            play = True
        elif choice == "2":
            try:
                f = open("load.txt", "r")
                load_list = f.readlines()
                if len(load_list) == 9:
                    name = load_list[0][:-1]
                    HP = int(load_list[1][:-1])
                    ATK = int(load_list[2][:-1])
                    pot = int(load_list[3][:-1])
                    elix = int(load_list[4][:-1])
                    gold = int(load_list[5][:-1])
                    x = int(load_list[6][:-1])
                    y = int(load_list[7][:-1])
                    key = bool(load_list[8][:-1])
                    clear()
                    print("Welcome back, " + name + "!")
                    input("> ")
                    menu = False
                    play = True
                else:
                    print("Corrupt save file!")
                    input("> ")
            except OSError:
                print("No loadable save file!")
                input("> ")
        elif choice == "3":
            rules = True
        elif choice == "4":
            quit()

    while play:
        save()  # autosave
        clear()

        if not standing:
            if biom[map[y][x]]["e"]:
                if random.randint(0, 100) < 30:
                    fight = True
                    battle()

        if play:
            draw()
            print("LOCATION: " + biom[map[y][x]]["t"])
            draw()
            print("NAME: " + name)
            print("HP: " + str(HP) + "/" + str(HPMAX))
            print("ATK: " + str(ATK))
            print("POTIONS: " + str(pot))
            print("ELIXIRS: " + str(elix))
            print("GOLD: " + str(gold))
            print("COORD:", x, y)
            draw()
            print("0 - SAVE AND QUIT")
            dest = input("# ")

            if Limiter>0:
                if y > 0 and previousUsed != "1":
                    print("1 - NORTH")
                if x < x_len and previousUsed != "2":
                    print("2 - EAST")
                if y < y_len and previousUsed != "3":
                    print("3 - SOUTH")
                if x > 0 and previousUsed != "4":
                    print("4 - WEST")
                if pot > 0:
                    print("5 - USE POTION (30HP)")
                if elix > 0:
                    print("6 - USE ELIXIR (50HP)")
                if map[y][x] == "shop" or map[y][x] == "mayor" or map[y][x] == "cave":
                    print("7 - ENTER")

                if dest == "0":
                    play = False
                    menu = True
                    save()
                elif dest == "1" and previousUsed != "1":
                    if y > 0:
                        y -= 1
                    standing = False
                    currentLocY += 1
                    previousUsed = 1
                    Limiter -= 1
                elif dest == "2" and previousUsed != "2":
                    if x < x_len:
                        x += 1
                    standing = False
                    currentLocX += 1
                    previousUsed = 2
                    Limiter -= 1
                elif dest == "3" and previousUsed != "3":
                    if y < y_len:
                        y += 1
                    standing = False
                    currentLocY -= 1
                    previousUsed = 3
                    Limiter -= 1
                elif dest == "4" and previousUsed != "1":
                    if x > 0:
                        x -= 1
                    standing = False
                    currentLocX -= 1
                    previousUsed = 4
                    Limiter -= 1
                elif dest == "5":
                    if pot > 0:
                        pot -= 1
                        heal(30)
                    else:
                        print("No potions!")
                        input("> ")
                        standing = True
                elif dest == "6":
                    if elix > 0:
                        elix -= 1
                        heal(50)
                    else:
                        print("No elixirs!")
                        input("> ")
                        standing = True
                elif dest == "7":
                    if map[y][x] == "shop":
                        buy = True
                        shop()
                    if map[y][x] == "mayor":
                        speak = True
                        mayor()
                    if map[y][x] == "cave":
                        boss = True
                        cave()
                    else:
                        standing = True
            else:
                if y > 0:
                    print("1 - NORTH")
                if x < x_len:
                    print("2 - EAST")
                if y < y_len:
                    print("3 - SOUTH")
                if x > 0:
                    print("4 - WEST")
                if pot > 0:
                    print("5 - USE POTION (30HP)")
                if elix > 0:
                    print("6 - USE ELIXIR (50HP)")
                if map[y][x] == "shop" or map[y][x] == "mayor" or map[y][x] == "cave":
                    print("7 - ENTER")
                draw()

                if dest == "0":
                    play = False
                    menu = True
                    save()
                elif dest == "1":
                    if y > 0:
                        y -= 1
                    standing = False
                    currentLocY += 1
                elif dest == "2":
                    if x < x_len:
                        x += 1
                    standing = False
                    currentLocX += 1
                elif dest == "3":
                    if y < y_len:
                        y += 1
                    standing = False
                    currentLocY -= 1
                elif dest == "4":
                    if x > 0:
                        x -= 1
                    standing = False
                    currentLocX -= 1
                elif dest == "5":
                    if pot > 0:
                        pot -= 1
                        heal(30)
                    else:
                        print("No potions!")
                        input("> ")
                        standing = True
                elif dest == "6":
                    if elix > 0:
                        elix -= 1
                        heal(50)
                    else:
                        print("No elixirs!")
                        input("> ")
                        standing = True
                elif dest == "7":
                    if map[y][x] == "shop":
                        buy = True
                    shop()
                if map[y][x] == "mayor":
                    speak = True
                    mayor()
                if map[y][x] == "cave":
                    boss = True
                    cave()
                else:
                    standing = True