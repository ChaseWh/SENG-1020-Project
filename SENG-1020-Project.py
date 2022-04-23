class BudgetClass:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def add_money(self, money):
        self.balance = money

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

def create_budget(budget_name):
    

print('Welcome, please choose from the options below \n'
      '1 - Create a new budget \n'
      '2 - Add funds to a budget \n'
      '3 - Remove funds from a budget \n'
      '4 - Check available funds of a budget \n'
      '5 - Remove funds from a budget \n'
      '6 - View history of fund allocations\n'
      '0 - Stop program\n')


input1 = 'cars'
food = BudgetClass('food')
food.add_money(1000)
ente = BudgetClass(input1)
ente.add_money(400)
print(ente.name)
food.transfer_bal(200, ente)
ente.display_bal()