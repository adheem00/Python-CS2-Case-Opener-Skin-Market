# Adheem's CS2 Case Opener & Inventory
# Written 09.02.25 - 

devmode = False 
money = 0
wanttosell = False
maxinvspace = 20

# ----- Modules ----- #

import random
import time

# ----- Cases & Dictionaries ----- #

csgoweaponcase = {
        "name": "CS:GO Weapon Case",
        "price": 112.09,
        "0": ("Mil-Spec", "MP7", "Skulls", 26.23),
        "1": ("Mil-Spec", "AUG", "Wings", 27.11),
        "2": ("Mil-Spec", "SG 553", "Ultraviolet", 26.93),

        "3": ("Restricted", "USP-S", "Dark Water", 83.64),
        "4": ("Restricted", "M4A1-S", "Dark Water", 96.85),
        "5": ("Restricted", "Glock-18", "Dragon Tattoo", 117.42),

        "6": ("Classified", "Desert Eagle", "Hypnotic", 246.28),
        "7": ("Classified", "AK-47", "Case Hardened", 384.75), 

        "8": ("Covert", "AWP", "Lightning Strike", 559.32),
        
        #knives and gloves
        "9": ("Gold", "Butterfly Knife", "Fade", 1298.75),
        "10": ("Gold", "Butterfly Knife", "Slaughter", 1023.50),
        "11": ("Gold", "Butterfly Knife", "Case Hardened", 1104.32),
        "12": ("Gold", "Butterfly Knife", "Blue Steel", 998.15),

        "13": ("Gold", "Shadow Daggers", "Crimson Web", 325.99),
        "14": ("Gold", "Shadow Daggers", "Fade", 412.47),
        "15": ("Gold", "Shadow Daggers", "Slaughter", 387.61),
        "16": ("Gold", "Shadow Daggers", "Case Hardened", 354.29),

        "17": ("Gold", "Huntsman Knife", "Tiger Tooth", 540.83),
        "18": ("Gold", "Huntsman Knife", "Doppler", 615.67),
        "19": ("Gold", "Huntsman Knife", "Marble Fade", 578.22),
        "20": ("Gold", "Huntsman Knife", "Freehand", 490.90),

        "21": ("Gold", "Talon Knife", "Lore", 974.63),
        "22": ("Gold", "Talon Knife", "Stained", 825.49),
        "23": ("Gold", "Talon Knife", "Safari Mesh", 689.30),
        "24": ("Gold", "Talon Knife", "Case Hardened", 915.78)

}

operationbravocase = {
    "name": "Operation Bravo Case",
    "price": 49.04,
    "0": ("Mil-Spec", "Dual Berettas", "Black Limba", 15.37),
    "1": ("Mil-Spec", "G3SG1", "Demeter", 12.66),
    "2": ("Mil-Spec", "UMP-45", "Bone Pile", 12.50),
    "3": ("Mil-Spec", "Nova", "Tempest", 12.66),
    "4": ("Mil-Spec", "Galil AR", "Shattered", 26.63),
    "5": ("Mil-Spec", "SG-553", "Wave Spray", 8.59),

    "6": ("Restricted", "MAC-10", "Graven", 40.58),
    "7": ("Restricted", "M4A4", "Zirka", 48.38),
    "8": ("Restricted", "M4A1-S", "Bright Water", 33.42),
    "9": ("Restricted", "USP-S", "Overgrowth", 57.45),

    "10": ("Classified", "AWP", "Graphite", 154.52),
    "11": ("Classified", "P2000", "Ocean Foam", 139.56),
    "12": ("Classified", "P90", "Emerald Dragon", 666.94),

    "13": ("Covert", "Desert Eagle", "Golden Koi", 128.36),
    "14": ("Covert", "AK-47", "Fire Serpent", 1360.85),

    #knives and gloves

    "16": ("Gold", "Karambit", "Case Hardened", 1200.73),
    "17": ("Gold", "Karambit", "Stained", 1494.20),
    "18": ("Gold", "Karambit", "Blue Steel", 1204.74),
    "19": ("Gold", "Karambit", "Safari Mesh", 1494.41),

    "20": ("Gold", "Gut Knife", "Case Hardened", 535.73),
    "21": ("Gold", "Gut Knife", "Slaughter", 248.95),
    "22": ("Gold", "Gut Knife", "Blue Steel", 174.34),
    "23": ("Gold", "Gut Knife", "Crimson Web", 249.78),

    "24": ("Gold", "Flip Knife", "Doppler", 661.25),
    "25": ("Gold", "Flip Knife", "Marble Fade", 586.50),
    "26": ("Gold", "Flip Knife", "Tiger Tooth", 549.97),
    "27": ("Gold", "Flip Knife", "Fade", 836.28),

    "28": ("Gold", "Bayonet", "Gamma Doppler", 1,135.00),
    "29": ("Gold", "Bayonet", "Lore", 537.54),
    "30": ("Gold", "Bayonet", "Doppler", 925.00),
    "31": ("Gold", "Bayonet", "Freehand", 517.01)

}

