import multiprocessing as mp
import sys, Main
from random import randint
number_of_cores = 42
start_port = 3001


def run(port, w):
    Main.train(port, w)   
    

if __name__ == "__main__":
    if True :
        processes = []
        ports = 3001
        for i in range(3001, 3001+number_of_cores):
            print(i)
            p = mp.Process(target = run, args = (i, [randint(-5,5)*5/3, randint(-5,5)*5/3,randint(-5,5)*5/3,randint(-5,5)*5/3,randint(-5,5)*5/3]))
            p.run()
            processes.append(p)
        processes[0].join()