from time import sleep  # Importing sleep function to control game speed
from turtle import *  # Importing all functions and classes from the turtle module
from Food import *  # Importing the Food class from the Food module
from Snake import *  # Importing the Snake class from the Snake module
from scoreboard import *  # Importing the ScoreBoard class from the scoreboard module

# Setting up the game screen
screen = Screen()  # Creating a Screen object
screen.setup(700, 700)  # Setting the canvas size to 700x700 pixels
screen.bgcolor("black")  # Setting the canvas background color to black
screen.title("Welcome To The Snake Game")  # Setting the window title
screen.tracer(0)  # Disabling automatic screen updates for better control

# Creating instances of the game components
snake = Snake()  # Creating the snake object
score = ScoreBoard()  # Creating the scoreboard object
food = Food()  # Creating the food object

# Setting the screen to listen for key presses to control snake movement
screen.listen()  # Enables event listening on the screen

# Binding arrow keys to corresponding movement methods in the Snake class
screen.onkey(fun=snake.move_up, key="Up")  # Moves the snake up
screen.onkey(fun=snake.move_right, key="Right")  # Moves the snake right
screen.onkey(fun=snake.move_down, key="Down")  # Moves the snake down
screen.onkey(fun=snake.move_left, key="Left")  # Moves the snake left

# Function to exit the game on screen click
def exit_game(x, y):
    """Closes the game window."""
    screen.bye()  # Closes the game window

# Binds the left mouse button to exit the game
screen.onscreenclick(fun=exit_game, btn=1, add=None)

game_active = True  # Controls the game loop

# Main game loop
while game_active:
    screen.update()  # Manually updating the screen
    sleep(0.1)  # Adding a delay to control the game speed
    snake.move()  # Moving the snake in the current direction

    # Check for collision with the food
    if snake.head.distance(food) < 15:  # If the snake's head is within 15 pixels of the food
        food.refresh()  # Refresh the food's position
        snake.extend_snake()  # Extend the snake's length
        score.increment_score()  # Increase the score

    # Check for collision with the wall
    if (snake.head.xcor() > 350 or snake.head.xcor() < -360 or 
        snake.head.ycor() > 350 or snake.head.ycor() < -350):
        snake.reset()  # Reset the snake
        score.reset()  # Reset the scoreboard

    # Check for collision with the snake's own body
    for segment in snake.segments[1:]:  # Skipping the head segment
        if snake.head.distance(segment) < 10:  # If the head is too close to a body segment
            snake.reset()  # Reset the snake
            score.reset()  # Reset the scoreboard

# Exiting the game when the screen is clicked
screen.exitonclick()  # Keeps the window open until clicked