gammacase = {
    "name": "Gamma Case",
    "price": 3.38,
    "0": ("Mil-Spec", "SG 553", "Aerial", 0.33),
    "1": ("Mil-Spec", "MAC-10", "Carnivore", 0.63),
    "2": ("Mil-Spec", "Nova", "Exo", 0.38),
    "3": ("Mil-Spec", "PP-Bizon", "Harvester", 0.52),
    "4": ("Mil-Spec", "P250", "Iron Clad", 0.79),
    "5": ("Mil-Spec", "Tec-9", "Ice Cap", 0.84),
    "6": ("Mil-Spec", "Five-SeveN", "Violent Daimyo", 0.88),
    
    "7": ("Restricted", "Sawed-Off", "Limelight", 3.04),
    "8": ("Restricted", "AUG", "Aristocrat", 2.42),
    "9": ("Restricted", "P90", "Chopper", 2.44),
    "10": ("Restricted", "R8 Revolver", "Reboot", 3.38),
    "11": ("Restricted", "AWP", "Phobos", 3.07),
    
    "12": ("Classified", "P2000", "Imperial Dragon", 10.14),
    "13": ("Classified", "SCAR-20", "Bloodsport", 4.88),
    "14": ("Classified", "M4A4", "Desolate Space", 33.55),

    "15": ("Covert", "Glock-18", "Wasteland Rebel", 7.25),
    "16": ("Covert", "M4A1-S", "Mecha Industries", 124.55),

    # knives and gloves
    "17": ("Gold", "Bayonet", "Marble Fade", 1123.45),
    "18": ("Gold", "Bayonet", "Case Hardened", 1064.50),
    "19": ("Gold", "Bayonet", "Stained", 980.35),
    "20": ("Gold", "Bayonet", "Safari Mesh", 945.90),

    "21": ("Gold", "M9 Bayonet", "Stained", 1158.65),
    "22": ("Gold", "M9 Bayonet", "Blue Steel", 1103.32),
    "23": ("Gold", "M9 Bayonet", "Doppler", 1200.48),
    "24": ("Gold", "M9 Bayonet", "Fade", 1182.29),

    "25": ("Gold", "Karambit", "Stained", 1389.15),
    "26": ("Gold", "Karambit", "Safari Mesh", 1298.00),
    "27": ("Gold", "Karambit", "Case Hardened", 1332.23),
    "28": ("Gold", "Karambit", "Tiger Tooth", 1415.79),

    "29": ("Gold", "Gut Knife", "Stained", 478.50),
    "30": ("Gold", "Gut Knife", "Marble Fade", 485.32),
    "31": ("Gold", "Gut Knife", "Crimson Web", 463.27),
    "32": ("Gold", "Gut Knife", "Tiger Tooth", 510.76)
}

dreamsandnightmarescase = {
    "name": "Dreams and Nightmares Case",
    "price": 1.62,
    "0": ("Mil-Spec", "MAG-7", "Foresight", 0.22),
    "1": ("Mil-Spec", "SCAR-20", "Poultrygeist", 0.24),
    "2": ("Mil-Spec", "P2000", "Lifted Spirits", 0.28),
    "3": ("Mil-Spec", "MP5-SD", "Necro Jr.", 0.11),
    "4": ("Mil-Spec", "Sawed-Off", "Spirit Board", 0.27),
    "5": ("Mil-Spec", "MAC-10", "Ensnared", 0.23),
    "6": ("Mil-Spec", "Five-SeveN", "Scrawl", 0.23),
    
    "7": ("Restricted", "G3SG1", "Dream Glade", 1.59),
    "8": ("Restricted", "XM1014", "Zombie Offensive", 1.51),
    "9": ("Restricted", "PP-Bizon", "Space Cat", 1.48),
    "9": ("Restricted", "USP-S", "Ticket to Hell", 2.47),
    "10": ("Restricted", "M4A1-S", "Night Terror", 1.90),
    
    "11": ("Classified", "Dual Berettas", "Melondrama", 3.58),
    "12": ("Classified", "MP7", "Abyssal Apparition", 9.23),
    "13": ("Classified", "FAMAS", "Rapid Eye Movement", 9.17),
    
    "14": ("Covert", "MP9", "Starlight Protector", 16.90),
    "15": ("Covert", "AK-47", "Nightwish", 58.61),

    #knives
    "16": ("Gold", "Butterfly Knife", "Doppler", 1158.90),
    "17": ("Gold", "Butterfly Knife", "Blue Steel", 1123.45),
    "18": ("Gold", "Butterfly Knife", "Fade", 1205.20),
    "19": ("Gold", "Butterfly Knife", "Case Hardened", 1192.33),

    "20": ("Gold", "Talon Knife", "Marble Fade", 932.18),
    "21": ("Gold", "Talon Knife", "Tiger Tooth", 996.50),
    "22": ("Gold", "Talon Knife", "Gamma Doppler", 1024.70),
    "23": ("Gold", "Talon Knife", "Fade", 1025.65),

    "24": ("Gold", "Huntsman Knife", "Blue Steel", 481.88),
    "25": ("Gold", "Huntsman Knife", "Tiger Tooth", 514.32),
    "26": ("Gold", "Huntsman Knife", "Marble Fade", 493.29),
    "27": ("Gold", "Huntsman Knife", "Crimson Web", 472.12),

    "28": ("Gold", "Falchion Knife", "Fade", 550.89),
    "29": ("Gold", "Falchion Knife", "Blue Steel", 520.76),
    "30": ("Gold", "Falchion Knife", "Gamma Doppler", 540.93),
    "31": ("Gold", "Falchion Knife", "Crimson Web", 510.20)

}

