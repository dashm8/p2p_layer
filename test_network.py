from network.client import Client
from network.server import TcpServer


IP = "127.0.0.1"
PORT = 4444

def main():
    """
    main test function
    """
    client = Client(IP, PORT)
    server = TcpServer(IP, PORT)
    main_thread = threading.Thread(target=server.run)
    main_thread.start()
    client.send_to_peer(IP, PORT, {"data" : "hello world"})


if __name__ == "__main__":
    main()