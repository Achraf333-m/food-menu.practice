class Menu:
    def __init__(self, dish, items, time) -> None:
        self.dish = dish
        self.items = items
        self.time = time

    def contents(self):
        return (
            "The dish: "
            + self.dish
            + " , will require "
            + str(self.items)
            + " and will take "
            + str(self.time)
            + " min to make!"
        )

pizza = Menu('Pizza', ['flour', 'cheese', 'tomatoes'], 45)
pasta = Menu('Pasta', ['pasta', 'sauce', 'tomatoes'], 35)
burger = Menu('Burger', ['bread', 'meat', 'pickles'], 15)

print(pizza.contents())
print(pasta.contents())
print(burger.contents())
