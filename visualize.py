import networkx as nx
import math
from matplotlib import pylab as plt
from summarizer import get_graph
with open("training.txt") as file:
    text = file.read()
graph=get_graph(text)
edge_list=[]
G=nx.DiGraph()
for edge in graph.edge_properties:
	G.add_edges_from([edge],weight=round(graph.edge_properties[edge]['weight'],2))
edge_labels=dict([((u,v,),d['weight']) for u,v,d in G.edges(data=True)])
pos=nx.random_layout(G)
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
nx.draw(G,pos,node_size=150,edge_cmap=plt.cm.Reds,with_labels=False)
#nx.draw(graph, ) 
plt.show()