import time
from random import randint

from charsheet import CharSheet
from monster import Monster

def main():
    counter = 0

    player = CharSheet()
    player.set_name()
    player.set_class()
    player.set_random_parameters()

    try:
        while True:
            monster = Monster(f"Monster-{randint(1,100)}")
            monster.__str__()
            time.sleep(2)
            while monster.m_health > 0:
                    print(f"{player.p_name} hit {monster.m_name} for {monster.damage(player)}")
                    print(f"Health at: {monster.m_health}")
                    time.sleep(1)
                    if monster.m_health < 1:
                        print(f"\n---{player.p_name} killed {monster.m_name}---\n")
                        player.xp_gain()
                        print(f"Experience: {player.p_xp} / {player.p_xp_base}")
                        counter += 1
    except KeyboardInterrupt:
        print(f"\n///---Monsters slain: {counter}---\\\\\\\n")

if __name__ == "__main__":
    main()