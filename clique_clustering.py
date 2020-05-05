# -*- coding: utf-8 -*-
"""
Created on Tue May  5 13:14:54 2020

@author: Hiro
"""

import networkx as nx
from itertools import combinations

G = nx.random_geometric_graph(50, .3)
pos = nx.spring_layout(G)
nx.draw(G, pos)

k = 4

perc_graph = nx.Graph()

cliques = {i:set(c) for i, c in enumerate(nx.find_cliques(G)) if len(c) >= k}

perc_graph.add_nodes_from(list(cliques.keys()))

for c1, c2 in combinations(cliques, 2):
    if len(cliques[c1].intersection(cliques[c2])) >= k-1:
        perc_graph.add_edge(c1, c2)
        
nx.draw(perc_graph)

##############################################################
clusters = {}

for j, graph in enumerate(nx.connected_components(perc_graph)):
    clusters[j] = []
    for i in graph:
        clusters[j].extend( list(cliques[i]))

for i in clusters:
    clusters[i] = list(set(clusters[i]))
    
clusters

###########################################################

colors = ['b', 'g', 'y', 'r', 'c', 'm']

plt.figure()
plt.gca().set_axis_off()
nx.draw_networkx_nodes(G, pos, node_color = 'k')
for i in clusters:
    nx.draw_networkx_nodes(G, pos, nodelist = clusters[i], node_color = colors[i%len(colors)])

nx.draw_networkx_edges(G, pos)