

r, c = 5, 1 # Defining how many rowsand columns the array has 
Matrix = [[0 for x in range(r)] for y in range(c)]
Matrix[0][0] = "Play a game"
Matrix[0][1] = "Add some numbers"
Matrix[0][2] = "Solve some numbers"
Matrix[0][3] = "Rename a file"
Matrix[0][4] = "Quit"
i = 0

def options(i, Matrix, r):
    for r in Matrix:
        for val in r:
            i += 1
            print(i, ": ", "{}".format(val))

options(i, Matrix, r)

mon = True
while mon == True:
    q = int(input("What Option do you pick?\n"))

    if q == 1:
        print("You have picked: ", Matrix[0][q])
        mon = False
    elif q == 2:
        print("You have picked: ", Matrix[0][q])
        mon = False
    elif q == 3:
        print("You have picked: ", Matrix[0][q])
        mon = False
    elif q == 4:
        print("You have picked: ", Matrix[0][q])
        mon = False
    elif q == 4:
        print("You have picked: ", Matrix[0][q])
        mon = False
    else:
        print("You have picked an invalid value\n\n")
        options(i, Matrix, r)
