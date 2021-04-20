import socket

import gzip
from io import BytesIO
'''
We can potentially chain the decorators to achieve much cleaner Multiple Inheritance.

Decorator vs Inheritance:
When faced with a choice between decorators and inheritance, we should only use decorators if we need to modify the object dynamically, according to some condition. For e.g. here we can switch between LogSocket and normal socket based on whether debugging mode is on for server. Similarly we can switch between LogSocket and GzipSocket based on a config.
'''

# Gzip Decorator
class GzipSocket:
    def __init__(self, socket):
        self.socket = socket

    def send(self, data):
        buf = BytesIO()
        zipfile = gzip.GzipFile(fileobj=buf, mode="w")
        zipfile.write(data)
        zipfile.close()
        self.socket.send(buf.getvalue())

    def close(self):
        self.socket.close()

# Logging Decorator - via composition
class LogSocket:
    def __init__(self, socket):
        self.socket = socket

    def send(self, data):
        print(
            "Sending {0} to {1}".format(
                data, self.socket.getpeername()[0]
            )
        )
        self.socket.send(data)

    def close(self):
        self.socket.close()

def respond(client):
    response = input("Enter a value: ")
    client.send(bytes(response, "utf8"))
    client.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 2403))
server.listen(1)
try:
    while True:
        client, addr = server.accept()
        # respond(client)- basic socket without decorator
        # respond(LogSocket(client))
        respond(GzipSocket(client))
finally:
    server.close()