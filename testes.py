import sys
import time
import random

# Define mazes outside the functions
Maze1 = """  
   ████████████████████████████
      █                 █     █
█  ████  █████████████  █  ████
█  █        █  █  █     █     █
█  █  ███████  █  ████  ████  █
█           █        █        █
████  █  ████  ████  ███████  █
█     █     █  █  █  █        █
█  ████  ████  █  █  █  █  ████
█  █  █        █     █  █  █  █
█  █  ███████  ██████████  █  █
█        █  █     █     █     █
█  █  ████  ████  █  ███████  █
█  █     █           █  █     █
█  █████████████  ████  ████  █
█              █        █  █  █
███████  ████  ████  ████  ████
█        █  █  █  █  █  █  █  █
█  ███████  █  █  █  █  █  █  █
█     █           █           
█████████████████████████████  """

# Add more mazes if needed
# Maze2 = """
# ... (similar format as Maze1)
# """

def start_game():
    print("Welcome to the Maze Escape Game!")
    player_name = input("Enter your username: ")
    input("Press Enter to begin...")
    print(f"""With your passion for the legend of the keyboard, you venture to the desert to acquire the lost remaining symbol relics that will complete the keyboard. The symbols !,$,&,* and ~.

Your companion, Jebrael, helped you to get to the location because only you, {player_name}, were the last person in your bloodline who has the capabilities to take hold of them and place them to the right location.

On the last leg, you finally acquire the “~” symbol. However, the whole place started shaking.""")

    simulate_maze_escape()

def credits():
    print("""Game created by:
Gerryle Martinez
Yasmien Gayao
Adrian Rivera
Ivan Corpuz""")

def simulate_maze_escape():
    print("Simulating maze escape...")
    time.sleep(2)

    # Use the global keyword to access the globally defined Maze1
    global rand_maze
    rand_maze = random.choice([Maze1])

    # Add player position
    player_position = [1, 1]

    while True:
        print(rand_maze)
        print("\n1. Move Up")
        print("2. Move Down")
        print("3. Move Left")
        print("4. Move Right")
        print("5. Quit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1" and player_position[0] > 1:
            if rand_maze[player_position[0] - 2][player_position[1]] == ' ':
                player_position[0] -= 1
        elif choice == "2" and player_position[0] < len(rand_maze) - 2:
            if rand_maze[player_position[0] + 2][player_position[1]] == ' ':
                player_position[0] += 1
        elif choice == "3" and player_position[1] > 1:
            if rand_maze[player_position[0]][player_position[1] - 2] == ' ':
                player_position[1] -= 1
        elif choice == "4" and player_position[1] < len(rand_maze[0]) - 2:
            if rand_maze[player_position[0]][player_position[1] + 2] == ' ':
                player_position[1] += 1
        elif choice == "5":
            print("Thanks for playing. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

        if player_position == [18, 28]:  # Adjust these coordinates based on the exit position
            print("Congratulations! You have escaped the maze.")
            sys.exit()

# Use a single randomly chosen maze for simplicity
rand_maze = random.choice([Maze1])

def press_button():
    print("\n1. Start Game")
    print("2. Credits")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        start_game()
    elif choice == "2":
        credits()
    elif choice == "3":
        print("Thanks for playing. Goodbye!")
        sys.exit()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

input("Press enter...")
press_button()