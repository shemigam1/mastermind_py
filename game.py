import random

COLORS = ["R", "O", "Y", "G", "B", "I"]
TRIES = 10
CODE_LENGTH = 4

# generate random code
def gen_code():
    code = []

    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)

    return code

def guess_code():
    while True:
        guess = input("Guess the code... ").upper().split(" ")

        if len(guess) != CODE_LENGTH:
            print("Guess length must be equal to {}".format(CODE_LENGTH))
            continue

        for color in guess:
            if color not in COLORS:
                print("Invalid color: {}... Try again".format(color))
                break

        else:
            break

    return guess

def check_code(guess, real_code):
    color_counts = {}
    correct_position = 0
    incorrect_position = 0

    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_position += 1
            color_counts[guess_color] -= 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_position += 1
            color_counts[guess_color] -= 1

    return correct_position, incorrect_position

def game():
    print("Welcome to mastermind, you have {} tries to guess the code".format(TRIES))
    print("PS: always add a space inbetween your colors eg. R O G B")
    print("The valid colors are", *COLORS)
    code = gen_code()
    for tries in range(1, TRIES + 1):
        guess = guess_code()
        print("You have {} tries remaining".format(TRIES - tries ))
        correct_position, incorrect_position = check_code(guess, code)

        if correct_position == CODE_LENGTH:
            print("You guessed the code in {} tries".format(tries))
            break

        print("correct positions: {} | incorrect positions: {}".format(correct_position, incorrect_position))

    else:
        print("you ran out of tries, the code was:", *code)

if __name__ == "__main__":
    game()