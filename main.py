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

    def speak(self):
        return self.voice


class Milk:
    """Животные, дающие молоко"""
    def __init__(self, satiety):
        self.satiety = satiety

    def milking(self):
        if self.satiety >= 5:
            self.satiety -= 2
            return 'Надоили 2 ведра молока.'
        elif 0 < self.satiety < 5:
            self.satiety -= 1
            return 'Надоили 1 ведро молока.'
        else:
            return 'Нужно покормить.'


class Wool:
    """Животные, с которых можно настричь шерсть"""
    def __init__(self, satiety):
        self.satiety = satiety

    def cut(self):
        if self.satiety >= 5:
            self.satiety -= 2
            return 'Настригли 2 корзины шерсти.'
        elif 0 < self.satiety < 5:
            self.satiety -= 1
            return 'Настригли 1 корзину шерсти.'
        else:
            return 'Нужно покормить.'


class Eggs:
    """Животные, несущие яйца"""
    def __init__(self, satiety):
        self.satiety = satiety

    def coll_eggs(self):
        if self.satiety >= 5:
            self.satiety -= 2
            return 'Собрали 5 яиц.'
        elif 0 < self.satiety < 5:
            self.satiety -= 1
            return 'Собрали 2 яйца.'
        else:
            return 'Нужно покормить.'


class Cow(Animals, Milk):
    """Корова"""
    animal_type = "Корова"
    voice = "Мууу"


class Goat(Animals, Milk):
    """Коза"""
    animal_type = "Коза"
    voice = "Меее"

    def milking(self):
        if self.satiety >= 5:
            self.satiety -= 2
            return 'Надоили 10 литров молока.'
        elif 0 < self.satiety < 5:
            self.satiety -= 1
            return 'Надоили 4 литра молока.'
        else:
            return 'Нужно покормить.'


class Ram(Animals, Wool):
    """Баран"""
    animal_type = "Баран"
    voice = "Беее"


class Goose(Animals, Eggs):
    """Гусь"""
    animal_type = "Гусь"
    voice = "Гага"


class Hen(Animals, Eggs):
    """Курица"""
    animal_type = "Курица"
    voice = "Коооо"


class Duck(Animals, Eggs):
    """Утка"""
    animal_type = "Утка"
    voice = "Крякря"


def main():
    manya = Cow("Манька", 720, 6)
    roga, kopyta = Goat("Рога", 120, 8), Goat("Копыта", 90)
    barash, kudryav = Ram("Барашек", 45), Ram("Кудрявый", 50)
    seriy, beliy = Goose("Серый", 3, 3), Goose("Белый", 4)
    ko_ko, kukareku = Hen("Ко-Ко", 3, 9), Hen("Кукареку", 4)
    kryakva = Duck("Кряква", 1, 1)
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

    for animal in animals:
        print(f'{animal.feed(1)} животное {animal.animal_type.lower()} "{animal.name}"')
        print(animal.speak())
        print(f'Сытость увеличилась до {animal.satiety}\n{"-" * 20}')


if __name__ == __name__:
    main()
