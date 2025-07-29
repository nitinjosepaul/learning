class Fruit(object):
    def __init__(self, name, color, shape):
        self.name = name
        self.color = color
        self.shape = shape
        print(f"Initialized fruit {self.name}")

    def get_nutrition(self):
        print(f"This method gives information about nutrition for {self.name}")

    def get_shape(self):
        print(f"Shape of {self.name} is {self.shape}")


class Banana(Fruit):
    def __init__(self):
        super().__init__(name=Banana.__name__,
                         color='yellow',
                         shape='curved and elongated with cylindrical form')

    def get_nutrition(self):
        nutrition_values = {
                            'Calories' : '105 kcal',
                            'Carbohydrates' : '27 grams',
                            'Protein' : '1.3 grams',
                            'Fat' : '0.3 grams'
                            }
        print(f"Nutritional values for {self.name}")
        print("=" * 30)
        for item in nutrition_values:
            print(f"{item} : {nutrition_values[item]}")

    def get_color(self):
        print(f"Color of {self.name} is {self.color}")

b = Banana()
b.get_color()
b.get_shape()
b.get_nutrition()