from random import random

diceOptions=list(range(1,7))

#Weapons Array
weapons=["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

#Display available weapons
print("Available options:", ','.join(weapons))

def get_combat_strength(prompt):
    while True:
        try:
            value=int(input(prompt))
            if 1 <=value<=6:
                return value
            else:
                print("Invalid input! Please enter a number between 1 and 6")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 6")
combatStrength=get_combat_strength("Enter your combat strength (1-6):")
mCombatStrength=get_combat_strength("Enter your combat strength (1-6):")

for j in range (1, 21, 2):
    heroRoll=range.choice(diceOptions)
    monsterRoll=random.choice(weapons)

    heroWeapon=weapons[heroRoll-1]
    monsterWeapon=weapons[monsterRoll-1]

    heroTotal=combatStrength+heroRoll
    monsterTotal=mCombatStrength+monsterRoll

    print(f"\n Hero rolled {heroRoll}, Monster rolled {monsterRoll}")
    print(f"\n Hero selected {heroTotal}, Monster selected {monsterWeapon}")
    print(f"\n Hero total Strength: {heroTotal}, Monster total Strength: {monsterTotal}")

    #Determine the winner

    if heroTotal>monsterTotal:
        print("Hero wins")
    elif heroTotal<monsterTotal:
        print("Monster wins")
    else:
        print("It's a tie!")

if j !=11:
    print(f"\n Battle concluded after 20 rounds!")