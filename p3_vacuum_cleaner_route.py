"""
Given a string representing the sequence of moves a robot vacuum makes,
return whether or not it will return to its original position.
The string will only contain L, R, U, and D characters, representing
left, right, up, and down respectively.

Ex: Given the following strings...

"LR", return True
"URURD", return False
"RUULLDRD", return True
"""


def main():
    """Main Function"""
    moves = input('> ')

    lefts, ups = 0, 0
    for move in moves:
        if move == 'L':
            lefts += 1
        elif move == 'R':
            lefts -= 1
        elif move == 'U':
            ups += 1
        elif move == 'D':
            ups -= 1

    print(ups == lefts == 0)


if __name__ == "__main__":
    main()
