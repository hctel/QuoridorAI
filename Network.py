import socket, json
from json.decoder import JSONDecodeError


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
        while sentBytes < len(data):
            sent = self.__socket.send(data[sentBytes:])
            sentBytes+=sent
        chunks = []
        finished = False
        while not finished:
            data = self.__socket.recv(1024)
            chunks.append(data)
            finished = data == b''
        try:
            subResp = json.loads(b''.join(chunks).decode())
            if subResp["response"] == "ok":
                self.__subscribed = True
            else:
                self.__subscribed = False
                errorCode = subResp["error"]
                print(f"Couldn't subscribe with the GameManager: {errorCode}")
        except JSONDecodeError:
            print("Received subscribe response not a JSON string")
        self.__socket.close()
        
        
    @property
    def isSubscribed(self):
        return self.__subscribed
        
network = Network("localhost", 3000)
print(network.isSubscribed)