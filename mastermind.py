import random

correct_digits_and_position = 0
correct_digits_only = 0
correct = False


def create_code():
    """Function that creates the 4 digit code, using random digits from 1 to 8"""

    code = [0, 0, 0, 0]

    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value
    
    return code


def show_instructions():
    """Shows instructions to the user"""

    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')


def show_results(numbers):
    """Show the results from one turn"""

    print('Number of correct digits in correct place:     ' + str(numbers[0]))
    print('Number of correct digits not in correct place: ' + str(numbers[1]))


def take_turn(code):
    """Handle the logic of taking a turn, which includes:
       * get answer from user
       * check if answer is valid
       * check correctness of answer
    """
    correct_numbers = (0, 0)
    correct_list = list(correct_numbers)
    answer = get_answer_input()

    correct_digits_and_position = 0
    correct_digits_only = 0
    for i in range(len(answer)):
        if code[i] == int(answer[i]):
            correct_digits_and_position += 1
        elif int(answer[i]) in code:
            correct_digits_only += 1
    correct_list[0] = correct_digits_and_position
    correct_list[1] = correct_digits_only
    correct_numbers = tuple(correct_list)
    show_results(correct_numbers)
    return correct_numbers

def get_answer_input():

    """
    Retrieves an imput from the user
    
    Checks that the length of code is anything but 4
    Asks again if the length is not 4
    """

    answer = input("Input 4 digit code: ")
    while len(answer) < 4 or len(answer) > 4:
        print("Please enter exactly 4 digits.")
        answer = input("Input 4 digit code: ")
    return answer

def show_code(code):
    """Show Code that was created to user"""

    print('The code was: '+str(code))


def check_correctness(turns, correct_numbers):
    """Checks correctness of answer and show output to user"""
    if correct_numbers == 4:
        print('Congratulations! You are a codebreaker!')
        return True
    else:
        print('Turns left: ' + str(12 - turns))
        return False


def run_game():
    """Main function for running the game"""
    correct = False
    code = create_code()
    show_instructions()

    turns = 0
    while not correct and turns < 12:
        correct_digits = take_turn(code)
        turns += 1
        correct = check_correctness(turns, correct_digits[0])

    show_code(code)


if __name__ == "__main__":
    run_game()
