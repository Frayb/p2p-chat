import socket
from threading import Thread

# server's IP address
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5002 # port we want to use
separator_token = "<SEP>" # we will use this to separate the client name & message
user_token = "<USR>"
# initialize list/set of all connected client's sockets
client_sockets = set()
# create a TCP socket
s = socket.socket()
# make the port as reusable port
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# bind the socket to the address we specified
s.bind((SERVER_HOST, SERVER_PORT))
# listen for upcoming connections
s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

def listen_for_client(cs):
    """
    This function keep listening for a message from `cs` socket
    Whenever a message is received, broadcast it to all other connected clients
    """
    while True:
        info_array = {}
        # determine user making the connection upon initial connection
        try:
            # keep listening for a message from `cs` socket
            msg = cs.recv(1024).decode()
        except Exception as e:
            # client no longer connected
            # remove it from the set
            print(f"[!] Error: {e}")
            client_sockets.remove(cs)
        else:
            # if we received a message, replace the <SEP>
            # token with ": " for nice printing
            print("Message was sent")

            if user_token in msg:
                target_user = ""
                message1 = ""
                info_array = msg.split()
                #iterate through array and look

                for i in info_array:
                    if not user_token:
                        target_user += i
                    else:
                        message1 += i

                message1 = message1.replace(user_token, "")
                message1 = message1.replace(separator_token, ":")

                #iterate through clients to find correct socket
                #if client not found return error

            else:
                msg = msg.replace(separator_token, ": ")

                # if PM do the following
                # iterate over all connected sockets
                for client_socket in client_sockets:
                    # and send the message
                    client_socket.send(msg.encode())

        #else if DM search for specific socket

#def list_all_clients(client):
#    #identify each client
#    for client in client_sockets:
#        print("\nclient is: \n")
#        print(client.client_address)


while True:
    # we keep listening for new connections all the time
    client_socket, client_address = s.accept()

    #identify client originating message
    #separate class that inherits the treading


    print(f"[+] {client_address} connected.")
    # add the new connected client to connected sockets
    client_sockets.add(client_socket)
    # start a new thread that listens for each client's messages
    t = Thread(target=listen_for_client, args=(client_socket,))
    # make the thread daemon so it ends whenever the main thread ends
    t.daemon = True
    # start the thread
    t.start()
    # close client sockets
for cs in client_sockets:
    cs.close()
# close server socket
s.close()