kilowattcase = {
    "name": "Kilowatt Case",
    "price": 0.66,

    "0": ("Mil-Spec", "SSG 08", "Dezastre", 0.43),
    "1": ("Mil-Spec", "Nova", "Dark Sigil", 0.31),
    "2": ("Mil-Spec", "Dual Berettas", "Hideout", 0.31),
    "3": ("Mil-Spec", "UMP-45", "Motorized", 0.30),
    "4": ("Mil-Spec", "XM1014", "Irezumi", 0.32),
    "5": ("Mil-Spec", "Tec-9", "Slag", 0.10),
    "6": ("Mil-Spec", "MAC-10", "Light Box", 0.65),
    
    "7": ("Restricted", "M4A4", "Etch Lord", 3.88),
    "8": ("Restricted", "Five-SeveN", "Hybrid", 2.67),
    "9": ("Restricted", "Sawed-Off", "Analog Input", 2.61),
    "10": ("Restricted", "MP7", "Just Smile", 2.68),
    "11": ("Restricted", "Glock-18", "Block-18", 2.61),

    "12": ("Classified", "Zeus x27", "Olympus", 12.51),
    "13": ("Classified", "USP-S", "Jawbreaker", 23.56),
    "14": ("Classified", "M4A1-S", "Hideout", 2.61),
    
    "15": ("Covert", "AWP", "Chrome Cannon", 154.33),
    "16": ("Covert", "AK-47", "Inheritance", 213.22),

    #knives n gloves
    "17": ("Gold", "Karambit", "Gamma Doppler", 1299.75),
    "18": ("Gold", "Karambit", "Marble Fade", 1378.60),
    "19": ("Gold", "Karambit", "Crimson Web", 1182.90),
    "20": ("Gold", "Karambit", "Safari Mesh", 1123.45),

    "21": ("Gold", "M9 Bayonet", "Blue Steel", 1245.80),
    "22": ("Gold", "M9 Bayonet", "Crimson Web", 1152.30),
    "23": ("Gold", "M9 Bayonet", "Tiger Tooth", 1225.55),
    "24": ("Gold", "M9 Bayonet", "Marble Fade", 1304.10),

    "25": ("Gold", "Butterfly Knife", "Slaughter", 1227.50),
    "26": ("Gold", "Butterfly Knife", "Crimson Web", 1099.20),
    "27": ("Gold", "Butterfly Knife", "Doppler", 1149.75),
    "28": ("Gold", "Butterfly Knife", "Case Hardened", 1132.33),

    "29": ("Gold", "Falchion Knife", "Tiger Tooth", 542.70),
    "30": ("Gold", "Falchion Knife", "Stained", 509.90),
    "31": ("Gold", "Falchion Knife", "Slaughter", 520.20),
    "32": ("Gold", "Falchion Knife", "Gamma Doppler", 536.15)

}


casedict = {
    # free cases
    "CS:GO Weapon Case": csgoweaponcase,
    "Operation Bravo Case": operationbravocase,
    "Gamma Case": gammacase,
    "Dreams and Nightmares Case": dreamsandnightmarescase,
    "Kilowatt Case": kilowattcase
}

userinventory = [] # A list of tuples of owned items in the form: (gun, skin, price, case it was unboxed from, rarity)

itemshop = { # rarity, weapon type, skin, price
    "0": ("Gold", "Karambit", "Ruby Doppler", 5000),
    "1": ("Gold", "Butterfly Knife", "Marble Fade", 2500),
    "2": ("Gold", "Huntsman Knife", "Slaughter", 500),
    "3": ("Gold", "Sports Glove", "Pandora's Box", 7500),
    "4": ("Gold", "Hand Wraps", "Cobalt Skulls", 400),
    "5": ("Gold", "Driver Gloves", "Imperial Plaid", 500),
    "6": ("Gold", "M4A4", "Howl", 6500),
    "7": ("Gold", "AWP", "Dragon Lore", 14000),
}

market = {
    "Item Shop": itemshop, # knives gloves and contraband
    "Inventory Upgrade": [1, 500, 15], #tuples in the form (level, price, size increase per purchase)
    "Sell Value Upgrade": [1, 3500], # tuples in the form (level, price)
    "Buy Cases": []
}




# ----- Subprograms ----- #

def ageverification(input): # Age Verification

    oldestpersonalive = 116

    if input > oldestpersonalive:
        return False
    elif input <= 0:
        return False
    elif input < 18:
        return False
    else:
        return True

def chanceroller(): # Random Number Generator
    return round(random.uniform(0, 100), 2) # random float between 1 and 100 (percent) to 2 decimal places

def clean_string(input_string):
    return ''.join([char.lower() for char in input_string if char.isalpha()])


