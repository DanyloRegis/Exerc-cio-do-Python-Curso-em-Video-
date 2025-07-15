class Computer:
    def __init__(self,model,speed):
        self.model = model
        self.speed = speed
        

class LaptopComputer(Computer):
    def __init__(self, weight: float, model: str, speed: int):
        self.weight = weight
        super().__init__(model, speed)


    def __str__(self):
        return f"Laptop(model={self.model}, speed={self.speed}, weight={self.weight})"
    

if __name__ == "__main__":
    laptop = LaptopComputer("NoteBook Pro15", 1500, 2)
print(laptop)
