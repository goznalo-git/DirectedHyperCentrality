import numpy as np
from itertools import product, permutations
from collections import defaultdict



def directed_tensor(dictionary, N):
    
    L = len(list(dictionary.values())[0][0] + list(dictionary.values())[0][1])

    tensor_dict = defaultdict(lambda: 0)

    for in_edge, out_edge in dictionary.values():
        
        for out_node in out_edge:
            
            for in_nodes in set(permutations(in_edge)):
                
                indices = tuple([in_node for in_node in in_nodes] + [out_node])
                
                tensor_dict[indices] += 1
        
    return dict(tensor_dict), tuple([N]*L)


def tensor_in_degree_centrality(T, weighted=True):
    
    cent = defaultdict(lambda: 0)
    
    for edge, weight in T[0].items():
        
        if weighted:
            cent[edge[-1]] += weight
        else:
            cent[edge[-1]] += 1
            
    return cent



########## FROM UPLIFT PROJECT #############

def HEC_ours(T, m=3, niter=100, tol=1e-6, verbose=True):
    '''
    Given a hypergraph (tensor, in the form of a sparse tensor, (python dictionary, shape)) T, we calculate it HEC using the power method.
    :param T :: (python dictionary, shape):
    :param m :: Integer (power):
    :param niter :: Integer (number of iterations):
    '''
    converged = False
    x = np.ones(T[1][0])
    y = apply(T, x)
    for i in range(niter):
        y_scaled = np.power(y, 1 / m)
        x = y_scaled / np.sum(y_scaled)
        y = apply(T, x)
        s = np.divide(y, np.power(x, m))
        converged = (max(s) - min(s)) / min(s) < tol

        if converged and verbose:
            print('Finished in', i, 'iterations.')
            break

    return x, converged


def apply(T, x):
    '''
    Given an nth order tensor T, contract it (n-1) times with vector x
    :param T :: (python dictionary, shape):
    :param x :: vector (centralities):
    :return y :: vector (T*x):
    '''
    # Product of a tensor and a vector, only taking the non-zero values (using a dictionary)
    y = np.zeros(x.shape[0])
    for edge, weight in T[0].items():
        y[edge[0]] += weight * np.prod(x[list(edge[1:])])
        
    return y