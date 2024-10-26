from random import randint, choice  # Importing randint and choice functions from the random module
from turtle import Turtle  # Importing the Turtle class from the turtle module

# List of colors to choose from for the food item
COLOR_LIST = ["turquoise", "dark violet", "orange red", "gold", "deep pink", 
              "medium slate blue", "purple", "dark goldenrod", "dark khaki", 
              "spring green"]

class Food(Turtle):  # Defining the Food class that inherits from the Turtle class
    def __init__(self):
        super().__init__()  # Calling the constructor of the Turtle class
        self.shape("circle")  # Setting the shape of the food to a circle
        self.pu()  # Lifting the pen to prevent drawing while moving
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Setting the size of the food shape
        self.color(choice(COLOR_LIST))  # Randomly choosing a color from COLOR_LIST
        self.speed("fastest")  # Setting the drawing speed to the fastest
        self.refresh()  # Calling the refresh method to position the food

    def refresh(self):
        # Changing the color of the food to a new random color
        self.color(choice(COLOR_LIST))
        
        # Generating random coordinates for the food position within the specified range
        x_coordinate = randint(-300, 300)
        y_coordinate = randint(-300, 300)
        
        # Moving the food to the new random coordinates
        self.goto(x_coordinate, y_coordinate)
