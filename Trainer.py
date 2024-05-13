INIT = 0
SPECIALIZE = 1
CUSTOM = 2


import multiprocessing as mp
import Main
from random import randint, uniform
number_of_cores = 10
start_port = 3001

center_weights = [-13,10,-1,-13,-4,-5]
delta = 10
mode = CUSTOM

# 1st round
#custom_weights = [[-5,5,7,13,-4,11],[-8,4,2,16,1,10],[-8,7,13,-9,7,-4],[-13,-12,-6,-1,13,-8],[-8,13,-14,5,6,11]]
#custom_weights = [[-5,5,7,13,-4,11],[-8,4,2,16,1,10],[-13,-12,-6,-1,13,-8],[-8,13,-14,5,6,11]]
#custom_weights = [[-8,4,2,16,1,10],[-13,-12,-6,-1,13,-8],[-8,13,-14,5,6,11]]
#custom_weights = [[-8,4,2,16,1,10],[-13,-12,-6,-1,13,-8]]
#custom_weights = [[-8,4,2,16,1,10]]

#custom_weights = [[-8,4,2,16,1,10],[-9,5,2,15,2,11]] # good winners

# 2nd round
#custom_weights = [[-10,5,-15,-13,-5,5],[-2,6,-4,-7,13,15],[0,-14,-3,10,6,-4]]

# 3nd round
#custom_weights = [[-13,10,-1,-13,-4,-5],[6,14,-10,-9,7,-10]]

# 4nd round
#custom_weights = [[-14,-12,-11,2,-8,-14],[-5,10,-13,7,11,-15]]

# 4nd round
#custom_weights = [[-10,11,4,-7,-13,3]]

# championship
'''custom_weights = [[-8,4,2,16,1,10],[-13,-12,-6,-1,13,-8],[-8,13,-14,5,6,11],[-9,5,2,15,2,11],
                  [-10,5,-15,-13,-5,5],[-2,6,-4,-7,13,15],[0,-14,-3,10,6,-4],
                  [-13,10,-1,-13,-4,-5],[6,14,-10,-9,7,-10],
                  [-14,-12,-11,2,-8,-14],[-5,10,-13,7,11,-15],
                  [-10,11,4,-7,-13,3]]'''

#custom_weights = [[-8,4,2,16,1,10],[-9,5,2,15,2,11],[-13,10,-1,-13,-4,-5]]
#custom_weights = [[-8,4,2,16,1,10],[-9,5,2,15,2,11],[-13,10,-1,-13,-4,-5],[-8,13,-1,-6,-5,2],[-9,14,-2,-15,-14,-11],[-8,4,2,16,1,10]]
#custom_weights = [[-8,4,2,16,1,10],[-9,5,2,15,2,11],[-13,10,-1,-13,-4,-5],[-8,4,2,16,1,10]] # -9 is better
#custom_weights = [[-9,14,-2,-15,-14,-11],[-9,5,2,15,2,11]] # -9,5 is better

custom_weights = [[-9,5,2,15,2,11],[-13,10,-1,-13,-4,-5]]

def run(port, w):
    Main.train(port, w)   

# Training function to find the best weights for the searching algorithm
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
            p = mp.Process(target = run, args = (i, [randint(-delta, delta)+center_weights[0], randint(-delta, delta)+center_weights[1],randint(-delta, delta)+center_weights[2],randint(-delta, delta)+center_weights[3],randint(-delta, delta)+center_weights[4],randint(-delta, delta)+center_weights[5]]))
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
        