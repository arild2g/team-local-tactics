from logging import shutdown
import pickle
import socket
from DatabaseService import createConnection, selectAllChamps, saveMatchToDatabase
from core import Match 

class DatabaseServer:
    def __init__(self, PORT) -> None:
        self.SOCKET = socket.socket()
        self.connection = 0

        print("Socket created successfully")

        self.SOCKET.bind(("localhost", PORT))
        print(f"Socket bound to localhost with port {PORT}")

        print("Database Server running...")

        self.SOCKET.listen()
        print("Waiting for connections...")

        self.DBconn = createConnection("TNTDatabase")

        self.connectionLoop()
        
    def connectionLoop(self):
        while True:
            # Accept connection
            self.connection, addr = self.SOCKET.accept()
            print(f"Got connection from {addr}")
            # Send champions to Server.
            self.connection.send(pickle.dumps(selectAllChamps(self.DBconn)))
            break
        while True:
            data = self.connection.recv(4098)
            
            if not data:
                continue
            
            data = pickle.loads(data)

            if type(data) is Match:
                saveMatchToDatabase(self.DBconn, data)

            break
        self.shutdown()


    def shutdown(self):
        self.SOCKET.close()
        print("Server shutting down")


if __name__ == "__main__":
    PORT = 6960
    database = DatabaseServer(PORT)


