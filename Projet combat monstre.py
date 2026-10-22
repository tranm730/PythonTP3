"""
Petit programme de jeu de combat monstre
Par: Mackenzy Tran
Classe: 404
"""


import random
import time


player_nb_enemy_encountered = 0
player_health = 20
player_attack = 3
player_escape_cost = 2
player_name = input("Choisi le nom de votre hero: ")
nb_escape = 0
nb_enemy_defeated = 0
nb_defeat = 0
enemy_list= [{"nom":"chevalier","hp":3,"attaque":1},
             {"nom":"magicien","hp":1,"attaque":3},
             {"nom":"chien de guarde","hp": 2,"attaque": 2}
]


def enemy_stat():
    """
    #Permet de definir le monstre rencontre
    :return:current_enemy
    """
    enemy_encounter = random.randint(0,2)
    current_enemy = enemy_list[enemy_encounter].copy()
    mob_difficulty = random.randint(1,4)
    current_enemy["hp"] += mob_difficulty
    current_enemy["attaque"] += mob_difficulty
    return current_enemy


def player_stat():
    """
    Fonction qui demontre les stat du joueur
    :return: None
    """
    print(f"Nom: {player_name}\t hp: {player_health}\t attaque: {player_attack}")


def fight():
    """
    # Fonction de combat tour par tour entre le joueur et l'ennemi
    :return:none
    """


    global active_enemy
    global player_health
    global player_attack
    global player_escape_cost
    global player_nb_enemy_encountered
    global nb_escape
    global nb_enemy_defeated


    time.sleep(1)
    print(f"\nnombre d'ennemi rencontre:{player_nb_enemy_encountered}")
    player_nb_enemy_encountered += 1
    print(f"\nUn {active_enemy["nom"]} est apparu.")
    while active_enemy["hp"] > 0 and player_health > 0:
        print(f"\n{active_enemy["nom"]}\n{active_enemy["hp"]} hp\t{active_enemy["attaque"]} attaque")
        print(f"\n{player_name} hp = {player_health}")
        choice = input(f"Que veut tu faire?\nattaque ({player_attack} dommage,ecris 1)\t s'enfuir ({player_escape_cost} hp(ecris 2)\t voire stat/regle(ecris 3): ").lower()
        time.sleep(1)

        if choice == "1":
            active_enemy["hp"] -= player_attack
            print(f"\nTu a fait {player_attack} dommage")

            if active_enemy["hp"] > 0:
                player_health -= active_enemy["attaque"]
                print(f"\nLe {active_enemy["nom"]} a fait {active_enemy["attaque"]} dommage")

            else:
                player_health += 3
                nb_enemy_defeated += 1
                print(f"\nVous avez vaincu le {active_enemy["nom"]}")

        elif choice == "2":
            player_health -= 2
            nb_escape += 1
            print(f"\nTu est enfuis du {active_enemy["nom"]}, tu a perdu 2 hp, tu a maintenant {player_health} hp.")
            active_enemy["hp"] = 0

        elif choice == "3":
            player_stat()
            print("\nVoici les regles du jeu, tu commence avec 20 hp, en battant un monstre tu recois 3 hp, si tu survie 10 round tu gagne la partie, si tu meurt avant avoir survecu 10 round tu a perdu.")
            time.sleep(10)

        else:
            print(f"\nTu a ecris un autre truc que 1, 2 et 3, reesaye.")


print(f"La partie commence")
while player_health > 0 and player_nb_enemy_encountered != 10:
    active_enemy = enemy_stat()
    fight()

if player_nb_enemy_encountered == 10 and player_health > 0:
    # exigeance pour gagner la partie
    print(f"\nVous avez gagner la partie, bravo!")
    print(f"Vous etes enfuis {nb_escape} fois, vous avez vaincu {nb_enemy_defeated} ennemi/s et vous avez perdu {nb_defeat}fois ")


else:
    # defaite du joueur
    nb_defeat += 1
    print(f"\nVous avez perdu la partie, bien essaye!")
    print(f"Vous etes enfuis {nb_escape} fois, vous avez vaincu {nb_enemy_defeated} ennemi/s et vous avez perdu {nb_defeat} fois ")









