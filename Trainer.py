import multiprocessing as mp
import sys, Main
from random import randint
number_of_cores = 42
start_port = 3001


def run(port, w1, w2, w3, w4, w5):
    Main.train(port, w1, w2, w3, w4, w5)   
    

if __name__ == "__main__":
    if sys.argv[0] == "firstRun":
        ports = range(3001, 3001+number_of_cores+1)
        with mp.Pool(number_of_cores) as pool:
            pool.map(run(ports.step, randint(0,100)*5/3, randint(0,100)*5/3,randint(0,100)*5/3,randint(0,100)*5/3,randint(0,100)*5/3))
            
        