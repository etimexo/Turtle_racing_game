import turtle
import time
WIDTH, HEIGHT = 500, 500

# screen.Sleep(10)
def get_turtles():
    racers = 0
    while True:
        racers = input("Input number of turtles (2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input a valid number")
            continue
        
        if 2 <= racers <= 10:
            return racers
        else:
            print("Input must be in range 2 - 10")

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!")
    
racers = get_turtles()
init_turtle()
racer = turtle.Turtle()
racer.speed(1)
racer.forward(100)
time.sleep(10)