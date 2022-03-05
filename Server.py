from multiprocessing import connection
import socket

class Server:
    SOCKET = socket.socket()
    connections = []

    def __init__(self, PORT) -> None:    
        print("Socket created succsessfully")
        self.SOCKET.bind(("localhost", PORT))
        print(f"Socket binded to localhost with port {PORT}")

        self.SOCKET.listen()
        print("Waiting for connections...")
        self.connectionLoop()

    # Connection loop
    def connectionLoop(self):
        while True:
            # Accept connection
            con, addr = self.SOCKET.accept()
            self.connections.append(con)
            print(f"Got connection from {addr}")

            # Check connection state
            match len(self.connections):
                case 1:
                    self.connections[0].send("MESSAGE Waiting for another player to join.".encode())
                case 2:
                    print("All players connected starting game.")
                    break

        self.gameLoop()
            
    # Gameloop
    def gameLoop(self):
        while True:
            pass
            #TODO Create gameloop on server

        self.shutdown()

    def sendToAllClients(self, msg):
        for con in self.connections:
            con.send(msg.encode())
            print(f"Sent message: {msg} to connection: {con.getsockname()}")

    def shutdown(self):
        self.SOCKET.close()
        print("Server shutting down")
    

if __name__ == "__main__":
    
    PORT = 6966
    
    client = Server(PORT)
    
