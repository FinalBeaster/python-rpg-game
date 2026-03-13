# Added Heal Limit , Rage , Turn Counter , Defend , Critical
# Fixed Text , Minor Errors
import random
ply_hlt=100
bs_hlt=120
counter=1
heal=5
print(" 🗡️ Welcome To Text RPG Game 🎮 ")

while ply_hlt>0 and bs_hlt>0:
	print("Turn",counter)
	print("Player Health",ply_hlt)
	if bs_hlt>40:
		print("Boss Health",bs_hlt)
	else:
		print("Boss Health [RAGE]",bs_hlt)
	print("1.Attack")
	print("2.Heal (10-30 HP) [ Remaining : ",heal)
	print("3.Defend (+5 HP) ")
	choice=int(input("Enter You Choice :"))
	if choice==1:
		crit=random.randint(1,5)
		ply_dmg=random.randint(15,25)
		if crit==1:
			ply_dmg+=5
			bs_hlt-=ply_dmg
			print("CRITICAL HIT \nYou did ",ply_dmg,"points of damage")
		else:
			bs_hlt-=ply_dmg
			print("You did ",ply_dmg,"points of damage")
		if bs_hlt>0:
			if bs_hlt>40:
				bs_dmg=random.randint(10,25)
				ply_hlt-=bs_dmg
				print("Boss did ",bs_dmg,"points of damage to you")
			else:
				bs_dmg=random.randint(20,30)
				ply_hlt-=bs_dmg
				print("Boss is in RAGE \nHe did ",bs_dmg,"points of damage to you")
			counter+=1
	elif choice==2:
		if heal>0:
			ply_heal=random.randrange(10,31,5)
			bs_heal=random.randrange(10,21,5)
			ply_hlt+=ply_heal
			heal-=1
			print("You heal by",ply_heal,"points")
			if bs_hlt<120:
				bs_hlt+=bs_heal
				print("But boss also healed for",bs_heal,"points")
			else:
				bs_dmg=random.randint(15,35)
				ply_hlt-=bs_dmg
				print("Boss was on full help\nBoss did",bs_dmg,"points of damage")
				counter+=1
		else:
			print("Out Of Heals")
			print("Turn not counted. No action taken.")
	elif choice==3:
		ply_hlt+=5
		print("You healed by 5 points")
		if bs_hlt<40:
			def_dmg=random.randint(1,7)
			print("CRITICAL HIT \nDefend Took Hit \nBoss did",def_dmg,"to you")
		else:
			def_dmg=random.randint(1,5)
			print("Defend Took Hit \nBoss did",def_dmg,"to you")
		ply_hlt-=def_dmg
		counter+=1
	else:
		print("Invalid Choice")
		print("Turn not counted. No action taken.")
	if ply_hlt>100:
		ply_hlt=100
	if bs_hlt>120:
		bs_hlt=120
	print("\n\n")
if ply_hlt<=0:
	print("You Lose 💀")
else:
	print("You deafeated the boss 🏆")