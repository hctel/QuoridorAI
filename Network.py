import socket, json, time


subscribeRequest = "{{\"request\": \"subscribe\",\"port\": {},\"name\": \"Not-A-Virus.exe\",\"matricules\": [\"22054\", \"2217\"]}}"

class Network:
    
    def __init__(self, serverIP, serverPort):
        if not isinstance(serverIP, str) and not isinstance(serverPort, int):
            raise TypeError
            return
        self.__address = (serverIP, serverPort)
        self.__socket = socket.socket()
        self.__socket.connect(self.__address)
        data = subscribeRequest.format(serverPort).encode("utf8")
        sentBytes = 0
        while sentBytes == len(data):
            sent = self.__socket.send(data[sentBytes:])
            sentBytes+=sent
        chunks = []
        finished = False
        while not finished:
            data = self.__socket.recv(1024)
            chunks.append(data)
            finished = data == ''
        print(''.join(chunks).decode())
        
network = Network("127.0.0.1", 3000)