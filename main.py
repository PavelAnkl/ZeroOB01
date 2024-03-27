class Warrior():
    # характеристики персонажа
    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color

    # функции персонажа (методы)
    # спать
    def sleep (self):
        print(f'{self.name} лег спать')
        self.endurance += 2
    # есть
    def eat (self):
        print(f'{self.name} поел')
        self.power += 1
    # бить
    def hit (self):
        print(f'{self.name} бьёт соперника')
        self.endurance -= 6
    # ходить
    def walk (self):
        print(f'{self.name} гуляет')
    # вывод информации
    def info (self):
        print(f'Имя воина - {self.name}')
        print(f'Сила воина - {self.power}')
        print(f'Выносливость воина - {self.endurance}')
        print(f'Цвет волос воина - {self.hair_color}')