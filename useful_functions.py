import numpy as np
import networkx as nx
from itertools import product
from collections import defaultdict



## Newly defined

def hypergraph_statistics(dictionary):
    
    E = len(dictionary)
    
    nodeset = set()
    in_dict = defaultdict(lambda: 0)
    out_dict = defaultdict(lambda: 0)
    size_dict = defaultdict(lambda: 0)
    
    for edge in dictionary.values():
        
        for node in edge[0] + edge[1]:
            nodeset.add(node)
            
        len_in = len(edge[0])
        len_out = len(edge[1])
        
        in_dict[len_in] += 1
        out_dict[len_out] += 1
        size_dict[(len_in, len_out)] += 1
    
    N = len(nodeset)
    
    return N, E, in_dict, out_dict, size_dict


def labels_to_integers(dictionary):
    
    labels = {}
    relabeled_dictionary = {}
    
    i = 0
    for edge, (in_edge, out_edge) in dictionary.items():
        
        # Add nodes to the dictionary, if not already there
        for node in in_edge + out_edge:
            if node not in labels.keys():
                labels[node] = i
                i += 1
        
        # Fill the new dictionary
        in_relabeled = [labels[node] for node in in_edge]
        out_relabeled = [labels[node] for node in out_edge]
        
        relabeled_dictionary[edge] = (in_relabeled, out_relabeled)
    
    return labels, relabeled_dictionary



## Top N nodes based on a centrality dictionary ##
def topN(cent, N=None, return_list=False):
    """
    Given a dictionary node-centrality score, return the top N ranking
    """

    if not N:
        N = len(cent)
    
    C = sorted(cent, key=cent.get, reverse=True)[:N]
    ranking = {key: cent[key] for key in C}
    
    if return_list:
        return C

    return ranking


def standard_network(dictionary):
    
    G = nx.DiGraph()
    
    for in_edge, out_edge in dictionary.values():
        
        for edge in product(in_edge, out_edge):
            if edge in G.edges:
                G.edges[edge[0], edge[1]]['weight'] += 1
            else:
                G.add_edge(*edge, weight = 1)
                
    return G
