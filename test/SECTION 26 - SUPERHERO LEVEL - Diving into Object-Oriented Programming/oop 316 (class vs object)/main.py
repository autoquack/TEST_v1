class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def compute_area(self):
        return pow(self.side_length, 2)

if __name__ == "__main__":
    example_square = Square(15)
    print(example_square.compute_area())
    
    small_square = Square(2)
    print(small_square.compute_area())

    big_square = Square(1000)
    print(big_square.compute_area())