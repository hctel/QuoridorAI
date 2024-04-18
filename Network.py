import socket, json, threading, time
from json.decoder import JSONDecodeError

#Initial subscribe request. As only the port changes, we chose to hard-code that request string.
subscribeRequest = "{{\"request\": \"subscribe\",\"port\": {},\"name\": \"Not-A-Virus.exe\",\"matricules\": [\"22054\", \"22167\"]}}"

class Network:
    
    #Reads a JSON data from a socket
    def __readjson(self, sct):
        chunks = []
        finished = False
        while not finished: #Receive loop
            data = sct.recv(2048)
            chunks.append(data)
            jt = b''.join(chunks).decode()
            try: #Checks if the read string can be decoded as a JSON. If it can, it returns a dictionary created from the JSON string.
                json.loads(jt)
                finished = True
            except JSONDecodeError:
                pass
        return jt
    
    #Sends a string on a socket
    def send(self, socket, toSend):
        data = toSend.encode("utf8")
        sentBytes = 0
        while sentBytes < len(data): #Send loop
            sent = socket.send(data[sentBytes:])
            sentBytes+=sent  
            
    #This is the receiving thread. Threading is needed as socket.accept() is a locking function call.
    def __rcvthread(self):
        self.__socket = socket.socket()
        self.__socket.bind(self.__rcvAddress)
        self.__socket.listen()
        while True: #Infinite loop to accept clients
            client, addr = self.__socket.accept()
            received = self.__readjson(client)
            if received == "{\"request\": \"ping\"}":
                data = "{\"response\": \"pong\"}".encode("utf8")
                sentBytes = 0
                while sentBytes < len(data):
                    sent = client.send(data[sentBytes:])
                    sentBytes+=sent 
                client.close()
            else:
                js = json.loads(received)
                self.__inDef(js, client) #Calls the function passed as an argument in init.
                client.close()
            if self.__stopped == True: #Allows the thread to end when requested
                break
    

    #Creates the Network object. serverIP is a string of the server IP, serverPort is an int of the server listening port, inPort is an int of our program's port and inDef is a function to be called when 
    def __init__(self, serverIP, serverPort, inPort, inDef):

        if not isinstance(serverIP, str) and not isinstance(serverPort, int) and not isinstance(inPort, int) and callable(inDef):
            raise TypeError
            return
        self.__stopped = False
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
            subResp = json.loads(self.__readjson(self.__socket))
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
        
    #Closes the connection
    def close(self):
        self.__stopped = True
        self.__socket.close()
        if self.__receivethread is not None:
            self.__receivethread.join()
            
    
    @property
    def isSubscribed(self):
        return self.__subscribed
        

    