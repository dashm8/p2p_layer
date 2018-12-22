import SocketServer
import threading
from core.encoder import Encoder
from core.logger import Logger

BUFFER_SIZE = 2048

class TcpHandler(SocketServer.BaseRequestHandler):
    """
    basic server templace
    """

    def handle(self):
        raw_data = self.request.recv(BUFFER_SIZE).strip()
        self.data = Encoder.json_encode(raw_data)
        #for tests
        Logger.log_info(self.data)

class ThreadedTcpServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    """
    threaded tcp class
    """
    pass

class TcpServer(object):
    """
    tcp server
    """

    def __init__(self, ip_addr, port):
        """
        inits the server
        """
        self.ip_addr = ip_addr
        self.port = port
        self.server = None

    def run(self):
        """
        start server thread
        """
        self.server = ThreadedTcpServer((self.ip_addr, self.port), TcpHandler)
        server_thread = threading.Thread(target=self.server.serve_forever)
        server_thread.daemon = True
        server_thread.start()



    def shutdown(self):
        """
        shutdown server
        """
        self.server.shutdown()

