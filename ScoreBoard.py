from turtle import Turtle  # Importing the Turtle class from the turtle module

# Constants for text alignment and font settings
ALIGN = "center"  # Aligning text to the center
FONT = ('courier', 16, 'normal')  # Font settings: type, size, and style

class ScoreBoard(Turtle):  # Defining the ScoreBoard class that inherits from Turtle
    def __init__(self):
        super().__init__()  # Calling the constructor of the Turtle class

        # Reading the high score from the text file
        with open("./high_score.txt") as file:
            self.high_score = int(file.read().strip())  # Strip to remove any extra spaces or newlines

        self.ht()  # Hiding the turtle cursor (pen state)
        self.score = 0  # Initializing the score to 0
        self.color("white")  # Setting the color of the text to white
        self.pu()  # Lifting the pen to prevent drawing while moving
        self.goto(0, 310)  # Moving the scoreboard to the top of the screen
        self.update_score()  # Calling the method to display the initial score

    def update_score(self):
        """Clears the previous score and writes the updated score."""
        self.clear()  # Clearing any previous text on the screen
        # Writing the current score and high score
        self.write(f"SCORE: {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)

    def reset(self):
        """Resets the score and updates the high score if needed."""
        # Check if the current score exceeds the high score
        if self.score > self.high_score:
            self.high_score = self.score  # Update the high score
            # Save the new high score to the text file
            with open("./high_score.txt", mode="w") as file:
                file.write(f"{self.high_score}")

        self.score = 0  # Resetting the score to 0
        self.update_score()  # Display the reset score

    def increment_score(self):
        """Increments the score by 1 and updates the display."""
        self.score += 1  # Increasing the score
        self.update_score()  # Updating the display with the new score
