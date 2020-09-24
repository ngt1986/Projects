import socket
from _thread import *
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = '10.0.0.192'
port = 5555

server_ip = socket.gethostbyname(server)

try:
    s.bind((server, port))

except socket.error as e:
    print(str(e))

s.listen(2)
print("Server Started: Waiting for a connection...")

connections = 0

#currentId = "0"


def threaded_client(conn):
    global currentId, connections, player_move

    # if connections == 0:
    #     currentId = "1"
    # else:
    #     currentId = "2"
    # conn.send(str.encode(currentId))
    # connections += 1

    reply = ''
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode('utf-8')
            if not data:
                conn.send(str.encode("Goodbye"))
                break
            else:
                print("Received: " + reply)
                player_move = reply.split(":")
                #player_move[0] is ID : player move[1] is (row,column) : player_move[2] is horiz (0) or vert(1)

                player_id = int(player_move[0])
                player_move[player_id] = reply

                if player_id == 0: player_not_id = 1
                if player_id == 1: player_not_id = 0

                reply = player_move[player_not_id][:]
                print("Sending: " + reply)

            conn.sendall(str.encode(reply))
        except:
            break

    print("Connection Closed")
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn,))