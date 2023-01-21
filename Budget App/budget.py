class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    def transfer(self, amount, other_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {other_category.name}")
            other_category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def __str__(self):
        title = f"{self.name}".center(30, "*")
        items = "\n".join([f"{item['description'][:23]:<23} {item['amount']:>7.2f}" for item in self.ledger])
        total = f"Total: {self.get_balance():.2f}"
        return f"{title}\n{items}\n{total}"

def create_spend_chart(categories):
    spend = {}
    for category in categories:
        spend[category.name] = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spend[category.name] += abs(item["amount"])

    total_spend = sum(spend.values())
    chart = "Percentage spent by category\n"
    for i in range(100, -10, -10):
        chart += f"{i}|"
        for category in categories:
            if total_spend > 0:
                percent = spend[category.name] / total_spend
                if percent * 100 >= i:
                    chart += " o"
                else:
                    chart += "  "
            else:
                chart += "  "
        chart += "\n"

    chart += "    "
    for category in categories:
        chart += "-" * len(category.name) + "  "
    chart = chart[:-2] + "\n     "

    for char in "".join([category.name[0] for category in categories]):
        chart += char + "  "

    for char in "".join([category.name[1:] for category in categories]):
        chart += char + "  "
    return chart