def viewmarket():
    global maxinvspace
    global money

    print("\nWelcome to the Market!\nHere, you can access many features.")
    time.sleep(1)
    print("What would you like to buy today?\n")
    print("0) Return")
    
    k = 1
    for items in market:
        if k == 3 or k == 4:
            print(f"{k}) {items} (Coming Soon!)")
            time.sleep(0.5)
            k += 1
            continue
        print(f"{k}) {items}")
        time.sleep(0.5)
        k += 1

    
    whattobuy = input("")
    
    whattobuy = whattobuy.strip().lower()

    if whattobuy == "0":
        print("Returning to Landing Page...")
        landingpage()

    if whattobuy.strip() == "1" or whattobuy.strip().lower() == "item shop":

        print(f"Opening Item Shop...\n")
        
        for key, items in market["Item Shop"].items():
            print(f"{int(key) + 1}) {items[1]} - {items[2]} | £{items[3]}")
            time.sleep(0.5)

        time.sleep(0.5)
        print(f"\nName the index of the item you wanna buy.\nTo return to the Market, type \"Return\"\n")
        indexinput0 = input("")
        indexinput0 = indexinput0.strip().lower()

        if indexinput0 == "return":
            print("Returning to Market...")
            viewmarket()
        
        elif int(indexinput0) > 1 or int(indexinput0) <= k: #valid bounds check
            print(f"Are you sure you want to buy a/an {market['Item Shop'][str(int(indexinput0) - 1)][1]} - {market['Item Shop'][str(int(indexinput0) - 1)][2]}?")
            print(f"It's £{(market['Item Shop'][str(int(indexinput0) - 1)][3]):.2f}. (y/n)\n")

            areyousure1 = input("")
            areyousure1 = areyousure1.strip().lower()
            if areyousure1 == "y":
                if money >= market['Item Shop'][str(int(indexinput0) - 1)][3]:
                    money -= market['Item Shop'][str(int(indexinput0) - 1)][3]
                    print(f"Done! You just bought a {market['Item Shop'][str(int(indexinput0) - 1)][1]} - {market['Item Shop'][str(int(indexinput0) - 1)][2]}!")
                    print(f"You just spent £{(market['Item Shop'][str(int(indexinput0) - 1)][3]):.2f}.\nYour new balance is £{money:.2f}.")
                    del itemshop[str(int(indexinput0) - 0)]
                    print("Returning to Market...")
                    viewmarket()
                elif money < market['Item Shop'][str(int(indexinput0) - 1)][3]:
                    print("You don't have enough money.")
                    print(f"You need £{(market['Item Shop'][str(int(indexinput0) - 1)][3] - money):.2f}")
            else:
                print("Close one!")
                print("Returning to Market...")
                viewmarket()
        else:
            print("error 90000 lolz9k")

    elif whattobuy.strip() == "2" or whattobuy.strip().lower() == "inventory upgrade":
        time.sleep(1)
        print(f"Inventory Upgrades increase your inventory space by {market['Inventory Upgrade'][2]}.")
        time.sleep(1)
        print(f"Your inventory level is {market["Inventory Upgrade"][0]}.")
        time.sleep(0.5)
        print(f"They are £{market['Inventory Upgrade'][1]}.")
        
        invupgradeconfirmation = input(F"Are you sure you want to buy one? (y/n)\n")
        time.sleep(1)

        if invupgradeconfirmation.strip().lower() == "y":
            if money >= market['Inventory Upgrade'][1]:
                print("Buying item...")
                time.sleep(1)
                print(f"You just bought an Inventory Upgade for {market['Inventory Upgrade'][1]}!\n")


                maxinvspace += market["Inventory Upgrade"][2]

                print(f"Your inventory can now store {maxinvspace} items.")
                market["Inventory Upgrade"][0] += 1
                time.sleep(1)
                print(f"Your inventory level is now {market["Inventory Upgrade"][0]}.")

                money -= market['Inventory Upgrade'][1]
                time.sleep(0.5)
                print(f"Your new balance is £{money:.2f}")
            
                print("Returning to Market...")
                time.sleep(1)
                viewmarket()
            else:
                print("You don't have enough money to buy this.\nReturning to Market...")
                time.sleep(1)
                viewmarket()


        if invupgradeconfirmation.strip().lower() == "n":
            print("Close one! Returning to Market...")
            time.sleep(1)
            viewmarket()
        
        else:
            print("Invalid input. Returning to Market...")
            time.sleep(1)
            viewmarket()

    elif whattobuy.strip() == "3" or whattobuy.strip().lower() == "sell value upgrade":
        print(f"Coming Soon!...")
        time.sleep(2)

        viewmarket()

    elif whattobuy.strip() == "4" or whattobuy.strip().lower() == "buy cases":
        print(f"Coming Soon!...")
        time.sleep(2)
        viewmarket()
        
    elif whattobuy.strip() == str(k) or whattobuy.strip().lower() == "return":
        print("Returning to Landing Page...")
        landingpage()

