import time
import random

hint = """hint: deepness makes it harder to mine,
but the ores are more valuable"""
hint2 = """mine diamond, dimond gud, dimaonf cul,
 diaomnfd shiny ehehHEHehhEHHEEHEHEH EEEEEGEGEGEHEHEHEGE"""

deepness = 0
#deeplist = []

def intro():
    print("""chucky >> welcome! this is chucky's mine!
    here you will work from 5am to 10 pm? sounds good? (i honestly don't care what you say)
     you somehow got employed onto this mine, chucky will not let you free until you earn $10,000. go mining now""")

def print_ores(ores_array):
    return ', '.join(ores_array) if ores_array else "No ores"

def mine(deepness,user_ores, tank=0, lucky_charm=False):
    random_ore = random.randint(1, 7)
    ore_found = ""
    if not tank == 0:
        for i in range(tank):
            if random_ore == 1:
                ore_found = "stone"
            elif random_ore == 2:
                ore_found = "coal"
            elif random_ore == 3:
                ore_found = "iron"
            elif random_ore == 4:
                ore_found = "diamond"
            elif random_ore == 5:
                ore_found = "emerald"
            elif random_ore == 6:
                ore_found = "ruby"
            elif random_ore == 7:
                print("You found nothing!!!")
    else:
        if random_ore == 1:
            ore_found = "stone"
        elif random_ore == 2:
            ore_found = "coal"
        elif random_ore == 3:
            ore_found = "iron"
        elif random_ore == 4:
            ore_found = "diamond"
        elif random_ore == 5:
            ore_found = "emerald"
        elif random_ore == 6:
            ore_found = "ruby"
        elif random_ore == 7:
            print("You found nothing!!!")

    # print(deeplist)
    if ore_found:
        user_ores.append(ore_found)
       # deeplist.append(deepness)
        if tank:
            print(f"You found {ore_found} x{tank}")
        else:
            print(f"You found {ore_found} ")


        if lucky_charm and random.random() < 0.1:  # 10% chance to find a lucky ore
            user_ores.append("lucky ore")
            print("You found a lucky ore!")



# def autominer(user_ores, tank, lucky_charm):
#         print("auto miner collected,")
#         mine(user_ores, tank, lucky_charm)
#         time.sleep(10)

def sell(money, drill, ores):
    current_money = 0
    sell_input = input(f'You have {print_ores(ores)}, sell all? (y/n) >>> ').strip().lower()

    if sell_input == "y":
       # deepnesscoins = max(deepness - 0.7, 0)  # Ensure deepnesscoins is non-negative
        for ore in ores:
            if ore == "stone":
                current_money += 1 #+ deepnesscoins
            elif ore == "coal":
                current_money += 2#  + deepnesscoins
            elif ore == "iron":
                current_money += 3 # + deepnesscoins
            elif ore == "diamond":
                current_money += 4 # + deepnesscoins
            elif ore == "emerald":
                current_money += 5 # + deepnesscoins
            elif ore == "ruby":
                current_money += 6 #  + deepnesscoins
            elif ore == "lucky ore":
                current_money += 20 # + deepnesscoins
            # for item in range(deeplist):
            #     print(deeplist[1])
            #     deeplist.pop(1)
        if not drill == 0:
            current_money *= drill
            print(f"Multiplied money by {drill}!")

        money += current_money
        ores.clear()
        print(f'You now have ${money:.2f}')
        ores.clear()

    # Add this else statement to return money even if no sale is made
    else:
        print("No ores sold.")

    return money  # Make sure the function always returns 'money'


def main(deepness):

     # Initialize deepness
    money = 0
    ores = []
    tank = 0
    pickaxe = 0
    drill = 0
    mining_time = 3
    lucky_charm = False

    # Call the intro once at the start
    intro()

    # Game loop
    while True:
        mining = input("What do you want to do? mine, sell, or buy? (m/s/b). q to exit >>> ").strip()
        if mining == "q":
            break

        if mining == "m":
            print(f"Current ores: {print_ores(ores)}")
            countdown = mining_time
            sleep_time = max(0.1, 1 - pickaxe + deepness)  # Ensure sleep time is never negative or zero
            for numcount in range(countdown):
                print(f"Mining in progress... {countdown}.")
                countdown -= 1
                time.sleep(sleep_time)
            print("Mining complete!")
            mine(deepness,ores, tank, lucky_charm,)

            deepness = round(deepness + 0.1, 1)  # Increase deepness and round to one decimal place
            # print(f'Current deepness {deepness}')
           #  print()

        elif mining == "s":
            money = sell(money, drill,ores)

        elif mining == "b":
            print("""Welcome to duckmerch.store! What do you wanna buy?
                        1. Pickaxe: reduce mining time by 0.5 seconds (cost: $5)
                        2. Drill: doubles the money you get from selling (cost: $20)
                        3. Tank: 2x your ores per mining (cost: $50)
                        4. Workers: reduce mining time by 3 seconds (cost: $29)
                        5. Auto-Miner: mine automatically every 10 seconds(COMING SOON) (cost: $200)
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
                    tank += 1  # Increase tank multiplier
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
                print("sorry, coming soon")
                """if money >= 200:
                    money -= 200
                    auto_miner = True
                    print("You bought an auto-miner!")
                    # autominer(ores, tank, lucky_charm)
                else:
                    print("You don't have enough money.")"""
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
                    print(hint2)
                    time.sleep(1)
                    print(hint)
                    print("I mean, you bought it, so like don't complain")
                else:
                    print("You don't have enough money.")
        else:
            print("Invalid option. Please choose 'm', 's', or 'b'.")


if __name__ == '__main__':
    main(deepness)