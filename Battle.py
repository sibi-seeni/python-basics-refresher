#   A program to demonstrate the creation and use of classes in Python by simulating a battle to defeat the evil Sauron.
#
# by: Sibi Seenivasan

import random

class Character():
    def __init__(self, name, hp, atk, defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense

    def attack(self, target):
        damage = max(0, self.atk - target.defense)
        target.hp -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage!\n")
        if target.hp <= 0:
            print(f"{target.name} has been defeated!\n")

    def show_status(self):
        print(f"{self.name}")
        print(f"HP: {self.hp}")
        print(f"ATK: {self.atk}")
        print(f"Defense: {self.defense}\n")

    def special_move(self, target):
        pass

class Hero(Character):
    def __init__(self, name, hp, atk, defense, role="Warrior"):
        super().__init__(name, hp, atk, defense)
        self.role = role

    def special_move(self, target):
        if self.role == "Healer":
            heal = random.randint(50, 60)
            target.hp += heal
            print(f"{self.name} uses Healing, restoring {heal} HP to {target.name} !\n")
        if self.role == "Warrior":
            print(f"{self.name} uses Valor and deals triple damage!\n")
            damage = max(0, (self.atk * 3) - target.defense)
            print(f"{self.name} attacks {target.name} for {damage} damage!\n")
            target.hp -= damage
            if target.hp <= 0:
                print(f"{target.name} has been defeated!\n")

class Monster(Character):
    def __init__(self, name, hp, atk, defense, role="Boss"):
        super().__init__(name, hp, atk, defense)
        self.role = role

    def special_move(self, target):
        if self.role == "Boss":
            target.atk = target.atk // 2
            print(f"{self.name} lets out a mighty roar, intimidating {target.name} and reducing their attack by {target.atk}!\n")

def main():
    hero1 = Hero("Aragorn", 75, 60, 10, "Warrior")
    hero2 = Hero("Gandalf", 150, 25, 15, "Healer")
    hero3 = Hero("Legolas", 80, 50, 8, "Warrior")
    hero4 = Hero("Gimli", 80, 40, 12, "Warrior")
    monster1 = Monster("Sauron", 225, 70, 20, "Boss")

    print("Initial Status:")
    hero1.show_status()
    hero2.show_status()
    hero3.show_status()
    hero4.show_status()
    monster1.show_status()
    print("\nBattle Begins!\n")

    hero1.attack(monster1)
    monster1.attack(hero1)
    hero2.special_move(hero1)
    hero3.attack(monster1)
    hero4.attack(monster1)
    monster1.attack(hero3)
    monster1.attack(hero4)
    monster1.special_move(hero1)
    monster1.attack(hero2)
    hero1.special_move(monster1)
    monster1.attack(hero1)
    hero3.attack(monster1)
    hero4.attack(monster1)
    monster1.attack(hero4)
    monster1.attack(hero3)
    hero2.attack(monster1)
    hero1.attack(monster1)

    print("Middle Earth has been SAVED! VICTORY!! \n")

if __name__ == "__main__":
    main()