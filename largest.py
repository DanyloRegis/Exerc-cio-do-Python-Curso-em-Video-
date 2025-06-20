def largest():
    with open("numbers.txt", "r") as file:
        numbers = file.readlines()
        number = [int(num.strip()) for num in numbers if num.strip().isdigit()]
        max_value = max(number) if number else None
    print(max_value) 
    
if __name__ == "__main__":
    largest()