def sellitems():
    global money
    global wanttosell
    
    if devmode:
        print("sellitems() called")

    if len(userinventory) == 0:
        print("You have no items in your inventory. Go open some cases!")
        print("Returning to Landing Page...")
        landingpage()

    time.sleep(1)
    print(f"Here's your current balance: £{money:.2f}.\n")
    
    for i, items in enumerate(userinventory):
        if i == len(userinventory) - 1: # last item
            print(f"\033[38;5;153m[{i + 1}] [{items[4]}] {items[0]} - {items[1]} - £{items[2]:.2f} (latest item)\033[0m")

        else:
            print(f"[{i + 1}] [{items[4]}] {items[0]} - {items[1]} - £{items[2]:.2f}")
    
    if wanttosell == True:
        print(f"\nName the index of the item you wanna sell.\nIf you want to sell ALL YOUR ITEMS, type \"0\"\nIf you no longer want to sell, type \"-1\"")
        indexinput = int(input("\n"))

        if indexinput <= 0 or indexinput > len(userinventory): # if input less than 1 or more than inv len (valid bounds check)
            if indexinput == -1:
                print("Killing sell prompt...")
                time.sleep(1)
                wanttosell = False
                landingpage()

            elif indexinput == 0:
                
                runningtotal0 = 0.00
                for i, items in enumerate(userinventory):
                    runningtotal0 += items[2]

                print(f"You've chosen to sell ALL YOUR ITEMS.\nTotal Value: {runningtotal0:.2f}\nAre you sure you want to do this? (y/n)")
                areyousure0 = input("")
                time.sleep(1)
                if areyousure0.strip().lower() == "y":
                    print("Selling all items...")
                    time.sleep(1)
                    money += runningtotal0
                    userinventory.clear()

                    
                    print(f"You've just sold your entire inventory for {runningtotal0:.2f}!")
                    print(f"Your new balance is {money:.2f}")
                    time.sleep(1)
                elif areyousure0.strip().lower() == "n":
                    print("Close one!")
                    time.sleep(1)
                    print("Returning to sell prompt...")
                    time.sleep(1)
                    sellitems()
                else:
                    print("Error: Invalid input!\nReturning to sell prompt...")
                    time.sleep(1)
                    sellitems()
            else:
                print(f"You've just selected to sell a/an: {userinventory[indexinput - 1][0]} - {userinventory[indexinput - 1][1]} for  £{userinventory[indexinput - 1][2]}.")
                time.sleep(1)
                areyousure = input("Are you sure you want to sell this item? (y/n)\n")

                if areyousure.strip().lower() == "y":
                    print("Selling item...")
                    time.sleep(1)
                    print(f"Item sold for £{userinventory[indexinput - 1][2]}!")

                    money += userinventory[indexinput - 1][2]
                    userinventory.remove(userinventory[indexinput - 1])
                    print("Returning to Sell Prompt...")
                    time.sleep(1)
                    sellitems()
                if areyousure.strip().lower() == "n":
                    time.sleep(1)
                    print("Close one! Returning to sell prompt...")
                    time.sleep(1)
                    sellitems()
                else:
                    print("Invalid input. Returning to sell prompt...")
                    time.sleep(1)
                    sellitems()

def inventoryinfo(invsum, invlen):
    global maxinvspace
    print("\nInventory Statistics\n")
    
    if invlen > 0:
        print(f"Number of items: {invlen} / {maxinvspace}")
        time.sleep(0.25)
        if devmode:
            print(f"Number of unique items: UNFINISHED")
            time.sleep(0.25)
        print(f"Total Inventory Value: £{invsum:.2f}")
        time.sleep(0.25)
        print(f"Average Item Value: £{(invsum/invlen):.2f}")
        time.sleep(0.25)

        sortedprices = sorted([item[2] for item in userinventory])
        middleindex = len(sortedprices)//2

        print(f"Median Item Value: £{sortedprices[middleindex]}")
        time.sleep(1)

        mostvaluableitem = ""
        # bug: guns with same price may be labelled as most valuable ...
        # ... when it could be another one
        for items in userinventory:
            if items[2] == sortedprices[-1]:
                mostvaluableitem = items[0]
                mostvaluableitemskin = items[1]

        print(f"Most Valuable Item: {mostvaluableitem} - {mostvaluableitemskin} (£{sortedprices[-1]})")
    else:
        print("You have no items in your inventory. Go open some cases!")
        time.sleep(0.25)
        print("Returning to Landing Page...")
        time.sleep(1)
        landingpage()

def viewinventory():
    global wanttosell
    runningtotal = 0.00

    for i, items in enumerate(userinventory):
        if i == len(userinventory) - 1: # last item
            time.sleep(0.5)
            print(f"\033[38;5;153m[{i + 1}] [{items[4]}] {items[0]} - {items[1]} - £{items[2]:.2f} (latest item)\033[0m")

        else:
            print(f"[{i + 1}] [{items[4]}] {items[0]} - {items[1]} - £{items[2]:.2f}")
            time.sleep(0.5)

        runningtotal += items[2]
    
    inventoryinfo(runningtotal, len(userinventory))


    input0 = input(f'\nWanna sell your items to the Market? Type \"sell\".\nOr, When done, type "return"\n')
    
    if input0.strip().lower() == "return":
        landingpage()
    elif input0.strip().lower() == "sell":
        if devmode:
            print("\nsell reached")
        time.sleep(1)
        wanttosell = True
        sellitems()
    else:
        print("errorLOLZ")


