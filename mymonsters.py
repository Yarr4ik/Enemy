from monsters import NPCs
import random

def Enemy1():
    print("#####################################################################")

    desert_monster = NPCs("Enemy: Pustinya", "100", "Whatch out, here i come")

    print(desert_monster.get_name())
    print(desert_monster.get_speech())

    desert_monster.set_HP(100)
    desert_monster.take_damage(random.randint(20,50))
    desert_monster.speak("no pls nooo noooo")
    print(desert_monster.get_HP())
    ##desert_monster.set_name("Pustinya")
    ##desert_monster.set_HP("100HP")
    ##desert_monster.set_speech("Whatch out, here i come")
    ##desert_monster.describe()

def Enemy2():
    print("#####################################################################")

    woody_monster = NPCs("Enemy: Rust", "750", "I HA HA HUI")

    print(woody_monster.get_name())
    print(woody_monster.get_speech())

    woody_monster.set_HP(750)
    woody_monster.take_damage(random.randint(70,250))
    print(woody_monster.get_HP())
    ##woody_monster.set_name("Pustinya")
    ##woody_monster.set_HP("100HP")
    ##woody_monster.set_speech("Whatch out, here i come")

    ##woody_monster.describe()
def Enemy3():
    print("#####################################################################")

    fluffy_monster = NPCs("Enemy: Daria", "25", "oh noo +&/()&/&&%+*ç%")

    print(fluffy_monster.get_name())
    print(fluffy_monster.get_speech())

    fluffy_monster.set_HP(100)
    fluffy_monster.take_damage(random.randint(1,10))
    print(fluffy_monster.get_HP())
    ##fluffy_monster.set_name("Pustinya")
    ##fluffy_monster.set_HP("100HP")
    ##fluffy_monster.set_speech("Whatch out, here i come")
    ##fluffy_monster.describe()

    print("#####################################################################")

def Met_Enemy():
    

    x = random.randint(1,3)
    if x == 1:
        Enemy1()
    elif x == 2:
        Enemy2()
    elif x == 3:
        Enemy3()


while True:
    player_name = input("Player name:")


    health = random.randint(75,150)
    damage = random.randint(30,80)
    print("your name is", player_name, ",you have", health, "HP", "and", damage, "damage")

    choose = input("Enter 1 if you want to find adventures on yuor ass or enter 2 if you want to quit:")


    if choose == 1:
        Met_Enemy()
    else:
        
