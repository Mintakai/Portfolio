import random

def roll_d20():
    input("Press any key to roll...")
    roll = random.randint(1,20)
    return roll

def main():
    while True:
        print(roll_d20())

if __name__ == "__main__":
    main()