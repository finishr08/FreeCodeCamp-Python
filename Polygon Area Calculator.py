class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            picture = ""
            for i in range(self.height):
                picture += '*' * self.width + '\n'
            return picture

    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.height // shape.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.set_width(side)
        self.set_height(side)

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

    def __str__(self):
        return f"Square(side={self.width})"

# Create a Rectangle instance
rectangle = Rectangle(width=5, height=10)

# Output information about the Rectangle
print(rectangle)
print(f"Area: {rectangle.get_area()}")
print(f"Perimeter: {rectangle.get_perimeter()}")
print(f"Diagonal: {rectangle.get_diagonal()}")
print("Picture:")
print(rectangle.get_picture())
print(f"Amount Inside: {rectangle.get_amount_inside(Square(side=4))}")

# Create a Square instance
square = Square(side=5)

# Output information about the Square
print(square)
print(f"Area: {square.get_area()}")
print(f"Perimeter: {square.get_perimeter()}")
print(f"Diagonal: {square.get_diagonal()}")
print("Picture:")
print(square.get_picture())
print(f"Amount Inside: {square.get_amount_inside(Rectangle(width=2, height=2))}")
