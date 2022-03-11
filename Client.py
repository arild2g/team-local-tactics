import socket
import pickle
from threading import local
from core import Champion
from team_local_tactics import print_available_champs, print_match_summary

class Client:

    def __init__(self, PORT) -> None:
        self.SOCKET = socket.socket()
        self.SOCKET.connect(("localhost", PORT))
        print(f"Connected to localhost on port {PORT}")
        self.gameLoop()

    def gameLoop(self):
        print('Starting game loop')
        while True:
            data = self.SOCKET.recv(2048)

            if data is None:
                continue

            data_arr = pickle.loads(data)

            print(data_arr)

    def shutdown(self):
        self.SOCKET.close()
        print("Closed connection to server.")

if __name__ == "__main__":
    PORT = 6966
    client = Client(PORT)

"""

            if type(champs) is dict[Champion]:
                print_available_champs(champs)
                continue

            data.decode()

            match data.split()[0]:
                case "MESSAGE":
                    print(" ".join(data.split()[1:]))
                case "CHOOSECHAMPION":
                    print("Recieved CHOOSECHAMPION command.")
                    #TODO Print and choose a champion send back to server
                case "MATCHRESULT":
                    print("Recieved Match Result")
                    #TODO Do print matchresult
                    self.shutdown()
                    break
                case _ :
                    continue
"""

