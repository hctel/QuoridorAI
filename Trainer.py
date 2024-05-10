INIT = 0
SPECIALIZE = 1
CUSTOM = 2


import multiprocessing as mp
import sys, Main
from random import randint, uniform
number_of_cores = 22
start_port = 3001

center_weights = [0,0,0,0,0,0]
delta = 0.5
mode = CUSTOM

custom_weights = [[-5,5,7,13,-4,11],[-8,4,2,16,1,10],[-8,7,13,-9,7,-4],[-13,-12,-6,-1,13,-8],[-8,13,-14,5,6,11]]

def run(port, w):
    Main.train(port, w)   
    

if __name__ == "__main__":
    if mode == INIT :
        processes = []
        ports = 3001
        for i in range(3001, 3001+number_of_cores):
            print(i)
            p = mp.Process(target = run, args = (i, [randint(-15,15), randint(-15,15),randint(-15,15),randint(-15,15),randint(-15,15),randint(-15,15)]))
            p.start()
            processes.append(p)
        processes[0].join()
    elif mode == SPECIALIZE:
        processes = []
        ports = 3001
        for i in range(3001, 3001+number_of_cores):
            print(i)
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
        