from netmiko import ConnectHandler # adds a pre compiled libary called NetMiko which handles SSH connection to other machines through python, in specific importing the ConnectionHandler
# importing only a certain section of NetMiko ensures a smaller file size as the whole libary is then not imported
# NetMiko is an extension of ParaMiko with a lot more usability

IP = input(str("What IP are you attempting to connect to?"))
USER = input(str("What is the Username of the machine you're attempting to connect to?"))
PASS = input(str("What is the Password of the machine you're attempting to connect to?"))
# Inputs to the parameters needed to establish the connection

NetConnect = ConnectHandler(
                            device_type= autodetect, # The device OS your attempting to connect to
                            host= IP, # is the IP of the Host you're attempting to connect to
                            port= "5679", # is a Host port whereas port 22 is a Guest PORT
                            username= USER, # Change to your username
                            password= PASS, # Change to your password
)


