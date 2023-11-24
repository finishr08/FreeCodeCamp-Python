class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, budget_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {budget_category.category}")
            budget_category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.category:*^30}\n"
        items = ""
        for item in self.ledger:
            items += f"{item['description'][:23]:<23}{item['amount']:>7.2f}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    spendings = [(category.category, sum(item['amount'] for item in category.ledger if item['amount'] < 0)) for category in categories]
    total_spent = sum(spending for _, spending in spendings)

    for i in range(100, -1, -10):
        chart += f"{i:3}| "
        for _, spending in spendings:
            bar = "o" if spending >= i / 100 * total_spent else " "
            chart += f"{bar:3}"
        chart += " \n"

    chart += "    ----------\n"

    max_len = max(len(category.category) for category in categories)
    for i in range(max_len):
        chart += "     "
        for category in categories:
            if i < len(category.category):
                chart += f"{category.category[i]:2}  "
            else:
                chart += "   "
        chart += "\n"

    return chart.rstrip()


# Example usage:
food_category = Category("Food")
clothing_category = Category("Clothing")
auto_category = Category("Auto")

food_category.deposit(1000, "initial deposit")
food_category.withdraw(10.15, "groceries")
food_category.withdraw(15.89, "restaurant and more food")

clothing_category.transfer(50, food_category)

auto_category.deposit(1000, "initial deposit")
auto_category.withdraw(15, "gas")
auto_category.withdraw(30, "oil change")

categories = [food_category, clothing_category, auto_category]

print(food_category)
print(create_spend_chart(categories))
