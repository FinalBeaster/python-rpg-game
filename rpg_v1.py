# Game System , Critical Hits , Heavy Attacks , Heal , Name And More
import random

ply_hlt=100
bs_hlt=120
turn=1

print("👋 Welcome To RPG Game By FinalBeaster 🕹️")
name=input("Enter Player Name : ")

while ply_hlt>0 and bs_hlt>0:
    print("\n=============================")
    print("Turn ",turn)
    print("=============================")
    print(f"{name} Health : {ply_hlt}")
    print("Boss Health : ",bs_hlt)
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
    if choice == 1:
        ply_dmg = random.randint(10,30)
        bs_dmg = random.randint(10,30)
        crit=random.randint(1,5)
        if crit==1:
            ply_dmg +=15
            print("[ CRITICAL HIT ! ]")
        print(name,"Did",ply_dmg,"Amount Of Damage To Boss")
        bs_hlt -= ply_dmg
        if bs_hlt>0:
            ply_hlt -= bs_dmg
            print("Boss Did",bs_dmg,"Amount Of Damage To",name)
        turn+=1
    elif choice == 2:
        if ply_hlt<100:
            ply_hlt += 15
            print(name,"Healed 15 Amount Of Health")
            bs_dmg = random.randint(5,20)
            turn+=1
        else:
            print('Wrong Choice !\n',name ,"Health Was Full ")
            bs_dmg = random.randint(1,5)
        if ply_hlt>100:
            ply_hlt=100
        ply_hlt -= bs_dmg
        print(f"But Boss Did {bs_dmg} Amount Of Damage To {name}")
        if bs_hlt<0:
            bs_hlt=0
    elif choice == 3:
        ply_dmg = random.randint(30,50)
        bs_dmg = random.randint(10,30)
        miss=random.randint(1,2)
        if miss==1:
            print("HEAVY ATTACK MISSED !")
            ply_hlt-=bs_dmg
        else:
            bs_hlt-=ply_dmg
            print("Heavy Attack dealt ", ply_dmg ,"To Boss")
            if bs_hlt>0:
                ply_hlt-=bs_dmg
        print("Boss Did",bs_dmg,"To",name)
    else:
        print("Invalid Choice \nTry Again")
        continue
    if bs_hlt<=0:
        print(name,"Defeated The Boss ")
        break
    elif ply_hlt<=0:
        print(name ,"Got Killed By The Boss")