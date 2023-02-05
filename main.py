# Задача №1 "Ферма Дядюшки Джо"
from pprint import pprint


class Cow:
    """Корова"""
    animal_type = "Корова"
    speak = "Мууу"

    def __init__(self, name, weight, satiety=5):
        self.name = name
        self.weight = weight
        self.satiety = satiety

    def feed(self, eat):
        self.satiety += eat
        return 'Покормили'

    def milking(self):
        if self.satiety >= 5:
            self.satiety -= 2
            return 'Надоили 2 ведра молока.'
        elif 0 < self.satiety < 5:
            self.satiety -= 1
            return 'Надоили 1 ведро молока.'
        else:
            return 'Нужно покормить'


class Goat:
    """Коза"""
    animal_type = "Коза"
    speak = "Меее"

    def __init__(self, name, weight, satiety=5):
        self.name = name
        self.weight = weight
        self.satiety = satiety

    def milking(self):
        if self.satiety >= 5:
            self.satiety -= 2
            return 'Надоили 2 литра молока.'
        elif 0 < self.satiety < 5:
            self.satiety -= 1
            return 'Надоили 1 литр молока.'
        else:
            return 'Нужно покормить'


class Ram:
    """Баран"""
    animal_type = "Баран"
    speak = "Беее"

    def __init__(self, name, weight, satiety=5):
        self.name = name
        self.weight = weight
        self.satiety = satiety

    def feed(self, eat):
        self.satiety += eat
        return 'Покормили'

    def cut(self):
        if self.satiety >= 5:
            self.satiety -= 2
            return 'Настригли 2 корзины шерсти.'
        elif 0 < self.satiety < 5:
            self.satiety -= 1
            return 'Настригли 1 корзину шерсти.'
        else:
            return 'Нужно покормить.'


class Goose:
    """Гусь"""
    animal_type = "Гусь"
    speak = "Гага"

    def __init__(self, name, weight, satiety=5):
        self.name = name
        self.weight = weight
        self.satiety = satiety

    def feed(self, eat):
        self.satiety += eat
        return 'Покормили'

    def coll_eggs(self):
        if self.satiety >= 5:
            self.satiety -= 2
            return 'Собрали 5 яиц.'
        elif 0 < self.satiety < 5:
            self.satiety -= 1
            return 'Собрали 2 яйца.'
        else:
            return 'Нужно покормить.'


class Hen:
    """Курица"""
    animal_type = "Курица"
    speak = "Коооо"

    def __init__(self, name, weight, satiety=5):
        self.name = name
        self.weight = weight
        self.satiety = satiety

    def feed(self, eat):
        self.satiety += eat
        return 'Покормили'

    def coll_eggs(self):
        if self.satiety >= 5:
            self.satiety -= 2
            return 'Собрали 5 яиц.'
        elif 0 < self.satiety < 5:
            self.satiety -= 1
            return 'Собрали 2 яйца.'
        else:
            return 'Нужно покормить.'


class Duck:
    """Утка"""
    animal_type = "Утка"
    speak = "Крякря"

    def __init__(self, name, weight, satiety=5):
        self.name = name
        self.weight = weight
        self.satiety = satiety

    def feed(self, eat):
        self.satiety += eat
        return 'Покормили'

    def coll_eggs(self):
        if self.satiety >= 5:
            self.satiety -= 2
            return 'Собрали 5 яиц.'
        elif 0 < self.satiety < 5:
            self.satiety -= 1
            return 'Собрали 2 яйца.'
        else:
            return 'Нужно покормить.'


def main():
    manya = Cow("Манька", 500)
    roga = Goat("Рога", 60)
    kopyta = Goat("Копыта", 70)
    barash = Ram("Барашек", 45)
    kudryav = Ram("Кудрявый", 50)
    seriy = Goose("Серый", 15)
    beliy = Goose("Белый", 5)
    ko_ko = Hen("Ко-Ко", 3)
    kukareku = Hen("Кукареку", 4)
    kryakva = Duck("Кряква", 5)
    animals = [manya, roga, kopyta, barash, kudryav, seriy, beliy, ko_ko, kukareku, kryakva]
    total_weight = 0
    weight = 0
    name_animal_max_weight = ''

    for animal in animals:
        total_weight = total_weight + animal.weight
        if weight < animal.weight:
            weight = animal.weight
            name_animal_max_weight = str(f'{animal.animal_type} "{animal.name}"')

    print(f'Общий вес животных: {total_weight}.')
    print(f'Самое тяжелое животное: {name_animal_max_weight}.')


if __name__ == __name__:
    main()