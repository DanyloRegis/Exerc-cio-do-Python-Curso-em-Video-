class Car:
    def __init__(self, make: str, top_speed: int):
        self.make = make
        self.top_speed = top_speed
    def __str__(self):
        return f"{self.make} with top speed of {self.top_speed} km/h"

def fastest_car(cars):
    if not cars:
        return None
    faster = cars[0]
    for car in cars:
        if car.top_speed > faster.top_speed:
            faster = car
    return faster

if __name__ == "__main__":
    car1 = Car("Saab", 195)
    car2 = Car("Lada", 110)
    car3 = Car("Ferrari", 280)
    car4 = Car("Trabant", 85)

    cars = [car1, car2, car3, car4]
    print(fastest_car(cars))