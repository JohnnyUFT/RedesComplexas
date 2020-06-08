import numpy as np
import pandas as pd
import networkx as nx
from matplotlib import pyplot as plt
# %matplotlib inline
import seaborn as sns

# inicializa grafo (NetworkX):
G = nx.Graph()

fh=open('./data/facebook_combined.txt', 'rb')
#fh.close()

G=nx.read_weighted_edgelist(fh)

print(G.nodes())
