# Game System , Critical Hits , Heavy Attacks , Heal , Name And More
# Added New Enemies , Balancing Game Attack , No Negative Health
# Battle Stage System , Fixing Minor Bugs , Balancing The Game
# Player Dictionary , XP System , Level System , Level Up Rewards
# Added Boss , Inventory , Better Messages , Balancing The Game , Random Loot
# Save File , Load File
import random
import pickle
import os

os.makedirs("rpg game", exist_ok=True)

def save_game():
    data={
        "player":player,
        "next_level_xp":next_level_xp,
        "heal":heal,
        "battle":battle,
        "turn":turn
    }

    with open("rpg game/savedata.dat","wb") as file:
        pickle.dump(data,file)

    print("Game Saved !")
    stopage=input("Press Enter")

def load_game():
    global player , next_level_xp , heal , battle , turn
    if os.path.exists("rpg game/savedata.dat"):
        with open("rpg game/savedata.dat","rb") as file:
            data = pickle.load(file)
        
        player = data["player"]
        next_level_xp = data["next_level_xp"]
        heal = data["heal"]
        battle = data["battle"]
        turn = data["turn"]

        print("Game Loaded !")
        stopage=input("Press Enter\n")
        return True
    else:
        print("Save Not Founded")
        stopage=input("Press Enter\n")
        return False

goblin={
    "name":"Goblin",
    "health":40,
    "minattack":4,
    "maxattack":10,
    "xp":10,
    "drop":"potion"
}

skeleton={
    "name":"Skeleton",
    "health":50,
    "minattack":7,
    "maxattack":13,
    "xp":18,
    "drop":"bomb"
}

orc={
    "name":"Orc",
    "health":80,
    "minattack":10,
    "maxattack":17,
    "xp":30,
    "drop":"mega potion"
}

dragon={
    "name":"𝐅𝐋𝐀𝐌𝐄 𝐃𝐑𝐀𝐆𝐎𝐍",
    "health":180,
    "minattack":16,
    "maxattack":28,
    "xp":100,
    "drop":"dragon fragment"
}

total_enemy=[goblin,skeleton,orc]
battle = 1
next_level_xp=40
heal=5

turn=1

out=1
while out==1:
    newgame_entered=input("Start New Game (Yes/No) :")
    newgame = newgame_entered.lower()
    if newgame == "yes":
        print("Are You Sure ! It will erase old save permanently")
        sure_entered = input("Yes/No :")
        sure=sure_entered.lower()
        if sure == "yes":
            out=0
            print("New Game Started !")
            print("👋 Welcome To RPG GAME By FinalBeaster 🕹️")
            name=input("Enter Player Name : ")
        elif sure == "no":
            continue
        else:
            print("Invalid Input")
            continue
    elif newgame == "no":
        print("You Want to Load Old Game")
        sure_entered= input("Yes/No :")
        sure = sure_entered.lower()
        if sure=="yes":
            a=load_game()
            if a==True:
                out=0
            elif a==False:
                out =1
        elif sure == "no":
            continue
        else:
            print("Invalid Input")
            continue

player={
    "name":name,
    "health":100,
    "maxhp":100,
    "xp":0,
    "level":1,
    "minattack":8,
    "maxattack":18,
    "inventory":[]
}

