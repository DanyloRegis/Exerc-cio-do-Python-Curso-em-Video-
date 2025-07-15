class Person:
    def __init__(self, name: str, age: int, height: float, weigh: float):
        self.name = name
        self.age = age
        self.height = height
        self.weigh = weigh
        self.weigh_ins = 0  # Initialize the number of weigh-ins to 0
        
class BabyCentre:
    def weigh(self, person: Person):
        person.weigh_ins += 1
        # return the weight of the person passed as an argument
        return person.weigh
    
    def feed(self, person: Person):
        # feed the person by increasing their weight
        person.weigh += 1
        return person.weigh
    
    def weigh_ins(self, person: Person):
        # return the number of weigh-ins for the specific person
        return person.weigh_ins

baby_centre = BabyCentre()

eric = Person("Eric", 1, 110, 7)
peter = Person("Peter", 33, 176, 85)

print(f"Total number of weigh-ins is {baby_centre.weigh_ins(eric)}")

baby_centre.weigh(eric)
baby_centre.weigh(eric)

print(f"Total number of weigh-ins is {baby_centre.weigh_ins(eric)}")

baby_centre.weigh(eric)
baby_centre.weigh(eric)
baby_centre.weigh(eric)
baby_centre.weigh(eric)

print(f"Total number of weigh-ins is {baby_centre.weigh_ins(eric)}")

baby_centre.feed(eric)
baby_centre.feed(eric)
baby_centre.feed(eric)

print(f"{eric.name} weighs {baby_centre.weigh(eric)} kg")
print(f"{peter.name} weighs {baby_centre.weigh(peter)} kg")