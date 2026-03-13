# Game System , Critical Hits , Heavy Attacks , Heal , Name And More
# Added New Enemies , Balancing Game Attack , No Negative Health
import random

goblin={
    "name":"Goblin",
    "health":30,
    "minattack":4,
    "maxattack":10
}

skeleton={
    "name":"Skeleton",
    "health":40,
    "minattack":6,
    "maxattack":12
}

orc={
    "name":"Orc",
    "health":60,
    "minattack":10,
    "maxattack":16
}

total_enemy=[goblin,skeleton,orc]
enemy=random.choice(total_enemy).copy()
ply_hlt=100
turn=1

print("👋 Welcome To RPG Game By FinalBeaster 🕹️")
name=input("Enter Player Name : ")

print("\nA Wild",enemy["name"],"Appeared !")
if enemy == goblin:
    print("The Goblin grins mischievously.")
elif enemy == skeleton:
    print("Bones rattle as the Skeleton approaches.")
elif enemy == orc:
    print("The Orc roars angrily!")
stopage=input("Press Enter")

while ply_hlt>0 and enemy["health"]>0:
    print("\n=============================")
    print("Turn ",turn)
    print("=============================")
    print(f"{name} Health : {ply_hlt}")
    print(enemy["name"],"Health : ",enemy["health"])
    print("\nSelect Move")
    print("1.Attack(10-30)")
    print("2.Heal (+15)")
    print("3. Heavy Attack (30-50 damage but 50% miss)")
    choice_select=input("Enter Choice : ")
    if not choice_select.isdigit():
        print("Invalid Choice")
        continue
    else:
        choice=int(choice_select)
    emy_dmg = random.randint(enemy["minattack"],enemy["maxattack"])
    if choice == 1:
        ply_dmg = random.randint(10,25)
        crit=random.randint(1,5)
        if crit==1:
            ply_dmg +=15
            print("[ CRITICAL HIT ! ]")
        print(name,"Did",ply_dmg,"Amount Of Damage To",enemy["name"])
        enemy["health"] -= ply_dmg
        if enemy["health"]>0:
            ply_hlt -= emy_dmg
            print(enemy["name"],"Did",emy_dmg,"Amount Of Damage To",name)
        turn+=1
    elif choice == 2:
        if ply_hlt<100:
            ply_hlt += 15
            print(name,"Healed 15 Amount Of Health")
            turn+=1
        else:
            print('Wrong Choice !\n',name ,"Health Was Full ")
        if ply_hlt>100:
            ply_hlt=100
        if emy_dmg>20:
            emy_dmg-=10
        elif emy_dmg<20 and emy_dmg>10:
            emy_dmg-=5
        else:
            emy_dmg-=3
        if emy_dmg<0:
            emy_dmg=1
        ply_hlt -= emy_dmg
        print(f'But {enemy["name"]} Did {emy_dmg} Amount Of Damage To {name}')
    elif choice == 3:
        ply_dmg = random.randint(30,45)
        miss=random.randint(1,2)
        if miss==1:
            print("HEAVY ATTACK MISSED !")
            ply_hlt-=emy_dmg
        else:
            enemy["health"]-=ply_dmg
            print("Heavy Attack dealt ", ply_dmg ,"To",enemy["name"])
            if enemy["health"]>0:
                ply_hlt-=emy_dmg
                print(enemy["name"],"Did",emy_dmg,"To",name)
        turn+=1
    else:
        print("Invalid Choice \nTry Again")
        continue
    if enemy["health"]<0:
            enemy["health"]=0
    if enemy["health"]<=0:
        print(name,"Defeated",enemy["name"])
        break
    elif ply_hlt<=0:
        print(name ,"Got Killed By The",enemy["name"])