while battle<=5 and player["health"]>0:
    if out == 9:
        break            
    if battle == 5:
        enemy=dragon.copy()
    else:
        enemy=random.choice(total_enemy).copy()
        enemy["health"]+=(battle*5)
    if not enemy["name"]=="𝐅𝐋𝐀𝐌𝐄 𝐃𝐑𝐀𝐆𝐎𝐍":
        print("\n","-"*28)
        print("A Wild",enemy["name"],"Appeared !")
    if enemy["name"] == "Goblin":
        print("The Goblin grins mischievously.")
    elif enemy["name"] == "Skeleton":
        print("Bones rattle as the Skeleton approaches.")
    elif enemy["name"] == "Orc":
        print("The Orc roars angrily!")
    elif enemy["name"] == "𝐅𝐋𝐀𝐌𝐄 𝐃𝐑𝐀𝐆𝐎𝐍" :
        print("="*28)
        print("\n🔥 ⚔️ 𝐅𝐋𝐀𝐌𝐄 𝐃𝐑𝐀𝐆𝐎𝐍 ⚔️  APPEARS 🔥")
        print("The Lord Of Flame have Entered The Arena\n")
    print("="*28)
    stopage=input("\nPress Enter")

    while player["health"]>0 and enemy["health"]>0:
        if out == 9:
            break
        if player["health"]>player["maxhp"]:
            player["health"]=player["maxhp"]
        print("\n----------------------------")
        print(f"[ BATTLE {battle} ]  >>>  Turn {turn}")
        # print("Battle ",battle ,"=>🧬 Turn ",turn)
        print("-"*28)
        print(f'{name} Health : {player["health"]}')
        print(enemy["name"],"Health : ",enemy["health"])
        print("\nSelect Move")
        print(f'1.Attack({player["minattack"]}-{player["maxattack"]})')
        print(f'2.Heal (+18) [Quantity:{heal}]')
        print(f'3.Heavy Attack ({(player["minattack"]+14)}-{(player["maxattack"]+14)} damage but 50% miss)')
        print("4.Use Items (Access Inventory)")
        print("0.Exit (Save Game)")
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
                print("💥 CRITICAL HIT! Massive damage!")
            print(name,"Did",ply_dmg,"Amount Of Damage To",enemy["name"])
            enemy["health"] -= ply_dmg
            if enemy["health"]>0:
                player["health"] -= emy_dmg
                print(enemy["name"],"Did",emy_dmg,"Amount Of Damage To",name)
            turn+=1
        elif choice == 2:
            if player["health"]<player["maxhp"] and heal>0:
                player["health"] += 18
                print(name,"Healed 18 Amount Of Health")
                heal-=1
            elif player["health"]<player["maxhp"] and heal==0:
                print("Out Of Heal!")
                continue
            else:
                print('Wrong Choice !\n',name ,"Health Was Full ")
                print("Game Punished You For Your Wrong Decision")
            if player["health"]>player["maxhp"]:
                player["health"]=player["maxhp"]
            if emy_dmg>20:
                emy_dmg-=10
            elif emy_dmg<20 and emy_dmg>10:
                emy_dmg-=5
            else:
                emy_dmg-=3
            if emy_dmg<0:
                emy_dmg = 1
            player["health"] -= emy_dmg
            print(f' {enemy["name"]} Did {emy_dmg} Amount Of Damage To {name}')
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
        elif choice==4:
            if len(player["inventory"])==0:
                print("\n\n")
                print("Inventory Empty !")
                print("-"*20)
                stopage=input("Press Enter")
                continue
            else:
                print("Inventory :",player["inventory"])
                items_entering=input("Enter Choice (Name of Item) :")
                items=items_entering.lower()
                if items in player["inventory"]:
                    if items=="potion":
                        player["inventory"].remove("potion")
                        player["health"]+=20
                        print(player["name"],"healed 20 HP by using Potion")
                    elif items=="bomb":
                        player["inventory"].remove("bomb")
                        enemy["health"]-=20
                        print("Bomb Dealth 20 Damage To",enemy["name"])
                        print(enemy["name"],"Stunned!")
                    elif items=="mega potion":
                        player["inventory"].remove("mega potion")
                        player["health"]+=40
                        print(player["name"],"healed 40 HP by using Mega Potion")
                    else:
                        print("Invalid Choice [Check Spell Mistake]")
                        continue
                else:
                    print("Not In Inventory")
                    continue
                turn+=1

        elif choice==0:
            print("Are You Sure To Exit")
            sure_entered=input("Yes/No :")
            sure=sure_entered.lower()
            if sure == "yes":
                save_game()
                out=9
                continue
            elif sure == "no":
                continue
            else:
                print("Invalid Input")
                continue
        # Inventory Check
        elif choice==9999:
            player["inventory"].append(enemy["drop"])
            continue
            

        # Death Result    
        elif choice==999:
            player["health"]-=emy_dmg*4
            print("\n\nYou Got Damage of :",emy_dmg*4)
        
        # While Ending Loop
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
            player["health"]+=15
            print("You catch your breath and recover 15 HP")
            print("-"*28)
            luck=random.randint(1,2)
            if enemy["name"]=="𝐅𝐋𝐀𝐌𝐄 𝐃𝐑𝐀𝐆𝐎𝐍":
                print(enemy["name"],"Dropped A",enemy["drop"])
                print("You Picked It Up In Inventory !")
                player["inventory"].append(enemy["drop"])
            elif luck==1:
                print(enemy["name"],"Dropped A",enemy["drop"])
                print("You Picked It Up In Inventory !")
                player["inventory"].append(enemy["drop"])
            print("-"*28)
            player["xp"]+=enemy["xp"]
            print("Gained", enemy["xp"],"XP")
            battle+=1
            print("\n")
            save_game()
            break
    while player["xp"]>=next_level_xp:
        player["level"]+=1
        print("\nLevel Up!")
        print("You Are Now Level",player["level"])

        player["minattack"]+=2
        player["maxattack"]+=2
        player["maxhp"]+=8
        player["health"]=player["maxhp"]

        print("\n" + "✨"*10)
        print("⚡ LEVEL UP! ⚡")
        print(f'{player["name"]} reached Level {player["level"]}!')
        print("Your power surges through your body!")
        print("Attack +2")
        print("Max HP +8")
        print("You feel completely refreshed!")
        print("✨"*10)

        next_level_xp+=40

if out != 9:
    if player["health"]>0:    
        print("\n\nYou Defeated All Enemies 👹\nGood Job 👍")
        