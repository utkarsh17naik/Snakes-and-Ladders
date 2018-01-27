import random


def dice():
    small = 1
    large = 6

    result = random.randint(small, large)
    return result


def snakes(p):
    snake = {
        17: 7,
        87: 24,
        95: 75,
        62: 19,
        54: 35,
        93: 74,
        98: 60
    }
    return snake[p]


def ladders(p):
    ladder = {
        4: 14,
        9: 31,
        28: 84,
        51: 67,
        80: 97,
        71: 91,
        21: 42
    }
    return ladder[p]


choice = input("Are you ready to play? Press Y or N")
flag = 0
p1 = 1
p2 = 1
maximum = 100
while p1 < maximum or p2 < maximum:
    while choice == 'Y' or choice == 'y':
        if flag == 0:
            print("Player 1's turn")
            print("Rolling the dice")
            res = dice()
            print("The value is: ", res)
            if p1 + res <= 100:
                p1 = p1 + res
                print("Player 1's new position is: ", p1)
                if p1 == 4 or p1 == 9 or p1 == 28 or p1 == 51 or p1 == 80 or p1 == 71 or p1 == 21:
                    print("Wow! You got a ladder")
                    p1 = ladders(p1)
                    print("Player 1's new position is: ", p1)
                elif p1 == 17 or p1 == 87 or p1 == 95 or p1 == 62 or p1 == 54 or p1 == 93 or p1 == 98:
                    print("Oops!! You got swallowed by a snake")
                    p1 = snakes(p1)
                    print("Player 1's new position is: ", p1)
            if res == 6:
                print("Play again")
            else:
                flag = 1
            if p1 == 100:
                print("Player 1 is the winner")

        else:
            print("Player 2's turn")
            print("Rolling the dice")
            res = dice()
            print("The value is: ", res)
            if p2 + res <= 100:
                p2 = p2 + res
                print("Player 2's new position is: ", p2)
                if p2 == 4 or p2 == 9 or p2 == 28 or p2 == 51 or p2 == 80 or p2 == 71 or p2 == 21:
                    print("Wow! You got a ladder")
                    p2 = ladders(p2)
                    print("Player 2's new position is: ", p2)
                elif p2 == 17 or p2 == 87 or p2 == 95 or p2 == 62 or p2 == 54 or p2 == 93 or p2 == 98:
                    print("Oops!! You got swallowed by a snake")
                    p2 = snakes(p2)
                    print("Player 2's new position is: ", p2)
            if p2 == 100:
                print("Player 2 is the winner")
            if res == 6:
                print("Play again")
            else:
                flag = 0
        if p1 == 100 or p2 == 100:
            print("Thanks for playing")
            choice = 'N'
        else:
            choice = input("Do you want to continue? Press Y or N\n")









