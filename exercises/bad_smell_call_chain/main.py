# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

class Person:
    def __init__(self, room, street, city, population, planet):
        self.room = room
        self.city = city
        self.street = street
        self.population = population
        self.planet = planet

    def get_room(self):
        return self.room

    def get_street(self):
        return self.street

    def get_city(self):
        return self.city

    def get_population(self):
        return self.population

    def get_planet(self):
        return self.planet

# TODO после выполнения задания попробуйте
# сделать экземпляр класса person и вызвать новые методы.
if __name__ == '__main__':
    person = Person(536, "Ивановская", "Екатеринбург", 3000000, "Земля")
    print(person.get_room())
    print(person.get_population())
    print(person.get_city())
    print(person.get_street())
    print(person.get_planet())

