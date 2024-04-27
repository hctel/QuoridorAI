import multiprocessing as mp
import sys, Main
from random import randint
number_of_cores = 6
start_port = 3001

start_array = [-0.5,14.5,-13.5,-4,-13]
delta = 5
at = True


def run(port, w):
    Main.train(port, w)   
    

if __name__ == "__main__":
    if at :
        processes = []
        ports = 3001
        for i in range(3001, 3001+number_of_cores):
            print(i)
            p = mp.Process(target = run, args = (i, [randint(-30,30)/2, randint(-30,30)/2,randint(-30,30)/2,randint(-30,30)/2,randint(-30,30)/2]))
            p.start()
            processes.append(p)
        processes[0].join()
    else :
        processes = []
        ports = 3001
        for i in range(3001, 3001+number_of_cores):
            print(i)
            p = mp.Process(target = run, args = (i, [randint((start_array[0]-delta)*2,(start_array[0]+delta)*2)/2, randint((start_array[1]-delta)*2,(start_array[1]+delta)*2)/2,randint((start_array[2]-delta)*2,(start_array[2]+delta)*2)/2,randint((start_array[3]-delta)*2,(start_array[3]+delta)*2)/2,randint(-30,30)/2]))
            p.start()
            processes.append(p)
        processes[0].join()