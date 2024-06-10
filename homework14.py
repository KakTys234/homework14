class House:
    def __init__(self, nameHouse, numberOfFloors):
        self.nameHouse = nameHouse
        self.numberOfFloors = numberOfFloors
        self.say_info()


    def setNumberOfFloors(self, floors):
        self.numberOfFloors = floors



    def say_info(self):
        print(f'Название: {self.nameHouse}, Количество этажей: {self.numberOfFloors}')



Orion = House('Орион', 23)
Object = House('Объект', 25)

Kemping = House('Кемпинг', 2)