import multiprocessing as mp
import sys, Main
from random import randint, uniform
number_of_cores = 22
start_port = 3001

center_weights = [0,0,0,0]
delta = 0.5

def run(port, w):
    Main.train(port, w)   
    

if __name__ == "__main__":
    if True :
        processes = []
        ports = 3001
        for i in range(3001, 3001+number_of_cores):
            print(i)
            p = mp.Process(target = run, args = (i, [randint(-15,0), randint(0,15),randint(0,15),randint(-15,0),randint(-5,5)*5/3]))
            p.start()
            processes.append(p)
        processes[0].join()
    else:
        processes = []
        ports = 3001
        for i in range(3001, 3001+number_of_cores):
            print(i)
            p = mp.Process(target = run, args = (i, [uniform(-delta, delta)+center_weights[0], uniform(-delta, delta)+center_weights[1],uniform(-delta, delta)+center_weights[2],uniform(-delta, delta)+center_weights[3],uniform(-5,5)*5/3]))
            p.start()
            processes.append(p)
        processes[0].join()