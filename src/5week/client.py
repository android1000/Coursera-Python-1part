import socket
import time


class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        try:
            self.connection = socket.create_connection((host, port), timeout)
        except socket.error as err:
            raise ClientError

    def put(self, metric_name, metric_value, timestamp=str(int(time.time()))):
        self.connection.sendall(f"put {metric_name} {metric_value} {timestamp}\n".encode("utf8"))
        data = b""
        while not data.endswith(b"\n\n"):
            try:
                data += self.connection.recv(1024)
            except socket.error:
                raise ClientError
        data_decoded = data.decode().split("\n")
        if data_decoded[0] == "error":
            raise ClientError

    def get(self, metric_name):
        self.connection.sendall(f"get {metric_name}\n".encode("utf8"))
        data = b""
        while not data.endswith(b"\n\n"):
            try:
                data += self.connection.recv(1024)
            except socket.error:
                raise ClientError
        data_decoded = data.decode().split("\n")
        if data_decoded[0] == "error":
            raise ClientError
        metric_dict = {}
        for row in data_decoded[1:len(data_decoded) - 2]:
            print(row)
            metric_name, metric_value, timestamp = row.split()
            if metric_name not in metric_dict:
                metric_dict[metric_name] = []
            metric_dict[metric_name] += [(int(timestamp), float(metric_value))]
        return metric_dict


class ClientError(Exception):
    pass
