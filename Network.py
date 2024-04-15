import socket, json, threading, time
from json.decoder import JSONDecodeError


subscribeRequest = "{{\"request\": \"subscribe\",\"port\": {},\"name\": \"{}\",\"matricules\": [\"22054\", \"2217\"]}}"

class Network:
    
    def __readjson(self, sct):
        chunks = []
        finished = False
        while not finished:
            data = sct.recv(2048)
            chunks.append(data)
            jt = b''.join(chunks).decode()
            try:
                json.loads(jt)
                finished = True
            except JSONDecodeError:
                pass
        return chunks
    
    def send(self, socket, toSend):
        data = toSend.encode("utf8")
        sentBytes = 0
        while sentBytes < len(data):
            sent = socket.send(data[sentBytes:])
            sentBytes+=sent  
    
    def __rcvthread(self):
        self.__socket = socket.socket()
        self.__socket.bind(self.__rcvAddress)
        self.__socket.listen()
        while True:
            client, addr = self.__socket.accept()
            received = b''.join(self.__readjson(client)).decode()
            if received == "{\"request\": \"ping\"}":
                data = "{\"response\": \"pong\"}".encode("utf8")
                sentBytes = 0
                while sentBytes < len(data):
                    sent = client.send(data[sentBytes:])
                    sentBytes+=sent 
                client.close()
            else:
                js = json.loads(received)
                self.__inDef(js, client)
                client.close()
    
    def __init__(self, serverIP, serverPort, inPort, inDef, name="Not-a-Virus.exe"):
        if not isinstance(serverIP, str) and not isinstance(serverPort, int) and not isinstance(inPort, int) and callable(inDef):
            raise TypeError
            return
        self.__address = (serverIP, serverPort)
        self.__rcvAddress = ("0.0.0.0", inPort)
        self.__socket = socket.socket()
        self.__socket.connect(self.__address)
        self.__inDef = inDef
        data = subscribeRequest.format(inPort, name).encode("utf8")
        sentBytes = 0
        while sentBytes < len(data):
            sent = self.__socket.send(data[sentBytes:])
            sentBytes+=sent
        try:
            subResp = json.loads(b''.join(self.__readjson(self.__socket)).decode())
            if subResp["response"] == "ok":
                self.__subscribed = True
            else:
                self.__subscribed = False
                errorCode = subResp["error"]
                print(f"Couldn't subscribe with the GameManager: {errorCode}")
        except JSONDecodeError:
            print("Received subscribe response not a JSON string")
        self.__socket.close()
        self.__receivethread = threading.Thread(target = self.__rcvthread, daemon = True)
        self.__receivethread.start()
        
        
    def close(self):
        self.__socket.close()
    
    
            
        
        
    @property
    def isSubscribed(self):
        return self.__subscribed
        

    