

r, c = 6, 1 # Defining how many rows and columns the array has 
Matrix = [[0 for x in range(r)] for y in range(c)] # Creates a 2D Array
Matrix[0][0] = "Show date and time"
Matrix[0][1] = "Show IP address"
Matrix[0][2] = "Show Remote home directory listing"
Matrix[0][3] = "Backup remote file"
Matrix[0][4] = "Save web page"
Matrix[0][5] = "Quit"
'''
 All the options available for the user, once an option has been 
 selected by the user the code for it would be executed.
'''
'''
Options will be split into primary and secondary options, 
most primary options will have a secondary option
'''

i = 0 # Variable created to be able to be incremented to then be able to list all the Primary options

def options(i, Matrix, r): # Function created to output all the primary options once called on
    for r in Matrix:
        for val in r:
            i += 1
            print(i, ": ", "{}".format(val)) 
            # Using formating to output the Option numbers and the options themselves



while True:
    options(i, Matrix, r) # Calling function to print out all the options
    q = int(input("What Option do you pick?\n")) # Getting user input for primary option
    q -= q

    # Based on user input detects all the available primary options and gives the desired output 
    if q == 0:
        print("You have picked: ", Matrix[0][q])
        command = "date"
        break

    elif q == 1:
        print("You have picked: ", Matrix[0][q])
        command = "ip addr show"
        break

    elif q == 2:
        print("You have picked: ", Matrix[0][q])
        command = "ls ~/"
        break

    elif q == 3:
        print("You have picked: ", Matrix[0][q])
        path = input("What Directory do you wish to copy from?\n~/")
        file = input("What file do you wish to copy? ")
        command = "cp ~/{path}{file} ~/{path}{file}".format()
        break

    elif q == 4:
        print("You have picked: ", Matrix[0][q])

        break

    else:
        print("You have picked an invalid value\n\n") # Error message if no valid input was detected
        
