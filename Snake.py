from turtle import *  # Importing all functions and classes from the turtle module

# Constants for movement distance and directions
MOVE_DIS = 20  # Distance the snake moves with each command
UP = 90  # Angle for upward movement
DOWN = 270  # Angle for downward movement
RIGHT = 0  # Angle for rightward movement
LEFT = 180  # Angle for leftward movement

class Snake:  # Defining the Snake class to handle snake-related logic
    def __init__(self):
        self.segments = []  # List to store the segments of the snake
        self.create_snake()  # Creating the initial snake with 3 segments
        self.head = self.segments[0]  # Assigning the first segment as the snake's head

    def create_snake(self):
        """Initializes the snake with 3 segments positioned horizontally."""
        for i in range(3):
            # Adding each segment at (-20*i, 0) to form the initial snake
            self.add_segment((-20 * i, 0))

    def extend_snake(self):
        """Extends the snake by adding a new segment at the position of the last segment."""
        # Get the position of the last segment
        coordinate_x, coordinate_y = self.segments[-1].pos()
        self.add_segment((coordinate_x, coordinate_y))  # Add a new segment at that position

    def add_segment(self, position):
        """Creates a new segment and adds it to the snake."""
        segment = Turtle("square")  # Creating a square-shaped turtle as a segment
        segment.pencolor("black")  # Setting the outline color to black
        segment.fillcolor("white")  # Setting the fill color to white
        segment.pu()  # Lift the pen to avoid drawing lines while moving
        segment.goto(position)  # Move the segment to the specified position
        self.segments.append(segment)  # Add the new segment to the snake's segments list

    def move(self):
        """Moves the snake by shifting each segment to the position of the previous one."""
        # Start from the last segment and move each one to the position of the segment before it
        for i in range(len(self.segments) - 1, 0, -1):
            coordinate_x, coordinate_y = self.segments[i - 1].pos()  # Get the previous segment's position
            self.segments[i].goto(coordinate_x, coordinate_y)  # Move the current segment

        self.head.fd(MOVE_DIS)  # Move the head forward by the defined distance

    def move_up(self):
        """Change the direction to up unless the snake is moving down."""
        if self.head.heading() != DOWN:  # Prevent 180-degree reversal
            self.head.seth(UP)  # Set the heading to UP

    def move_right(self):
        """Change the direction to right unless the snake is moving left."""
        if self.head.heading() != LEFT:  # Prevent 180-degree reversal
            self.head.seth(RIGHT)  # Set the heading to RIGHT

    def move_left(self):
        """Change the direction to left unless the snake is moving right."""
        if self.head.heading() != RIGHT:  # Prevent 180-degree reversal
            self.head.seth(LEFT)  # Set the heading to LEFT

    def move_down(self):
        """Change the direction to down unless the snake is moving up."""
        if self.head.heading() != UP:  # Prevent 180-degree reversal
            self.head.seth(DOWN)  # Set the heading to DOWN

    def reset(self):
        """Resets the snake by moving all segments off-screen and recreating the snake."""
        for segment in self.segments:
            segment.goto(1000, 1000)  # Move each segment far off-screen to hide them
        self.segments.clear()  # Clear the segments list
        self.create_snake()  # Recreate the initial snake with 3 segments
        self.head = self.segments[0]  # Set the new head as the first segment
