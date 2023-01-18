from my_project.mock.dice import roll_dice


def guess_number(num):
    result = roll_dice
    if num == result:
        return "You won!"
    else:
        return "You lost!"

