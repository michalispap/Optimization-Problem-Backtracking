import math
import numpy as np

def f(x, y): #objective function
    return 2*x + y**2 + math.exp(-x-y+1)

def gradient(x, y): #gradient(f(x_(n)))
    return np.array([-math.exp(-x-y+1) + 2, -math.exp(-x-y+1) + 2*y])

def delta(x, y): #delta = -1 * inverse_hessian_matrix_of_f(x_(n)) * gradient(f(x_(n)))
    return np.array([-(((math.exp(1-x-y)+2)*(2-math.exp(1-x-y))-math.exp(1-x-y)*(2*y-math.exp(1-x-y)))/(2*math.exp(1-x-y))), -y + 1])

def backtracking(x_n, c, t):
    global counter
    counter += 1
    x_n_new = np.round(x_n + t*delta(x_n[0], x_n[1]), 7) #calculate x_(n + 1)
    temp = round((gradient(x_n[0], x_n[1])[0])*((x_n_new-x_n)[0]) + (gradient(x_n[0], x_n[1])[1])*((x_n_new-x_n)[1]), 7)
    if round(f(x_n_new[0], x_n_new[1]), 7) <= round(f(x_n[0], x_n[1]) + c*temp, 7): #condition is true, algorithm stops
        print('Best approximation of x_n is:', x_n_new)
        return x_n_new
    else: #condition is false, algorithm is repeated with x_(n + 1) and t = t/2
        print('Current x_n is:', x_n_new)
        backtracking(x_n_new, c, t/2)

counter = 0
x_n = np.array([3, 3]) #inital point
c = 0.8
t = 1
print('Initial x_n is:', x_n)
backtracking(x_n, c, t)
print('\nThe Newton backtracking algorithm ran', counter, 'times.')
print('Total number of steps:', counter*3)
