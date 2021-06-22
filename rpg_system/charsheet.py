import time
from random import randint

CLASSES = ["(1) Warrior", "(2) Rogue", "(3) Mage"]

class CharSheet:
    p_name = ""
    p_class = ""
    p_xp_base = 1
    p_xp = 1
    p_level = 1
    p_abilities = [["Strength", "?"], ["Dexterity", "?"], ["Intelligence", "?"], ["Wisdom", "?"], ["Charisma", "?"]]

    def __str__(self):
        print(f"Character name: {self.p_name}\nCharacter class: {self.p_class}\n")
        for i in range(0,5):
            print(f"{self.p_abilities[i][0]} = {self.p_abilities[i][1]}")
        print("\n")

    def set_parameters(self):
        abilities = [["Strength", input("Strength: ")],
                ["Dexterity", input("Dexterity: ")],
                ["Intelligence", input("Intelligence: ")],
                ["Wisdom", input("Wisdom: ")],
                ["Charisma", input("Charisma: ")]]
        for i in range(0, 5):
            self.p_abilities[i][1] = abilities[i][1]

    def set_random_parameters(self):
        for i in range(len(self.p_abilities)):
            self.p_abilities[i][1] = randint(10, 18)

    def set_name(self):
        self.p_name = input("Character name: ")

    def set_class(self):
        while True:
            print("\nChoose a character class!\n")
            for i in range(len(CLASSES)): print(CLASSES[i])
            try:
                choice = int(input(": "))
                if choice == 1:
                    self.p_class = CLASSES[0][4:]
                    break
                elif choice == 2:
                    self.p_class = CLASSES[1][4:]
                    break
                elif choice == 3:
                    self.p_class = CLASSES[2][4:]
                    break
            except ValueError:
                print("\nTry again...")

    def xp_gain(self):
        self.p_xp += randint(1, 3)
        if self.p_xp >= self.p_xp_base:
            self.p_xp_base = self.p_xp * 2
            self.p_level += 1
            print(f"\nLEVEL UP!\n{self.p_name} is now level {self.p_level}!\n")
            for i in range(len(self.p_abilities)):
                temp = randint(0, 1)
                self.p_abilities[i][1] += temp
                print(f"{self.p_abilities[i][0]} ({self.p_abilities[i][1]}) + {temp}")
            print("\n")
            # self.__str__()
            time.sleep(5)

    def modifiers(self, stat):
        if stat < 15:
            return 1
        elif stat < 20:
            return 2
        elif stat < 25:
            return 3
        elif stat < 30:
            return 4
        elif stat < 35:
            return 5