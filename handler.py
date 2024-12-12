from netmiko import ConnectHandler 
import getpass # Secure way of inputting a password (no terminal feedback)
from netmiko import NetmikoTimeoutException # To detect and handle timeout of the ssh connection
import os
import requests

'''
adds a pre compiled libary called NetMiko which handles
SSH connection to other machines through python, 
in specific importing the ConnectionHandler
'''
'''
importing only a certain section of NetMiko ensures a smaller file size 
as the whole libary is then not imported
'''
# NetMiko is an extension of ParaMiko with a lot more usability

r, c = 6, 1 # Defining how many rows and columns the array has 
Matrix = [[0 for x in range(r)] for y in range(c)] # Creates a 2D Array
Matrix[0][0] = "Show date and time (local)"
Matrix[0][1] = "Show IP address(local)"
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
    for r in Matrix: # for rows in 2D array
        for val in r: # for values detected in a row
            i += 1 # increment I
            print(i, ": ", "{}".format(val)) # prints option number and value of the current row
            # Using formating to output the Option numbers and the options themselves


def picker(NetConnect): # user input made into function which can be called on at anytime
    try: # tries the following code if there are no errors
        while True:
            options(i, Matrix, r) # Calling function to print out all the options
            q = input("What Option do you pick?\n") # Getting user input for primary option
            q = int(q) - 1 # turns user inputinto an iteger decrements the user input for if/else

            # Based on user input detects all the available primary options and gives the desired output 
            if q == 0:
                print("You have picked: ", Matrix[0][q])
                command = "date" 
                os.system(command) # runs the command date on the local terminal
                

            elif q == 1:
                print("You have picked: ", Matrix[0][q])
                command = "ip addr show"
                os.system(command) # runs the command ip addr show on the local terminal
                

            elif q == 2:
                print("You have picked: ", Matrix[0][q])
                command = "ls ~/"
                print(NetConnect.send_command(command)) # runs command in ssh
                

            elif q == 3:
                print("You have picked: ", Matrix[0][q])
                path = input("What Directory do you wish to copy from? ")
                file = input("What file do you wish to copy? ")
                command = "cp ~/{}/{} ~/{}/{}.old".format(path, file, path, file)
                print(NetConnect.send_command(command)) # copies a user inputted file in ssh
                '''
                path and file variables both use user input to establish the path the command will follow 
                and what file to execute this on
                '''
                print("\nFile copied\n")
                

            elif q == 4:
                print("You have picked: ", Matrix[0][q])
                UserUrl = input("What URL would you like to save?\ne.g. http(s)://www.google.com\n") # will be passed to be saved
                url = requests.get(UserUrl) # The webpage get coppied
                FileName = "{}.html".format(UserUrl) # Made into a HTML file so it can be accessed at anytime
                file = open(FileName, "x") # file to store the webpage is created in the same directory as this program
                file = open(FileName, "w") # file to write in is open
                file.write(url.text) # writing the source code of the webpage in
                file.close # closes the file
                print("Webpage saved\n")
                
    
            elif q == 5:
                print("You have picked: ", Matrix[0][q])
                break

            else:
                print("You have picked an invalid value\n\n") # Error message if no valid input was detected
    
            '''
            Command variable stores the command for each option and then passes 
            through to be executed depending on user input
            '''
    except: # catches the error rather than crashing and exitting the program
        print("You have picked an invalid value\n\n") 
        #prints error message if there were no valid input

        picker(NetConnect) 
        '''
        Calls on the user options function to allow the user to see and pick options again 
        if there was an error
        '''

def connector():
    try: # Tries this code first
        IP = input(str("What IP are you attempting to connect to? "))
        USER = input(str("What is the Username of the machine you're attempting to connect to? "))
        PASS = getpass.getpass("What is the Password of the machine you're attempting to connect to? ")
        # Inputs to the parameters needed to establish the connection

        NetConnect = ConnectHandler(
                                    device_type= "autodetect", # The device OS your attempting to connect to
                                    host= IP, # is the IP of the Host you're attempting to connect to
                                    port= "5679", # is a Host port whereas port 22 is a Guest PORT
                                    username= USER, # Change to your username
                                    password= PASS, # Change to your password
                                )
        

        print("\n\nYou have connected to {}@{}\n\n".format(
                                                      NetConnect.username, 
                                                      NetConnect.host
                                                          )
             )
        return NetConnect

    except NetmikoTimeoutException: # An error catcher which stops the command/connection being made indefinetly 
        print("\nConnection time out.\n")
        connector()
    except Exception as Error: # Catches all the other errors that do not fall under timeout
        print("\nError:{}\n".format(Error))
        connector()


NetConnect = connector() # place the connector file into the main file for ease of coding and ease of access
picker(NetConnect) # initialise picker after connector as a ssh connection to the machine needs to be made
