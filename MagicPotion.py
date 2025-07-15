class SecretMagicPotion:
    def __init__(self,name: str, master_password: str):
        self.__ingredients = {}
        self.__name = name
        self.__master_password = master_password
    
    def add_ingredient(self, ingredient: str, amount: float, password: str):
        if password == self.__master_password:
            self.__ingredients[ingredient] = amount
        else:
            print("Access denied. Incorrect password.")
    
    def print_recipe(self, password: str):
        if password == self.__master_password:
            print(f"{self.__name}:")
            for ingredient, amount in self.__ingredients.items():
                print(f"{ingredient}: {amount}")
        else:
            print("Access denied. Incorrect password.")

if __name__ == "__main__":
    diminuendo = SecretMagicPotion("Diminuendo maximus", "hocuspocus")
    diminuendo.add_ingredient("Toadstool", 1.5, "hocuspocus")
    diminuendo.add_ingredient("Magic sand", 3.0, "hocuspocus")
    diminuendo.add_ingredient("Frogspawn", 4.0, "hocuspocus")
    diminuendo.print_recipe("hocuspocus")

    diminuendo.print_recipe("pocushocus")