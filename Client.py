import socket
import pickle
from threading import local
from core import Champion, Match
from team_local_tactics import print_available_champs, print_match_summary, input_champion

class Client:

    def __init__(self, PORT) -> None:
        self.SOCKET = socket.socket()
        self.SOCKET.connect(("localhost", PORT))
        print(f"Connected to localhost on port {PORT}")
        self.gameLoop()

    def gameLoop(self):
        while True:
            
            data = self.SOCKET.recv(4098)

            if not data:
                continue

            data = pickle.loads(data)

            if type(data) is dict:
                champs = data
                print_available_champs(champs)
            elif type(data) is tuple:
                chosenChamp = input_champion(f"Player {data[0]}", data[1], champs, data[2], data[3])
                self.SOCKET.send(pickle.dumps(chosenChamp))
            elif type(data) is list:
                print(f"Player 1 team: {data[0]} | Player 2 team: {data[1]}")
            elif type(data) is Match:
                print_match_summary(data)
                break


    def shutdown(self):
        self.SOCKET.close()
        print("Closed connection to server.")

if __name__ == "__main__":
    PORT = 6961
    client = Client(PORT)
