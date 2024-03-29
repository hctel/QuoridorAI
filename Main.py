from Network import *
import time

def handleRcv(js, client):
    print(js)

if __name__ == "__main__":
    network = Network("localhost", 3000, 3001, handleRcv)
    if network.isSubscribed:
        print("Registered with server! Yay!")
    else: 
        print("Error when registering with server...")
    while True:
        time.sleep(1)