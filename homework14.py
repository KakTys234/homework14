class House:
    def __init__(self, nameHouse, numberOfFloors):
        self.nameHouse = nameHouse
        self.numberOfFloors = numberOfFloors

    def setNewNumberOfFloors(self):
        print(f'Название: {self.nameHouse}, Этажей: {self.numberOfFloors}')

Orion = House('Орион', 23)
Object = House('Объект', 25)
