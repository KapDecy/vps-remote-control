import pickle
import socket
import os
import threading


def stop():
    global stopped
    input()
    stopped = True


class ServerThread(threading.Thread):
    def __init__(self, sock, ip):
        self.sock = sock
        self.ip = ip
        threading.Thread.__init__(self)

    def run(self):
        print("Received connection:", self.ip[0])
        # request = pickle.loads(self.sock.recv(1024))
        # if request == "exit":
        #     self.sock.send(pickle.dumps("stoped"))
        #     self.sock.close()
        #     print("Closed connection:", self.ip[0])
        #     os._exit(0)
        # else:
        #     print(request)
        #     self.sock.send(pickle.dumps("done"))
        self.sock.close()
        print("Closed connection:", self.ip[0])


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("192.168.3.27", 9000))
server.listen(0)


def start_server():
    global stopped
    global server
    while not stopped:
        sock, ip = server.accept()
        ServerThread(sock, ip).start()


stopped = False
threading.Thread(target=start_server, daemon=True).start()
stop()
