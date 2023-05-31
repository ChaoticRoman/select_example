import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()

# Choose a port that matches the server
port = 50000

# Connection to the server
client_socket.connect(('localhost', port))

# Send a message to the server
message = "Hello, server!"
client_socket.send(message.encode('ascii'))

# Receive the server's response
response = client_socket.recv(1024)

print('Received from server: ', response.decode('ascii'))

# Close the connection
client_socket.close()
