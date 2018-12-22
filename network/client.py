import socket
from core.logger import Logger
from core.encoder import Encoder

class Client(object):
    """
    the client class
    """
    def __init__(self, ip_addr, port):
        self.ip_addr = ip_addr
        self.port = port

    def make_header(self, packet, data):
        """
        makes this layar header
        """
        header = {"network":data}
        packet.update(header)
        return packet

    @staticmethod
    def connect(ip_addr, port):
        """
        connect to a peer
        """
        sock = socket.socket()
        try:
            sock.connect((ip_addr, port))
        except socket.error:
            Logger.log_error("cannot connect to peer")
        return sock

    def send(self, sock, msg):
        """
        sends data to peer from socket
        """
        try:
            peer_ip, peer_port = sock.getpeername()
            to_send = {"peer_ip":peer_ip, "peer_port":peer_port,
                       "ip":self.ip_addr, "port":self.port}

            data = self.make_header(msg, to_send)
            data = Encoder.json_decode(data)
            sock.send(data)
        except socket.error:
            Logger.log_error("cant send to peer")

    def send_to_peer(self, ip_addr, port, msg):
        """
        send data to peer wraped as one function
        """
        connection_socket = Client.connect(ip_addr, port)
        self.send(connection_socket, msg)
