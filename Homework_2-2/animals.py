from abc import ABC, abstractmethod

class Animal(ABC):
    satiety_max = 100
    scream = "AAAAAA"  #defualt scream
    item = None
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
        return self.scream
    
    @abstractmethod
    def collect(self):
        pass


class Bird(Animal):
    item = 'Яйцо'
    def __init__(self, name, weight, egg_number = 3, satiety_level = 50):
        Animal.__init__(self, name, weight, satiety_level)
        self.egg_number = egg_number

    def collect(self):
        """
        Return int with number of eggs you collected
        """
        egg_to_return = self.egg_number
        self.egg_number = 0
        return egg_to_return


class MilkAnimal(Animal):
    """
    Parent class for animals with milk.
    """
    item = "Молоко"
    def __init__(self, name, weight, satiety_level=100, milk_level=1.0):
        Animal.__init__(self, name, weight, satiety_level=100)
        self.milk_level = milk_level
    
    def collect(self):
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
    item = 'Шерсть'
    def __init__(self, name, weight, satiety_level=100, ready_to_shear = True):
        Animal.__init__(self, name, weight, satiety_level=100)
        self.ready_to_shear = ready_to_shear

    def collect(self):
        if self.ready_to_shear:
            return '1 кг'
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
chicken_2 = Chicken('Кукареку', 3.8)

goat_1 = Goat('Рога', 35)
goat_2 = Goat('Копыта', 33, satiety_level=35)

duck_1 = Duck('Кряква', 6)

cow_1.get_scream()
goose_1.get_scream()


all_animals = [goose_1, goose_2, cow_1, sheep_1, sheep_2, chicken_1, chicken_2, goat_1, goat_2, duck_1]

for animal in all_animals:
    animal.feed(1)
    colletcted_item = animal.collect()
    # scream = animal.get_scream()
    print(f"{animal.name} кричит {animal.get_scream()}, его уровень голода после кормления {animal.satiety_level}%. С животного собрано {colletcted_item} {animal.item}")

sum_weight = 0.0

for animal in all_animals:
    sum_weight += animal.weight

print('Общий вес всех животных:', round(sum_weight, 2))

all_animals.sort(key=lambda animal: animal.weight)
print("Самое тяжелое животное:", all_animals[-1].name)
