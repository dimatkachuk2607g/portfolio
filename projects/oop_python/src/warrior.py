"""
Represents a Warrior that inherits from Character, with an additional rage attribute
and a special attack method, alongside a __str__ override for displaying details.
"""

from oop_python.src.character import Character


class Warrior(Character):
    class_type = "Warrior"

    def __init__(self, name:str, age:int, attack:int, defense:int, health:int, rage:int):
        super().__init__(name, age, attack, defense, health)

        if not isinstance(rage, int):
            raise TypeError("Rage must be a positive integer")

        self.rage = rage


    def rage_attack(self, target:"Character"):
        """Performs a rage attack on a target character, adding rage to base attack"""
        damage = self.attack + self.rage
        target.take_damage(damage)
        return f'{self.name} rage attacks {target.name} for {damage} damage'


    def __str__(self):
        character_str = super().__str__()
        return f'''\
{character_str}\
Character Type: {self.class_type}      
Character Rage: {self.rage}
'''





def main():
    """Sample fight between the a dragon(Character) and warrior(Warrior)"""
    conan = Warrior("Conan", 47, 150, 30, 300, 500)
    dragon = Character("dragon", 1500, 200, 50, 1000)

    print("Initialize both characters:")
    print("-" * 40)
    print(conan)
    print(dragon, end="")
    print("-" * 40 ,"\n\n")


    print("Battle:")
    print("-" * 40)
    print(dragon.attack_target(conan))
    print(conan.rage_attack(dragon))
    print(f"Dragon is still alive? {dragon.is_alive()}, remaining health: {dragon.health}")
    print(f"Conan is still alive? {conan.is_alive()}, remaining health: {conan.health}")
    print(conan.heal(2))
    print("-" * 40 ,"\n\n")


    print("Characters after battle:")
    print("-" * 40)
    print(conan)
    print(dragon, end="")
    print("-" * 40 ,"")

if __name__ == "__main__":
    main()


