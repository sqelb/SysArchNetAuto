

r, c = 5, 1 # Defining how many rows and columns the array has 
Matrix = [[0 for x in range(r)] for y in range(c)] # Creates a 2D Array
Matrix[0][0] = "Show date and time"
Matrix[0][1] = "Show IP address"
Matrix[0][2] = "Show Remote home directory listing"
Matrix[0][3] = "Backup remote file"
Matrix[0][4] = "Quit"
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

options(i, Matrix, r) # Calling function to print out all the options

mon = True
while mon == True:
    q = int(input("What Option do you pick?\n")) # Getting user input for primary option

    # Based on user input detects all the available primary options and gives the desired output 
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
        print("You have picked an invalid value\n\n") # Error message if no valid input was detected
        options(i, Matrix, r) # Prints options again to remind user of the options
