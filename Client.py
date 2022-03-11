import socket

class Client:

    SOCKET = socket.socket()

    def __init__(self, PORT) -> None:
        self.SOCKET.connect(("localhost", PORT))
        print(f"Connected to localhost on port {PORT}")
        self.gameLoop()

    def gameLoop(self):
        while True:
            msg = self.SOCKET.recv(1024).decode()

            if not msg:
                continue

            match msg.split()[0]:
                case "MESSAGE":
                    print(" ".join(msg.split()[1:]))
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

    def shutdown(self):
        self.SOCKET.close()
        print("Closed connection to server.")

if __name__ == "__main__":
    PORT = 6966
    client = Client(PORT)

