import time
import random

hint = """hint: deepness makes it harder to mine,
but the ores are more valuable"""
hint2 = "subscribe to RandomDuckGuy and comment mining gam on Youtube (my minecraft channel) for extra perks"
hint3 = """mine diamond, dimond gud, dimaonf cul,
 diaomnfd shiny ehehHEHehhEHHEEHEHEH EEEEEGEGEGEHEHEHEGE"""
money = 0
ores = []
tank = 1
pickaxe = 0
drill = 0

lucky_charm = False
mining_time = 3
deepness = 0  # Initialize deepness

def intro():
    print("""chucky >> welcome! this is chucky's mine!
    here you will work from 5am to 10 pm? sounds good? (i honestly don't care what you say)
     you somehow got employed onto this mine, chucky will not let you free until you earn $10,000. go mining now""")

def print_ores(ores_array):
    return ', '.join(ores_array) if ores_array else "No ores"

def mine():
    randomv = random.randint(1, 6)
    ore_found = ""
    if randomv == 1:
        ore_found = "stone"
    elif randomv == 2:
        ore_found = "coal"
    elif randomv == 3:
        ore_found = "iron"
    elif randomv == 4:
        ore_found = "diamond"
    elif randomv == 5:
        ore_found = "emerald"
    elif randomv == 6:
        ore_found = "ruby"

    ores.append(ore_found)
    print(f"You found {ore_found} x{tank}")

    if lucky_charm and random.random() < 0.1:  # 10% chance to find a lucky ore
        ores.append("lucky ore")
        print("You found a lucky ore!")

# Call the intro once at the start
intro()
def autominer():
    while auto_miner == True:
        print("auto miner collected,")
        mine()

        time.sleep(10)
auto_miner = False
# Game loop
while True:
    minging = input("What do you want to do? mine, sell, or buy? (m/s/b) >>> ").strip().lower()

    if minging == "m":
        print(f"Current ores: {print_ores(ores)}")
        countdown = mining_time
        sleep_time = max(0.1, 1 - pickaxe + deepness)  # Ensure sleep time is never negative or zero
        for numcount in range(countdown):
            print(f"Mining in progress... {countdown}.")
            countdown -= 1
            time.sleep(sleep_time)
        print("Mining complete!")
        mine()

        deepness = round(deepness + 0.1, 1)  # Increase deepness and round to one decimal place
        print(f'Current deepness {deepness}')
        print()

    elif minging == "s":
        sell = input(f'You have {print_ores(ores)}, sell all? (y/n) >>> ').strip().lower()
        if sell == "y":
            deepnesscoins = max(deepness - 0.7, 0)  # Ensure deepnesscoins is non-negative
            total_money = 0
            for ore in ores:
                if ore == "stone":
                    total_money += 1 + deepnesscoins
                elif ore == "coal":
                    total_money += 2 + deepnesscoins
                elif ore == "iron":
                    total_money += 3 + deepnesscoins
                elif ore == "diamond":
                    total_money += 4 + deepnesscoins
                elif ore == "emerald":
                    total_money += 5 + deepnesscoins
                elif ore == "ruby":
                    total_money += 6 + deepnesscoins
                elif ore == "lucky ore":
                    total_money += 20 + deepnesscoins

            if not drill == 0:
                total_money *= drill
                print(f"Multiplied money by {drill}!")
            ores = []
            print(f'You now have ${money:.2f}')

    elif minging == "b":
        print("""Welcome to duckmerch.store! What do you wanna buy?
                1. Pickaxe: reduce mining time by 0.5 seconds (cost: $5)
                2. Drill: doubles the money you get from selling (cost: $20)
                3. Tank: 3x your ores per mining (cost: $50)
                4. Workers: reduce mining time by 3 seconds (cost: $29)
                5. Auto-Miner: mine automatically every 10 seconds (cost: $200)
                6. Lucky Charm: chance to find a lucky ore worth more (cost: $300)
                7. Escape: Home sweet home! win the game (cost: $10,000)
                8. Hint: idk y u would buy this, but ig u can?? (cost: $5,000)""")

        choice = input("Choose an item to buy (1/2/3/4/5/6/7) >>> ").strip()
        if choice == "1":
            if money >= 5:
                money -= 5
                pickaxe += 0.5
                print("You bought a pickaxe!")
            else:
                print("You don't have enough money.")
        elif choice == "2":
            if money >= 20:
                money -= 20
                drill += 2
                print("You bought a drill!")
            else:
                print("You don't have enough money.")
        elif choice == "3":
            if money >= 50:
                money -= 50
                tank += 3  # Increase tank multiplier
                print("You bought a tank!")
            else:
                print("You don't have enough money.")
        elif choice == "4":
            if money >= 29:
                money -= 29
                pickaxe += 3
                print("You bought workers!")
            else:
                print("You don't have enough money.")
        elif choice == "5":
            if money >= 200:
                money -= 200
                auto_miner = True
                print("You bought an auto-miner!")
                autominer()
            else:
                print("You don't have enough money.")
        elif choice == "6":
            if money >= 300:
                money -= 300
                lucky_charm = True
                print("You bought a Lucky Charm!")
            else:
                print("You don't have enough money.")
        elif choice == "7":
            if money >= 10000:
                print("Congratulations! You've escaped the mine and won the game!")
                break
            else:
                print("You don't have enough money.")
        elif choice == "8":
            if money >= 5000:
                print(hint3)
                print("I mean, you bought it, so like don't complain")
            else:
                print("You don't have enough money.")
    else:
        print("Invalid option. Please choose 'm', 's', or 'b'.")
