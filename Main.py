from Network import *
import time

def handleRcv(js, client):
    print(js)
    
def train(port, w1, w2, w3, w4, w5):
    network = Network("localhost", 3000, port, handleRcv, f"{w1};{w2};{w3};{w4};{w5}")
    if network.isSubscribed:
        print("Registered with server! Yay!")
    else: 
        print("Error when registering with server...")
    while True:
        time.sleep(1)

if __name__ == "__main__":
    network = Network("localhost", 3000, 3001, handleRcv)
    if network.isSubscribed:
        print("Registered with server! Yay!")
    else: 
        print("Error when registering with server...")
    while True:
        time.sleep(1)
