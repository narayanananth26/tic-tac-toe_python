
l = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
remaining_choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
selected_choices = []
count = 0
corners = [1, 3, 7, 9]
sides = [2, 4, 6, 8]
middle = 5


def board(player, row, col, count):

    if count % 2 == 0:
        l[row][col] = "X"
    else:
        l[row][col] = "O"

    return """        {} |  {}  | {}
       - - - - - - -
        {} |  {}  | {}
       - - - - - - -
        {} |  {}  | {}""".format(l[0][0], l[0][1], l[0][2], l[1][0], l[1][1], l[1][2], l[2][0], l[2][1], l[2][2])


def check_winner(player):

    # checking rows
    for i in range(3):
        win = True
        for j in range(3):
            # print(l[i][j])
            if l[i][j] != player:
                win = False
                # print("not rows")
                break
        if win:
            return win

    # checking columns
    for j in range(3):
        win = True
        for i in range(3):
            # print(l[i][j])
            if l[i][j] != player:
                win = False
                # print("not columns")
                break
        if win:
            return win

    # checking diagonals
    for i in range(3):
        win = True
        if l[i][i] != player:
            win = False
            # print("not straight diagonal")
            break
    if win:
        return win

    for i in range(3):
        win = True
        if l[i][2-i] != player:
            win = False
            # print("not reverse diagonal")
            break
    if win:
        return win

    return False


print("        1 |  2  | 3 ")
print("       - - - - - - -")
print("        4 |  5  | 6 ")
print("       - - - - - - -")
print("        7 |  8  | 9 ")
player = ""

while count < 9:
    choice = int(input("Enter any of the remaining digits (0-9) : ")) - 1

    if (choice + 1) not in remaining_choices:
        print("Enter a valid input!")
        continue

    row = choice // 3
    col = choice % 3
    # print(row, col)

    print(board(player, row, col, count))

    if count >= 4:
        if count % 2 == 0:
            player = "X"
        else:
            player = "O"

        # print(check_winner(l, player), player)
        if check_winner(player):
            print(f"'{player}'wins!")
            break

    selected_choices.append(choice)
    remaining_choices.remove(choice + 1)
    count += 1
    # print(count)
