from netmiko import ConnectHandler # adds a pre compiled libary called NetMiko which handles SSH connection to other machines through python, in specific importing the ConnectionHandler
# importing only a certain section of NetMiko ensures a smaller file size as the whole libary is then not imported

NetConnect = ConnectHandler(
device_type= autodetect,
host= IP,
port= "5679" PORT,
username= USER, # Change to your username
password= PASS, # Change to your password
)


