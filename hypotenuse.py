import math
def hypotenuse(leg1: float, leg2: float):
    left_squared = leg1 ** 2
    right_squared = leg2 ** 2
    hypotenuse_length = math.sqrt(left_squared + right_squared)
    #breakpoint()
    return hypotenuse_length


if __name__ == "__main__":
    x = hypotenuse(3, 4)
    print(f"The length of the hypotenuse is: {x}")