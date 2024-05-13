#"enums" for easier use
INIT = 0
SPECIALIZE = 1
CUSTOM = 2

import multiprocessing as mp
import Main
from random import randint, uniform

number_of_cores = 6 #Or the number of instances to be created
start_port = 3001 #Starting network port

center_weights = [0,0,0,0,0,0] #Weights to be altered for further precision
delta = 0.5 #Max alteration of the weigts (ex. if 0.5 : -0.5 to 0.5)

mode = CUSTOM #Training mode

custom_weights = [[-5,5,7,13,-4,11],[-8,4,2,16,1,10],[-8,7,13,-9,7,-4],[-13,-12,-6,-1,13,-8],[-8,13,-14,5,6,11]] #Weights to be tested

def run(port, w):
    Main.train(port, w)   

# Training function to find the best weights for the searching algorithm
if __name__ == "__main__":
    if mode == INIT :
        processes = []
        ports = 3001
        for i in range(3001, 3001+number_of_cores):
            p = mp.Process(target = run, args = (i, [randint(-15,15), randint(-15,15),randint(-15,15),randint(-15,15),randint(-15,15),randint(-15,15)])) #Creates each instance with random weights from -15 to 15
            p.start()
            processes.append(p)
        processes[0].join()
    elif mode == SPECIALIZE:
        processes = []
        ports = 3001
        for i in range(3001, 3001+number_of_cores):
            #Creates an instance with the randomly altered weights
            p = mp.Process(target = run, args = (i, [uniform(-delta, delta)+center_weights[0], uniform(-delta, delta)+center_weights[1],uniform(-delta, delta)+center_weights[2],uniform(-delta, delta)+center_weights[3],uniform(-delta, delta)+center_weights[4],uniform(-delta, delta)+center_weights[5]]))
            p.start()
            processes.append(p)
        processes[0].join()
    elif mode == CUSTOM:
        processes = []
        startPort = 3001
        for i in range(0,len(custom_weights)):
            p = mp.Process(target = run, args = (i+startPort, custom_weights[i]))
            p.start()
            processes.append(p)
        processes[0].join()
        