def aftercase(caseparam):
    global firsttime
    global money

    if firsttime:
        print("Congrats on opening your first case!")
    
    time.sleep(1)
    print("---------------------------------------")
    print("What do you wanna do next?: \n")
    time.sleep(1)
    print("1 - Open another case\n2 - Open a new type of case\n3 - View Inventory\n4 - Return to Landing Page")
    time.sleep(0.5)
    aftercaseinput = input(" \n")

    if aftercaseinput.strip().title() == "Open Another Case" or aftercaseinput.strip() == "1":
        if devmode:
            print("open another case called")
        
        if invfullcheck() == False:
            if money >= caseparam["price"]:
                money -= caseparam["price"]
                time.sleep(1)
                print(f"\n(You just spent £{caseparam["price"]})")
                time.sleep(1)
                print("Opening CS:GO Weapon Case...")
                time.sleep(1.5)
                print("...")
                caseopener(caseparam)
            else:
                print("You can't afford this case; Try a cheaper one!\nReturning...")
                time.sleep(1.5)
                landingpage()
        
            time.sleep(1)
            print(f"Opening {caseparam["name"]}...")
            time.sleep(1)
            print("...")
            caseopener(caseparam)
        else:
            print("\nYour inventory is full!\nPlease make space by selling some items.")
            time.sleep(1)
            print("Returning to Landing Page...")
            time.sleep(1.5)
            landingpage()

    elif aftercaseinput.strip().title() == "Open A New Type Of Case" or aftercaseinput.strip() == "2":
        if devmode:
            print("Open a new type of case called")
        
        time.sleep(1)
        casedisplay()

    elif aftercaseinput.strip().title() == "View Inventory" or aftercaseinput.strip() == "3":
        if devmode:
            print("view inventory called")
        
        time.sleep(1)
        viewinventory()

    elif aftercaseinput.strip().title() == "Return To Landing Page" or aftercaseinput.strip() == "4":
        if devmode:
            print("return to landing page called")
        
        print("Returning to Landing Page...")
        landingpage()
    
    else:
        print("error")

def displaycaserewards(skinrolledparam, caseparam):
    global money
    print(f"YOU JUST GOT A: {caseparam[str(skinrolledparam)][1]} - {caseparam[str(skinrolledparam)][2]}\n")
    time.sleep(1)
    print(f"ITEM VALUE: £{caseparam[str(skinrolledparam)][3]:.2f}\n")
    time.sleep(1)
    print(f"New balance: £{money}\n")
    time.sleep(0.75)


    userinventory.append((caseparam[str(skinrolledparam)][1], caseparam[str(skinrolledparam)][2], caseparam[str(skinrolledparam)][3], caseparam["name"], caseparam[str(skinrolledparam)][0]))

    aftercase(caseparam)

