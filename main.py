# Задача №1 "Ферма Дядюшки Джо". Продолжение.
class Animals:
    """Животные"""

    def __init__(self, name, weight, satiety=5):
        self.name = name
        self.weight = weight
        self.satiety = satiety

    def feed(self, eat):
        self.satiety += eat
        return 'Покормили'


class Milk(Animals):
    """Животные, дающие молоко"""

    def milking(self):
        if self.satiety >= 5:
            self.satiety -= 2
            return 'Надоили 2 ведра молока.'
        elif 0 < self.satiety < 5:
            self.satiety -= 1
            return 'Надоили 1 ведро молока.'
        else:
            return 'Нужно покормить.'


class Wool(Animals):
    """Животные, с которых можно настричь шерсть"""

    def cut(self):
        if self.satiety >= 5:
            self.satiety -= 2
            return 'Настригли 2 корзины шерсти.'
        elif 0 < self.satiety < 5:
            self.satiety -= 1
            return 'Настригли 1 корзину шерсти.'
        else:
            return 'Нужно покормить.'


class Eggs(Animals):
    """Животные, несущие яйца"""

    def coll_eggs(self):
        if self.satiety >= 5:
            self.satiety -= 2
            return 'Собрали 5 яиц.'
        elif 0 < self.satiety < 5:
            self.satiety -= 1
            return 'Собрали 2 яйца.'
        else:
            return 'Нужно покормить.'


class Cow(Milk):
    """Корова"""
    animal_type = "Корова"
    speak = "Мууу"


class Goat(Milk):
    """Коза"""
    animal_type = "Коза"
    speak = "Меее"

    def milking(self):
        if self.satiety >= 5:
            self.satiety -= 2
            return 'Надоили 10 литров молока.'
        elif 0 < self.satiety < 5:
            self.satiety -= 1
            return 'Надоили 4 литра молока.'
        else:
            return 'Нужно покормить.'


class Ram(Wool):
    """Баран"""
    animal_type = "Баран"
    speak = "Беее"


class Goose(Eggs):
    """Гусь"""
    animal_type = "Гусь"
    speak = "Гага"


class Hen(Eggs):
    """Курица"""
    animal_type = "Курица"
    speak = "Коооо"


class Duck(Eggs):
    """Утка"""
    animal_type = "Утка"
    speak = "Крякря"


def main():
    manya = Cow("Манька", 720, 2)
    roga = Goat("Рога", 120)
    kopyta = Goat("Копыта", 90)
    barash = Ram("Барашек", 45)
    kudryav = Ram("Кудрявый", 50)
    seriy = Goose("Серый", 3)
    beliy = Goose("Белый", 4)
    ko_ko = Hen("Ко-Ко", 3)
    kukareku = Hen("Кукареку", 4)
    kryakva = Duck("Кряква", 1)
    animals = [manya, roga, kopyta, barash, kudryav, seriy, beliy, ko_ko, kukareku, kryakva]
    total_weight = 0
    weight = 0
    name_animal_max_weight = ''

    for animal in animals:
        total_weight = total_weight + animal.weight
        if weight < animal.weight:
            weight = animal.weight
            name_animal_max_weight = str(f'{animal.animal_type.lower()} "{animal.name}"')

    print(f'Общий вес животных: {total_weight}.')
    print(f'Самое тяжелое животное: {name_animal_max_weight}.')


if __name__ == __name__:
    main()
