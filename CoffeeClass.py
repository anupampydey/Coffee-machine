# Simulation of actual Coffee Machine
class CoffeeClass:

    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def machine_stock(self):
        print("\nThe coffee machine has:")
        print(self.water, "ml of water")
        print(self.milk, "ml of milk")
        print(self.beans, "gms of coffee beans")
        print(self.cups, "nos. of disposable cups")
        print(self.money, "$ of money")

    def fillmachine(self):
        fil_wtr = int(input("How many ml of water do you want to add: ").strip())
        mycoffee.water += fil_wtr
        fil_mlk = int(input("How many ml of milk do you want to add: ").strip())
        mycoffee.milk += fil_mlk
        fil_bns = int(input("How many gms of coffee beans do you want to add: ").strip())
        mycoffee.beans += fil_bns
        fil_cup = int(input("How many disposable cups of coffee do you want to add:: ").strip())
        mycoffee.cups += fil_cup

    def drawcash(self):
        print("I gave you $", mycoffee.money)
        mycoffee.money = 0

    def makeCoffee(self, cof_typ):
        if (mycoffee.water >= cof_typ.water) and (mycoffee.milk >= cof_typ.milk) \
                and (mycoffee.beans >= cof_typ.beans) and (mycoffee.cups >= cof_typ.cups):
            print("I have enough resources, making you a coffee!")
            mycoffee.water -= cof_typ.water
            mycoffee.milk -= cof_typ.milk
            mycoffee.beans -= cof_typ.beans
            mycoffee.cups -= cof_typ.cups
            mycoffee.money += cof_typ.money
        elif mycoffee.water < cof_typ.water:
            print("Sorry not enough water in stock!")
        elif mycoffee.milk < cof_typ.milk:
            print("Sorry not enough milk in stock!")
        elif mycoffee.cups < cof_typ.cups:
            print("Sorry not enough cups in stock!")
        elif mycoffee.beans < cof_typ.beans:
            print("Sorry not enough coffee beans in stock!")

    def MachineStatus(self, action):
        if action == "remaining":
            mycoffee.machine_stock()
        elif action == "take":
            mycoffee.drawcash()
        elif action == "fill":
            mycoffee.fillmachine()
        elif action == "buy":
            cof_typ = input("\nWhat do you want to buy? 1 - Espresso, 2 - Latte, 3 - Cappuccino "
                            "or 'back' to main menu: ").strip()
            while cof_typ != "back":
                if int(cof_typ) == 1:
                    espre = CoffeeClass(250, 0, 16, 1, 4)
                    mycoffee.makeCoffee(espre)
                    break
                elif int(cof_typ) == 2:
                    latte = CoffeeClass(350, 75, 20, 1, 7)
                    mycoffee.makeCoffee(latte)
                    break
                elif int(cof_typ) == 3:
                    cappu = CoffeeClass(200, 100, 12, 1, 6)
                    mycoffee.makeCoffee(cappu)
                    break


mycoffee = CoffeeClass(400, 540, 120, 9, 550)
print("Initialising the Coffee Machine ...")
action = ""
while action != "exit":
    action = input("\nPlease select the Actions(buy, fill, take, remaining, exit): ").strip()
    mycoffee.MachineStatus(action)
