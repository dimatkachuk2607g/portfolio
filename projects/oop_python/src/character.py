"""
Represents a character with attributes for name, age, attack, defense, and health
and methods for attacking, healing, and displaying details via __str__.
"""

class Character:
    def __init__(self, name:str, age:int, attack:int, defense:int, health:int):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Age must be a positive integer")
        if not isinstance(attack, int) or attack < 0:
            raise ValueError("Attack must be a positive integer")
        if not isinstance(defense, int) or defense < 0:
            raise ValueError("Defense must be a positive integer")
        if not isinstance(health, int) or health < 0:
            raise ValueError("Health must be a positive integer")


        self.name = name
        self.age = age
        self.attack = attack
        self.defense = defense
        self.__health = health


    @property
    def health(self):
        return self.__health


    @health.setter
    def health(self, new_health:int):
        if new_health < 0:
            self.__health = 0
        else:
            self.__health = new_health


    def take_damage(self, amount:int):
        damage = max(0, amount - self.defense)
        self.health -= damage
        return f'{self.name} took {damage} damage, remaining health: {self.health}'


    def attack_target(self, target:"Character"):
        target.take_damage(self.attack)
        return f'{self.name} attacks {target.name} for {self.attack} damage'


    def heal(self, amount:int):
        self.health += amount
        return f'{self.name} healed for {amount}, health is now {self.health}'


    def is_alive(self):
        return self.health > 0


    def __str__(self):
        return f'''\
Character Name: {self.name}
Character Age: {self.age}
Character Attack: {self.attack}
Character Defense: {self.defense}
Character Health: {self.health}
'''






def main():
    """Sample fight between two characters"""
    aragon = Character("Aragon", 45, 20, 5, 80)
    goblin = Character("Goblin", 20, 8, 3, 20)

    print("\nInitialize both characters:")
    print("-" * 40)
    print(aragon)
    print(goblin, end="")
    print("-" * 40 ,"\n\n")

    battle_counter = 1
    while aragon.is_alive() and goblin.is_alive():
        print(f"\nBattle_{battle_counter}:")
        print("-" * 40)
        print(goblin.attack_target(aragon))
        print(aragon.attack_target(goblin))
        print(f"Goblin remaining health: {goblin.health}")
        print(f"Aragon remaining health: {aragon.health}")
        print(aragon.heal(2))
        print("-" * 40 ,"\n\n")


        print("Characters after battle:")
        print("-" * 40)
        print(aragon)
        print(goblin, end="")
        print("-" * 40 ,"")
        battle_counter += 1


if __name__ == "__main__":
    main()
