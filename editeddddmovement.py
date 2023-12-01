import random

def print_maze(player_pos, maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if (row, col) == player_pos:
                print("@", end=" ")
            elif maze[row][col] == 1:
                print("#", end=" ")
            elif (row, col) == (len(maze) - 1, len(maze[0]) - 1):  # Check if it's the exit
                print("✩", end=" ")
            else:
                print(".", end=" ")
        print()

maps = [
    [[0, 0, 1, 1, 1, 1, 1, 1, 1],
     [1, 0, 0, 0, 1, 0, 1, 0, 1],
     [1, 1, 0, 0, 1, 1, 1, 1, 1],
     [1, 0, 1, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 1, 0, 1, 0, 0, 1],
     [1, 1, 1, 1, 1, 0, 0, 1, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 1, 0, 1, 0, 0, 0, 0, 0],
     [1, 1, 1, 1, 1, 1, 1, 1, 0]],

    [[0, 0, 1, 1, 1, 1, 1, 1, 1],
     [1, 0, 1, 1, 1, 1, 1, 1, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 1, 0, 1, 0, 1, 0, 1, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 1, 1, 0, 1, 1, 0, 1],
     [1, 0, 1, 0, 0, 0, 0, 0, 1],
     [1, 0, 1, 1, 0, 0, 0, 0, 0],
     [1, 1, 1, 1, 1, 1, 1, 1, 0]],
]

    # Add three more maps here...

def generate_maze():
    return random.choice(maps)

def move_player(player_pos, move_key, maze_size):
    row, col = player_pos
    if move_key == "w" and row > 0:
        row -= 1
    elif move_key == "s" and row < maze_size - 1:
        row += 1
    elif move_key == "a" and col > 0:
        col -= 1
    elif move_key == "d" and col < maze_size - 1:
        col += 1
    return row, col

def start_interface():
    print("""
888    d8P                    888                                     888       888       888                          d8b                  
888   d8P                     888                                     888       888   o   888                          Y8P                  
888  d8P                      888                                     888       888  d8b  888                                               
888d88K      .d88b.  888  888 88888b.   .d88b.   8888b.  888d888  .d88888       888 d888b 888  8888b.  888d888 888d888 888  .d88b.  888d888 
8888888b    d8P  Y8b 888  888 888 "88b d88""88b     "88b 888P"   d88" 888       888d88888b888     "88b 888P"   888P"   888 d88""88b 888P"   
888  Y88b   88888888 888  888 888  888 888  888 .d888888 888     888  888       88888P Y88888 .d888888 888     888     888 888  888 888     
888   Y88b  Y8b.     Y88b 888 888 d88P Y88..88P 888  888 888     Y88b 888       8888P   Y8888 888  888 888     888     888 Y88..88P 888     
888    Y88b  "Y8888   "Y88888 88888P"   "Y88P"  "Y888888 888      "Y88888       888P     Y888 "Y888888 888     888     888  "Y88P"  888     
                          888                                                                                                               
                     Y8b d88P                                                                                                               
                      "Y88P"                                                                                                                                                                                                                             
""")
    print("1. Start Game")
    print("2. Credits")
    print("3. Exit")


    choice = input("Select an option (1/2/3): ")

    if choice == "1":
        start_game()
    elif choice == "2":
        print("""\nGame created by 404 Gatekeepers:
        Jron Corpuz
        Yasmien Gayao
        Gerryle Martinez
        Adrian Rivera""")
        # start_interface()
    elif choice == "3":
        print("\nExiting the game. Goodbye!")
    else:
        print("\nInvalid choice. Please select a valid option.")
        start_interface()

def start_game():
    player_name = input("Enter your name: ").strip()

    while not player_name:
        print("Name cannot be blank. Please enter your name.")
        player_name = input("Enter your name: ").strip()

    print(f"\nHello, {player_name}! Let's start the game.")
    print(f"""With your passion for the legend of the keyboard, you venture to the desert to acquire the lost remaining symbol relics that will complete the keyboard. The symbols !,$,&,* and ~.

Your companion, Jebrael, helped you to get to the location because only you, {player_name}, were the last person in your bloodline who has the capabilities to take hold of them and place them to the right location.

On the last leg, you finally acquire the “~” symbol. However the whole place started shaking.""")

    global maze
    maze = generate_maze()
    global maze_size
    maze_size = len(maze)

    player_pos = (0, 0)

    while True:
        print_maze(player_pos, maze)
        move_key = input("Enter a move key (W/A/S/D) or 'exit' to quit: ").lower()

        if move_key == "exit":
            print("\nThanks for playing! Exiting the game.")
            break

        new_pos = move_player(player_pos, move_key, maze_size)
        if maze[new_pos[0]][new_pos[1]] == 0:
            player_pos = new_pos
        else:
            print("Oops! You can't move there. Try again.")

        if player_pos == (maze_size - 1, maze_size - 1):
            print("\nCongratulations ! You reached the exit. Game over.")
            break

if __name__ == "__main__":
    start_interface()