def caseopener(case):

    # Calculates and displays unboxed item to user.
    # rarity percentages remain constant for each case.
    # however, number of items of each rarity may differ, hence the 'skinrolled' range differing for each case.
    
    chanceroll = chanceroller()

    if devmode:
        print(f"{chanceroll}% Rolled\n")
    time.sleep(1.5)

    if 0 <= chanceroll <= 79.92: # Mil-Spec - 79.92%
        
        if case == csgoweaponcase: # CS:GO Weapon Case
            skinrolled = random.randint(0, 2)
            print("Mil-Spec - 79.92% Chance\n")
            displaycaserewards(skinrolled, csgoweaponcase)
        
        elif case == operationbravocase: # Operation Bravo Case
            skinrolled = random.randint(0, 5)
            print("Mil-Spec - 79.92% Chance\n")
            displaycaserewards(skinrolled, operationbravocase)

        elif case == gammacase: # Gamma Case
            skinrolled = random.randint(0, 5)
            displaycaserewards(skinrolled, gammacase)

        elif case == dreamsandnightmarescase: # Dreams and Nightmares Case
            skinrolled = random.randint(0, 6)
            displaycaserewards(skinrolled, dreamsandnightmarescase)

        elif case == kilowattcase: # Dreams and Nightmares Case
            skinrolled = random.randint(0, 6)
            print("Mil-Spec - 79.92% Chance\n")
            displaycaserewards(skinrolled, kilowattcase)

    elif 79.92 < chanceroll <= 95.90: # Restricted - 15.98%

        if case == csgoweaponcase: # CS:GO Weapon Case
            skinrolled = random.randint(3, 5)
            print("Restricted - 15.98% Chance\n")
            displaycaserewards(skinrolled, csgoweaponcase)
        
        elif case == operationbravocase: # Operation Bravo Case
            skinrolled = random.randint(6, 9)
            print("Restricted - 15.98% Chance\n")
            displaycaserewards(skinrolled, operationbravocase)
        
        elif case == gammacase: # Gamma Case
            skinrolled = random.randint(6, 10)
            print("Restricted - 15.98% Chance\n")
            displaycaserewards(skinrolled, gammacase)

        elif case == dreamsandnightmarescase: # Dreams and Nightmares Case
            skinrolled = random.randint(7, 10)
            print("Restricted - 15.98% Chance\n")
            displaycaserewards(skinrolled, dreamsandnightmarescase)

        elif case == kilowattcase: # Dreams and Nightmares Case
            skinrolled = random.randint(7, 11)
            print("Restricted - 15.98% Chance\n")
            displaycaserewards(skinrolled, kilowattcase)

    elif 95.90 < chanceroll <= 99.10: # Classified - 3.20%
        
        if case == csgoweaponcase: # CS:GO Weapon Case
            skinrolled = random.randint(6, 7)
            print("Classified - 3.20% Chance\n")
            displaycaserewards(skinrolled, csgoweaponcase)
        
        elif case == operationbravocase: # Operation Bravo Case
            skinrolled = random.randint(10, 12)
            print("Classified - 3.20% Chance\n")
            displaycaserewards(skinrolled, operationbravocase
                               )        
        elif case == gammacase: # Gamma Case
            skinrolled = random.randint(11, 13)
            print("Classified - 3.20% Chance\n")
            displaycaserewards(skinrolled, gammacase)

        elif case == dreamsandnightmarescase: # Dreams and Nightmares Case
            skinrolled = random.randint(11, 13)
            print("Classified - 3.20% Chance\n")
            displaycaserewards(skinrolled, dreamsandnightmarescase)

        elif case == kilowattcase: # Dreams and Nightmares Case
            skinrolled = random.randint(12, 14)
            print("Classified - 3.20% Chance\n")
            displaycaserewards(skinrolled, kilowattcase)

    elif 99.10 < chanceroll <= 99.74: # Covert - 0.64%

        if case == csgoweaponcase: # CS:GO Weapon Case
            skinrolled = 8
            print("Covert - 0.64% Chance\n")
            displaycaserewards(skinrolled, csgoweaponcase)

        elif case == operationbravocase: # Operation Bravo Case
            skinrolled = random.randint(13, 14)
            print("Covert - 0.64% Chance\n")
            displaycaserewards(skinrolled, operationbravocase)
        
        elif case == gammacase: # Gamma Case
            skinrolled = random.randint(13, 14)
            print("Covert - 0.64% Chance\n")
            displaycaserewards(skinrolled, gammacase)

        elif case == dreamsandnightmarescase: # Dreams and Nightmares Case
            skinrolled = random.randint(14, 15)
            print("Covert - 0.64% Chance\n")
            displaycaserewards(skinrolled, dreamsandnightmarescase)

        elif case == kilowattcase: # Dreams and Nightmares Case
            skinrolled = random.randint(15, 16)
            print("Covert - 0.64% Chance\n")
            displaycaserewards(skinrolled, kilowattcase)

    elif 99.74 < chanceroll <= 100: # Gold - 0.26%

        if case == csgoweaponcase: # CS:GO Weapon Case
            print("Gold - 0.26% Chance\n")
            skinrolled = random.randint(9, 24)
            displaycaserewards(skinrolled, csgoweaponcase)
        
        elif case == operationbravocase: # Operation Bravo Case
            print("Gold - 0.26% Chance\n")
            skinrolled = random.randint(16, 31)
            displaycaserewards(skinrolled, csgoweaponcase)

        elif case == gammacase: # Gamma Case
            print("Gold - 0.26% Chance\n")
            skinrolled = random.randint(15, 30)
            displaycaserewards(skinrolled, csgoweaponcase)

        elif case == dreamsandnightmarescase: # Dreams and Nightmares Case
            print("Gold - 0.26% Chance\n")
            skinrolled = random.randint(16, 31)
            displaycaserewards(skinrolled, csgoweaponcase)

        elif case == kilowattcase: # Dreams and Nightmares Case
            print("Gold - 0.26% Chance\n")
            skinrolled = random.randint(17, 32)
            displaycaserewards(skinrolled, csgoweaponcase)

    else:
        print("error?")

def invfullcheck():
    global maxinvspace
    if len(userinventory) == maxinvspace:
        return True
    else:
        return False

