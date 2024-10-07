class Air:
    def __add__(self, other):
        if other.__class__.__name__ == 'Water':
            return Storm()
        elif other.__class__.__name__ == 'Fire':
            return Lightning()
        elif other.__class__.__name__ == 'Earth':
            return Dust()


class Fire:
    def __add__(self, other):
        if other.__class__.__name__ == 'Air':
            return Lightning()
        elif other.__class__.__name__ == 'Earth':
            return Lava()
        elif other.__class__.__name__ == 'Water':
            return Steam()


class Earth:
    def __add__(self, other):
        if other.__class__.__name__ == 'Air':
            return Dust()
        elif other.__class__.__name__ == 'Fire':
            return Lava()
        elif other.__class__.__name__ == 'Water':
            return Dirt()


class Water:
    def __add__(self, other):
        if other.__class__.__name__ == 'Air':
            return Storm()
        elif other.__class__.__name__ == 'Fire':
            return Steam()
        elif other.__class__.__name__ == 'Earth':
            return Dirt()


class Storm:
    answer = 'Получился шторм'


class Lightning:
    answer = 'Получилась молния'


class Steam:
    answer = 'Получился пар'


class Dust:
    answer = 'Получилась пыль'


class Dirt:
    answer = 'Получилась грязь'


class Lava:
    answer = 'Получилась лава'


if __name__ == '__main__':
    first = Fire()
    second = Water()
    rezult = first + second
    print(rezult.answer)
