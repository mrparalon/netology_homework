class Animal:
    satiety_max = 100
    scream = "AAAAAA"  #defualt scream

    def __init__(self, name, weight, satiety_level = 100):
        self.name = name
        self.weight = weight
        self.satiety_level = satiety_level

    def feed(self, food_amount):
        """
        Get food amount in kg(int), return satiety level in % (int)
        """
        self.satiety_level += food_amount * 10
        if self.satiety_level >= self.satiety_max:
            self. satiety_level = self.satiety_max
        return self.satiety_level

    def get_scream(self):
        print(self.scream)


class Bird(Animal):
    
    def __init__(self, name, weight, egg_number = 3, satiety_level = 50):
        Animal.__init__(self, name, weight, satiety_level)
        self.egg_number = egg_number

    def get_egg(self, eggs_to_get):
        """
        Return int with number of egg you get and change bird's eggs number
        """
        if self.egg_number >= eggs_to_get:
            self.egg_number -= eggs_to_get
            return eggs_to_get
        else:
            self.egg_copy = self.egg_number
            self.egg_number = 0
            return self.egg_copy


class MilkAnimal(Animal):
    """
    Parent class for animals with milk.
    """
    def __init__(self, name, weight, satiety_level=100, milk_level=1.0):
        Animal.__init__(self, name, weight, satiety_level=100)
        self.milk_level = milk_level
    
    def get_milk(self):
        """
        Get 1.0 liter of milk from animal. Return milk in liters (float)
        """
        if self.milk_level >= 1.0:
            self.milk_level = round(self.milk_level - 1.0, 1)
            return 1.0
        else:
            print("Было только {} л. молока".format(self.milk_level))
            milk_to_return = self.milk_level
            self.milk_level = 0
            return milk_to_return

class Cow(MilkAnimal):
    """
    Milk level in %
    """
    scream = 'Мууууу'


class Goat(MilkAnimal):
    scream = 'Меееееh' #это коза-скептик


class Sheep(Animal):
    scream = 'Бе-Бе-Бе'

    def __init__(self, name, weight, satiety_level=100, ready_to_shear = True):
        Animal.__init__(self, name, weight, satiety_level=100)
        self.ready_to_shear = ready_to_shear

    def shear(self):
        if self.ready_to_shear:
            return 'Шерсть!'
        else:
            return 'Шерсть еще не выросла'


class Goose(Bird):
    scream = 'Га-Га-Га'


class Chicken(Bird):
    scream = 'Ко-Ко-Ко'

class Duck(Bird):
    swimming = True
    scream = 'Кря-Кря-Зря'


goose_1 = Goose('Серый', 10)
goose_2 = Goose('Белый', 12)

cow_1 = Cow('Манька', 500, milk_level=3.2)

sheep_1 = Sheep('Барашек', 30)
sheep_2 = Sheep('Кудрявый', 34)

chicken_1 = Chicken('Ко-Ко', 4, 1)
chicken_1 = Chicken('Кукареку', 3.8)

goat_1 = Goat('Рога', 35)
goat_2 = Goat('Копыта', 33, satiety_level=35)

duck_1 = Duck('Кряква', 6)



print('Взять яйца гуся 1: ', goose_1.get_egg(4))
print('Количество яиц гуся 1: ', goose_1.egg_number)
print('Покормить гуся 1: ', goose_1.feed(2))
print('Покормить козу 2: ', goat_2.feed(1))
print('Взять яйца курицы 1: ', chicken_1.get_egg(1))
print('Взять яйца утки 1: ', duck_1.get_egg(2))
print('Доить корову 1: ', cow_1.get_milk())
print('Доить козу 1: ', goat_1.get_milk())
print('Стричь овцу 1: ', sheep_1.shear())
cow_1.get_scream()
goose_1.get_scream()
goose_1.feed(1)
goose_2.feed(1)
cow_1
sheep_1.feed(1)
sheep_2.feed(1)
chicken_1.feed(1)
chicken_1.feed(1)
goat_1.feed(1)
goat_2.feed(1)
duck_1.feed(1)

all_animals = [goose_1, goose_2, cow_1, sheep_1, sheep_2, chicken_1, chicken_1, goat_1, goat_2, duck_1]

sum_weight = 0.0

for animal in all_animals:
    sum_weight += animal.weight

print('Общий вес всех животных:', round(sum_weight, 2))

animals_weght_dict = {}

for animal in all_animals:
    animals_weght_dict[animal] = animal.weight
max_weight = max(animals_weght_dict.values())
for animal, weight in animals_weght_dict.items():
    if max_weight == weight:
        print("Самое тяжелое животное: ", animal.name)

