import socket
import random
from threading import Thread
from datetime import datetime

# server's IP address
# if the server is not on this machine,
# put the private (network) IP address (e.g 192.168.1.2)
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5002  # server's port
separator_token = "<SEP>"  # we will use this to separate the client name & message
user_token = "<USR>"
# initialize TCP socket
s = socket.socket()
print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
# connect to the server
s.connect((SERVER_HOST, SERVER_PORT))
print("[+] Connected.")


def createUser():
    while True:
        username = input("Username:")
        password = input("Password:")
        if not username or not password:
            print("Enter a valid username and password...")
        users = c.get_all_users()
        Users = open('read.txt', 'w')
        # userList = users['list_users_response']['list_users_result']['users']
        if username in Users:
            print("username already exist")
        else:
            # I just want to create if fields are not empty and if username dont exist
            c.create_user(username)
    createUser()


# prompt the client for a name
# def register():
#    db = open("file.txt", "r")
#   name = input("Enter you name: ")
#    password = input("Enter your password: ")

#    if name in db:
#        print(" the username you entered exists: ")
#        register()
#    else:
#        db = open("file.txt", "a")
#        db.write(name + ", " + password+ "\n")

# register()
name = input("Enter your name: ")
# prompt the client for passwords
Password = input("Enter you password: ")
# SAVE NAME TO ONE MASTER FILE
# SEARCH NAME IF IT EXISTS DON'T CHANGE , IF NOT ADD NAME AND PASSWORD EXISTS

def listen_for_messages():
    while True:
        message = s.recv(1024).decode()
        print("\n\nmessage received\n")
        print("\n" + message)


# make a thread that listens for messages to this client & print them
t = Thread(target=listen_for_messages)

# start the thread
t.start()
while True:
    # input message we want to send to the server
    State = input("enter your operation: PM - private message, DM - direct message, EX - exit")
    if State == 'PM':
        to_send = input()
        to_send = f"{name}{separator_token}{to_send}"
        # finally, send the message
        s.send(to_send.encode())

    elif State == 'DM':

        print("enter desired user: ")
        user = input()

        to_send = input()

        to_send = f"{user} {user_token} {name} {separator_token} {to_send}"
        # finally, send the message
        s.send(to_send.encode())

    # a way to exit the program
    elif State == 'EX':
        break
        message = s.recv(1024).decode()
        print("\n\nmessage received\n")
        print("\n" + message)

# close the socket
s.close()
