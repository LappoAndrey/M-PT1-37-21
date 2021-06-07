from random import randint 

class Creature:

    def __init__(self, health, min_attack, max_attack, min_defense, max_defense):
        self.health = health
        self.min_attack = min_attack
        self.max_attack = max_attack
        self.min_defense = min_defense
        self.max_defense = max_defense
       


class Hero(Creature):
    def __init__(self, health, min_attack, max_attack, min_defense, max_defense, chanse_crit):
        Creature.__init__(self, health, min_attack, max_attack, min_defense, max_defense)
        self.chanse_crit = chanse_crit


class Monster(Creature):
    def __init__(self):
        Creature.__init__(self, randint(10, 500), 25, 35, 0, 15)





def fight():
    die=''
    health=250
    min_attack=10
    max_attack=20
    min_defense=0
    max_defense=30
    chanse_crit=0

    H = Hero(health, min_attack, max_attack, min_defense, max_defense, chanse_crit)
    M = Monster()

    count = 1

    print(f"Hero find monster!")
    print(f"Monster have {M.health} health, attack {M.min_attack} - {M.max_attack}, defense {M.min_defense} - {M.max_defense}.")
    print(f"Hero have {H.health} health, attack {H.min_attack} - {H.max_attack}, defense {H.min_defense} - {H.max_defense}.")

    while H.health >= 0 and  M.health >= 0:
       
        H_defense = randint(H.min_defense, H.max_defense)
        M.attack  = randint(25, 35)
        H.health =  H.health +  H_defense  - M.attack
        if (M.attack - H_defense )>0:
            print(f"Monster atack! He made {M.attack} damage! Hero health {H.health}.")
        else:
            print(f"Monster atack! He made no damage! Hero laughed: 'AHAHAHAHA'.")
        if H.health<=0:
            break
        M.defense = randint(0, 10)
        H_attack  = randint(H.min_attack, H.max_attack)
        H.chanse_crit = randint(0, 100)
        
        if H.chanse_crit>50:
            print(f"==>>>Hero have a crit strike! His attack X2 {H_attack}!<<<===")
            H_attack=H_attack*2
        M.health =  M.health +  M.defense- H_attack
        if (H_attack - M.defense )>0:
            print(f"Hero atack! He made {H_attack} damage! Monster health {M.health}.")
        else:
            print(f"Hero atack! He made no damage! Monster laughed.")
            
        if M.health<=0 or H.health<=0:
            break
        count +=1

    if H.health > M.health:
        print(f"Hero has won! He made {count} strikes! Health left {H.health}.\n------------------------------------------")
        die='Monster'
        return   die

    else:
        print(f"Hero DIE! Monster has won! He made {count} strikes!  Health left {M.health}.\n------------------------------------------")
        die='Hero'
        return  die
   
    
print(fight())

        
    


