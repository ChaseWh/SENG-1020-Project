import time


class BudgetClass:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        budgets.append(self)

    def add_money(self, money):
        self.balance += money

    def remove_money(self, money):
        if self.balance >= money:
            self.balance -= money
        else:
            print("Not enough money")

    def display_bal(self):
        print("current balance: " + str(self.balance))

    def transfer_bal(self, amount, receiving_budget):
        if self.name == receiving_budget.name:
            return
        else:
            if self.balance < amount:
                print("Not enough money")
            else:
                self.balance -= amount
                receiving_budget.balance += amount


def check_funds():
    choice = input("Which budget would you like to check?")
    for budget in budgets:
        if budget.name == choice.lower():
            return print("{}: ${}".format(budget.name, budget.balance))
    print("Cannot find budget with that name!")


def add_funds():
    choice = input("Which budget would you like to add to?")
    money_to_add = input("How much do you want to add?")
    for budget in budgets:
        if budget.name == choice.lower():
            try:
                budget.add_money(int(money_to_add))
            except ValueError:
                return print("Not a valid dollar amount.")
            return print("Updated balance of {}: ${}".format(budget.name, budget.balance))
    print("Cannot find budget with that name!")


def remove_funds():
    choice = input("Which budget would you like to deduct from?")
    money_to_add = input("How much do you want to remove?")
    for budget in budgets:
        if budget.name == choice.lower():
            try:
                budget.add_money(-int(money_to_add))
            except ValueError:
                return print("Not a valid dollar amount.")
            return print("Updated balance of {}: ${}".format(budget.name, budget.balance))
    print("Cannot find budget with that name!")

def transfer_funds():
    from_budget = input("Which budget would you like to take funds from?")
    to_budget = input("Which budget would you like to transfer funds to?")
    money_to_transfer = input("How much do you want to transfer?")
    for i in budgets:
        if i.name == from_budget.lower():
            for j in budgets:
                if j.name == to_budget.lower():
                    try:
                        i.transfer_bal(int(money_to_transfer), j)
                    except ValueError:
                        print("Not a valid dollar amount.")
                    return print("Updated balance of {}: ${} \n"
                                 "Updated balance of {}: ${}".format(j.name, j.balance, i.name, i.balance))
    print("Cannot find budget with that name!")


# setup budgets and a list to store them
budgets = []
food_budget = BudgetClass("food")
clothing_budget = BudgetClass("clothes")
entertainment = BudgetClass("entertainment")

user_input = input(
    'This program allows you to manage funds between the budgets of food, clothing, and entertainment.\n'
    'Please choose from the options below \n'
    '1 - Check available funds of each budget \n'
    '2 - Add funds to a budget \n'
    '3 - Remove funds from a budget \n'
    '4 - Transfer funds between budgets \n'
    '5 - List budgets \n'
    '6 - View history of fund allocations\n'
    '0 - Stop program')

# wait for input
while user_input != "0":
    if user_input == "1":
        check_funds()
    if user_input == "2":
        add_funds()
    if user_input == "3":
        remove_funds()
    if user_input == "4":
        transfer_funds()
    if user_input == "5":
        print("=-=-=Budgets=-=-=")
        for budget in budgets:
            print(budget.name)
    if user_input == "5":
        print("TODO view history")

    # wait then ask for input again
    time.sleep(2)
    user_input = input(
        '1 - Check available funds of each budget \n'
        '2 - Add funds to a budget \n'
        '3 - Remove funds from a budget \n'
        '4 - Transfer funds between budgets \n'
        '5 - List budgets \n'
        '6 - View history of fund allocations\n'
        '0 - Stop program')
