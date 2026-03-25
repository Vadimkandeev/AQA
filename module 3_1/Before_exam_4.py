class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health


class Warrior(Hero):
    def attac(self):
        return f"Нанёс 20 урона мечом"


class Mage(Hero):
    def attack(self):
        return f"Нанёс 15 урона заклинанием"



warrior = Warrior("Bob", 250)
mage = Mage("Anna", 400)

print(warrior.attac())
print(mage.attack())
