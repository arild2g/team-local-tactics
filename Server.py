from copyreg import pickle
from multiprocessing import connection
import socket
import pickle
from DatabaseService import selectAllChamps, createConnection, saveMatchToDatabase
from core import Match, Team, Champion

class Server:

    def __init__(self, PORT) -> None:    
        self.connections = []
        self.player1 = []
        self.player2 = []

        self.SOCKET = socket.socket()
        print("Socket created successfully")

        self.SOCKET.bind(("localhost", PORT))
        print(f"Socket bound to localhost with port {PORT}")

        self.SOCKET.listen()
        print("Waiting for connections...")

        self.DBSocket = socket.socket()
        self.DBSocket.connect(("localhost", 6960))
        data = self.DBSocket.recv(4098)
        data = pickle.loads(data)
        self.champDict = data
        print("Recieved champions from database")

        self.connectionLoop()

    # Connection loop
    def connectionLoop(self):
        while True:

            # Accept connection
            con, addr = self.SOCKET.accept()
            self.connections.append(con)
            print(f"Got connection from {addr}")

            # Check connection state
            if len(self.connections) == 2:
                print("All players connected, starting game.")
                self.gameLoop()
                break    
            
    # Gameloop
    def gameLoop(self):
        while True:

            #Display available champions from database
            self.sendToAllClients(self.champDict)

            #Ask each player to choose champions for their teams
            for _ in range(2):
                self.askForTeam(1)
                self.askForTeam(2)

            #Display teams
            self.sendToAllClients([self.player1, self.player2])

            #Create a new match with chosen teams
            match = Match(
                Team([self.champDict[champ] for champ in self.player1]),
                Team([self.champDict[champ] for champ in self.player2])
            )

            #Simulate a match of Team Network Tactics
            match.play()

            #Display match result
            self.sendToAllClients(match)
            
            #Store match history in database
            self.DBSocket.send(pickle.dumps(match))

            break
        self.shutdown()

    def askForTeam(self, nr):
        if nr == 1:
            choosing = 0
            send = 1
            color = "blue"
        else:
            choosing = 1
            send = 0
            color = "red"

        self.sendToClient(self.connections[choosing], (nr, color, self.player1, self.player2))

        while True:
            champ = self.connections[choosing].recv(4098)

            if not champ:
                continue

            champ = pickle.loads(champ)

            if nr == 1:
                self.player1.append(champ)
            else:
                self.player2.append(champ)
            break

    def sendToClient(self, conn, msg):
        conn.send(pickle.dumps(msg))

    def sendToAllClients(self, msg):
        for con in self.connections:
            con.send(pickle.dumps(msg))

    def shutdown(self):
        self.SOCKET.close()
        self.DBSocket.close()
        print("Server shutting down")

if __name__ == "__main__":
    PORT = 6961
    client = Server(PORT)
    
