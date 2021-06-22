from random import randint

class Monster:
    m_name = ""
    m_type = ""
    m_health = ""
    m_abilities = [["Strength","?"], ["Dexterity","?"],["Intelligence","?"],["Wisdom","?"],["Charisma","?"]]

    def __init__(self, name):
        self.m_name = name
        self.m_type = "Monster"
        self.m_health = randint(2, 10)
        for i in range(len(self.m_abilities)):
            self.m_abilities[i][1] = randint(8, 18)

    def __str__(self):
        print(f"Monster name: {self.m_name}\nMonster type: {self.m_type}\nMonster health: {self.m_health}")
        # for i in range(0,5):
            # print(f"{self.m_abilities[i][0]} = {self.m_abilities[i][1]}")
        print("\n")

    def damage(self, char):
        damage = randint(1, 2) + char.modifiers(char.p_abilities[0][1])
        self.m_health -= damage
        return damage