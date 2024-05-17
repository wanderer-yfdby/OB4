from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        return "наносит удар мечом"

class Bow(Weapon):
    def attack(self):
        return "наносит удар из лука"

class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def changeWeapon(self, weapon: Weapon):
        self.weapon = weapon

    def attack(self):
        if self.weapon:
            return f"{self.name} {self.weapon.attack()}"
        else:
            return f"{self.name} безоружен"

class Monster:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

# Пример использования
def battle(fighter, monster):
    print(f"{fighter.attack()}")
    print(f"{monster} побежден!")

# Создадим бойца и монстра
fighter = Fighter("Боец")
monster = Monster("Монстр")

# Боец выбирает меч
sword = Sword()
fighter.changeWeapon(sword)
battle(fighter, monster)

# Боец выбирает лук
bow = Bow()
fighter.changeWeapon(bow)
battle(fighter, monster)