def casedisplay():
    global money
    print("Loading Case Display Page...\n")
    time.sleep(2)
    print("Here are the cases:\n")
    time.sleep(1)

    i = 1
    for case_name, case_details in casedict.items():
        print(f"{i} - {case_name} | £{case_details['price']:.2f}")
        time.sleep(0.25)
        i += 1

    time.sleep(1.5)
    print("\nBy naming the case or it's number in the list, what would you like to open?\n")
    time.sleep(0.25)
    caseselection = input("")

    if caseselection.lower().strip() == "cs:go weapon case" or caseselection.strip() == "1":
        if invfullcheck() == False:
            if money >= csgoweaponcase["price"]:
                money -= csgoweaponcase["price"]
                time.sleep(1)
                print(f"\n(You just spent £{csgoweaponcase["price"]})")
                time.sleep(1)
                print("Opening CS:GO Weapon Case...")
                time.sleep(1.5)
                print("...")
                caseopener(csgoweaponcase)
            else:
                print("You can't afford this case; Try a cheaper one!\nReturning...")
                time.sleep(1.5)
                landingpage()
        else:
            print("\nYour inventory is full!\nPlease make space by selling some items.")
            print("Returning to Landing Page...")
            landingpage()
    elif caseselection.lower().strip() == "operation bravo case" or caseselection.strip() == "2":
        if invfullcheck() == False:
            if money >= operationbravocase["price"]:
                money -= operationbravocase["price"]
                time.sleep(1)
                print(f"(You just spent £{operationbravocase["price"]})")
                time.sleep(1)
                print("Opening Operation Bravo Case...")
                time.sleep(1.5)
                print("...")
                caseopener(operationbravocase)
            else:
                print("You can't afford this case; Try a cheaper one!\nReturning...")
                time.sleep(1.5)
                landingpage()
        else:
            print("Your inventory is full!\nPlease make space by selling some items.")
            print("Returning to Landing Page...")
            time.sleep(1.5)
            landingpage()

    elif caseselection.lower().strip() == "gamma case" or caseselection.strip() == "3":
        if invfullcheck() == False:
            if money >= gammacase["price"]:
                money -= gammacase["price"]
                time.sleep(1)
                print(f"(You just spent £{gammacase["price"]})")
                time.sleep(1)
                print("Opening Gamma Case...")
                time.sleep(1.5)
                print("...")
                caseopener(gammacase)
            else:
                print("You can't afford this case; Try a cheaper one!\nReturning...")
                time.sleep(1.5)
                landingpage()
        else:
            print("Your inventory is full!\nPlease make space by selling some items.")
            print("Returning to Landing Page...")
            time.sleep(1.5)
            landingpage()

    elif caseselection.lower().strip() == "dreams and nightmares case" or caseselection.strip() == "4":
        if invfullcheck() == False:
            if money >= dreamsandnightmarescase["price"]:
                money -= dreamsandnightmarescase["price"]
                time.sleep(1)
                print(f"(You just spent £{dreamsandnightmarescase["price"]})")
                time.sleep(1)
                print("Opening Dreams and Nightmares Case...")
                time.sleep(1.5)
                print("...")
                caseopener(dreamsandnightmarescase)
            else:
                print("You can't afford this case; Try a cheaper one!\nReturning...")
                time.sleep(1.5)
                landingpage()
        else:
            print("Your inventory is full!\nPlease make space by selling some items.")
            print("Returning to Landing Page...")
            time.sleep(1.5)
            landingpage()

    elif caseselection.lower().strip() == "kilowatt case" or caseselection.strip() == "5":
        if invfullcheck() == False:
            if money >= kilowattcase["price"]:
                money -= kilowattcase["price"]
                time.sleep(1)
                print(f"(You just spent £{kilowattcase["price"]})")
                time.sleep(1)
                print("Opening Kilowatt Case...")
                time.sleep(1.5)
                print("...")
                caseopener(kilowattcase)
            else:
                print("You can't afford this case; Try a cheaper one!\nReturning...")
                time.sleep(1.5)
                landingpage()
        else:
            print("Your inventory is full!\nPlease make space by selling some items.")
            print("Returning to Landing Page...")
            time.sleep(1.5)
            landingpage()

def landingpageoptions(option):

    if option.strip().title() == "Open Cases" or option.strip() == "1":
        print("Let's open some cases.\n")
        time.sleep(1)
        print("---------------------------------------")
        time.sleep(2)
        casedisplay()

    elif option.strip().title() == "View Inventory" or option.strip() == "2":
        print("Let's view your inventory.\n")
        time.sleep(1)
        print("---------------------------------------")
        time.sleep(2)
        viewinventory()

    elif option.strip().title() == "View Market" or option.strip() == "3":
        print("Let's view the market.\n")
        time.sleep(1)
        print("---------------------------------------")
        time.sleep(2)
        viewmarket()

    elif option.strip().title() == "Quit" or option.strip() == "4":
        print("Thanks for playing!\n")
        time.sleep(1)
        print("---------------------------------------")
        time.sleep(0.25)
        quit()
    
    else:
        print("error; returning to prompt...")
        landingpage()

def landingpage():
    global money
    # Features:
    # Open Cases / Access Inventory / Sell Owned Items / Access Market / View Case Drops / View Inventory Metrics
    global firsttime

    if firsttime:

        startingbets = 150
        money += startingbets
        print("Welcome to the Landing Page!")
        time.sleep(1)
        print("Here is where you will be able to perform most of your actions.\n")
        time.sleep(2)
        print(f"Here's £{startingbets} in starting funds.\n")
        time.sleep(1)

        print("Rarity List of Items:\nMil-Spec - 79.92%\nRestricted - 15.98%\nClassified - 3.20%\nCovert - 0.64%\nRare Special Item (Knife or Gloves): 0.26%\n")

    firsttime = False

    print(f"\nCurrent Balance: £{money:.2f}")
    time.sleep(2)
    print("What would you like to do today?\n")
    selection = input("1 - Open Cases\n2 - View Inventory\n3 - View Market\n4- Quit\n")
    time.sleep(1)
    landingpageoptions(selection)

# ----- Main Program ----- #
global firsttime
firsttime = True
print("Welcome to Adheem's CS2 Case Opener & Skin Store!")
time.sleep(1)
print("In this store, you will be able to\n- Unbox CS2 Cases for RARE items!\n- Buy and Sell Items on the Market!\n")
time.sleep(2)
print("Before you enter, we must ask: How old are you? (You must be 18+ to play.)\n")
time.sleep(0.5)
enteredAge = input("\n")
enteredAge = int(enteredAge.strip().lower())

if ageverification(enteredAge):
    print("\nNice! You've been verified, and are allowed to play today!\n")
    time.sleep(1)
    print("Loading Landing Page...\n")
    time.sleep(1.5)
    landingpage()
else:
    print("\nI'm sorry, but you are either too young to play, or you entered an invalid age.\n")

    exit()

if money == 0:
    print("You lose!")