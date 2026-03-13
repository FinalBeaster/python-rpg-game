# Game System , Critical Hits , Heavy Attacks , Heal , Name And More
# Added New Enemies , Balancing Game Attack , No Negative Health
# Battle Stage System , Fixing Minor Bugs , Balancing The Game
# Player Dictionary , XP System , Level System , Level Up Rewards
import random

goblin={
    "name":"Goblin",
    "health":45,
    "minattack":5,
    "maxattack":12,
    "xp":10
}

skeleton={
    "name":"Skeleton",
    "health":60,
    "minattack":8,
    "maxattack":15,
    "xp":18
}

orc={
    "name":"Orc",
    "health":85,
    "minattack":12,
    "maxattack":20,
    "xp":30
}

total_enemy=[goblin,skeleton,orc]
battle = 1
next_level_xp=40

print("👋 Welcome To RPG Game By FinalBeaster 🕹️")
name=input("Enter Player Name : ")

player={
    "name":name,
    "health":100,
    "maxhp":100,
    "xp":0,
    "level":1,
    "minattack":8,
    "maxattack":18
}

while battle<=5 and player["health"]>0:
    enemy=random.choice(total_enemy).copy()
    turn=1
    print("\nA Wild",enemy["name"],"Appeared !")
    if enemy["name"] == "Goblin":
        print("The Goblin grins mischievously.")
    elif enemy["name"] == "Skeleton":
        print("Bones rattle as the Skeleton approaches.")
    elif enemy["name"] == "Orc":
        print("The Orc roars angrily!")
    stopage=input("\nPress Enter")

    while player["health"]>0 and enemy["health"]>0:
        print("\n----------------------------")
        print(f"[ BATTLE {battle} ]  >>>  Turn {turn}")
        # print("Battle ",battle ,"=>🧬 Turn ",turn)
        print("-"*28)
        print(f'{name} Health : {player["health"]}')
        print(enemy["name"],"Health : ",enemy["health"])
        print("\nSelect Move")
        print(f'1.Attack({player["minattack"]}-{player["maxattack"]})')
        print("2.Heal (+12)")
        print(f'3.Heavy Attack ({(player["minattack"]+14)}-{(player["maxattack"]+14)} damage but 50% miss)')
        choice_select=input("Enter Choice : ")
        if not choice_select.isdigit():
            print("Invalid Choice")
            continue
        else:
            choice=int(choice_select)
        emy_dmg = random.randint(enemy["minattack"],enemy["maxattack"])
        if choice == 1:
            ply_dmg = random.randint(player["minattack"],player["maxattack"])
            crit=random.randint(1,5)
            if crit==1:
                ply_dmg +=10
                print("[ CRITICAL HIT ! ]")
            print(name,"Did",ply_dmg,"Amount Of Damage To",enemy["name"])
            enemy["health"] -= ply_dmg
            if enemy["health"]>0:
                player["health"] -= emy_dmg
                print(enemy["name"],"Did",emy_dmg,"Amount Of Damage To",name)
            turn+=1
        elif choice == 2:
            if player["health"]<player["maxhp"]:
                player["health"] += 12
                print(name,"Healed 12 Amount Of Health")
            else:
                print('Wrong Choice !\n',name ,"Health Was Full ")
            if player["health"]>player["maxhp"]:
                player["health"]=player["maxhp"]
            if emy_dmg>20:
                emy_dmg-=10
            elif emy_dmg<20 and emy_dmg>10:
                emy_dmg-=5
            else:
                emy_dmg-=3
            if emy_dmg<0:
                emy_dmg=1
            player["health"] -= emy_dmg
            print(f'But {enemy["name"]} Did {emy_dmg} Amount Of Damage To {name}')
            turn+=1
        elif choice == 3:
            ply_dmg = random.randint((player["minattack"]+14),(player["maxattack"]+14))
            miss=random.randint(1,2)
            if miss==1:
                print("HEAVY ATTACK MISSED !")
                emy_dmg=int(emy_dmg*1.5)
                player["health"]-=emy_dmg
                print("Heavy attack miss → enemy deal 1.5× damage")
                print("",enemy["name"],"Did",emy_dmg,"damage To",name)
            else:
                enemy["health"]-=ply_dmg
                print("Heavy Attack dealt", ply_dmg ,"damage To",enemy["name"])
                if enemy["health"]>0:
                    player["health"]-=emy_dmg
                    print("But",enemy["name"],"Did",emy_dmg,"damage To",name)
            turn+=1
        elif choice==999:
            player["health"]-=emy_dmg*4
            print("\n\nYou Got Damage of :",emy_dmg*4)
        else:
            print("Invalid Choice \nTry Again")
            continue

        #Admin Access
        if player["name"]=="ADMIN12":
            player["health"]=100


        if enemy["health"]<0:
                enemy["health"]=0
        if player["health"]<=0:
            print("\n",name,"got killed by ",enemy["name"])
            print("And Lost!")
            break
        if enemy["health"]<=0:
            print("\n\n")
            print(name,"Defeated",enemy["name"])
            print("-"*28)
            player["xp"]+=enemy["xp"]
            print("Gained", enemy["xp"],"XP")
            battle+=1
            break
    if player["xp"]>=next_level_xp:
        player["level"]+=1
        print("\n")
        print("Level Up!")
        print("You Are Now Level",player["level"])
        player["minattack"]+=3
        player["maxattack"]+=3
        player["maxhp"]+=10
        player["health"]=player["maxhp"]
        print("Max Health Increased by 10 \nAttack Increased By 3")
        print("\nYou Have Been Fully Healed")
        next_level_xp+=40
if player["health"]>0:    
    print("\n\nYou Defeated All Enemies 👹\nGood Job 👍")
        