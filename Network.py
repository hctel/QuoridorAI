import socket, json


subscribeRequest = "{{\"request\": \"subscribe\",\"port\": {},\"name\": \"Not-A-Virus.exe\",\"matricules\": [\"22054\", \"2217\"]}}"

class Network:
    
    def __init__(self, serverIP, serverPort):
        if not isinstance(serverIP, str) and not isinstance(serverPort, int):
            raise TypeError
            return
        self.__address = (serverIP, serverPort)
        self.__socket = socket.socket()
        self.__socket.connect(self.__address)
        data = subscribeRequest.format(serverPort).encode("utf-8")
        sent = self.__socket.send(data)
        if sent == len(data):
            print("Subscribe string sent")
        
