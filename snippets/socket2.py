import socket
import sys

HOST, PORT = None, 6048
data = " ".join(sys.argv[1:])
# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dict1 = dict()
while 1:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    lst = list()
    sock.sendall(bytes(data + "\n", "utf-8"))
    lst = data.strip()

    if lst[0] is 'set':
        key = lst[1]
        dict1[key] = lst[2]
    elif lst[0] is 'get':
        if lst[1] in dict1:
            print(dict1[lst[1]])

    # Receive data from the server and shut down
    received = str(sock.recv(1024), "utf-8")
    sock.close()
