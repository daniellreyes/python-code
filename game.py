import time

'''
Structure in this code is: 
1 -> definition of user_choice
2 -> random choice from compuer
3 -> select winner and return new round
'''
def print_game_options(options):
    print("Select your option game by '1', '2', or '3'\n")
    for key, value in options.items():
        print(f"Option: '{key}' {value}")
    print()

def get_user_choice(options):
    while True:
        try:
            user_option = int(input("Your choice is: "))
            if user_option not in options:
                raise ValueError
            return user_option
        except ValueError:
            print("Please select '1', '2', or '3'\n")

def user_option_game():
    game_options = { 
        1: "crayon 🪨", 
        2: "paper 📄", 
        3: "scissors ✂️"
    }

    print("Hello, this is a 🪨, 📄, or ✂️ game!!\n")
    time.sleep(3)

    print_game_options(game_options)
    user_choice = get_user_choice(game_options)
    print(game_options[user_choice])

# Ejecutar la función principal
user_option_game()