"""The below modules will help create a basic visual representation of a graph."""
import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Add nodes to the graph
nodes = [1, 2, 3, 4, 5]
G.add_nodes_from(nodes)

# Add edges between nodes
edges = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5)]
G.add_edges_from(edges)

# Visualize the graph
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)

nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_weight='bold', font_size=12, edge_color='black', width=1.5)
plt.title('Basic Graph Visualization')
plt.axis('off')
plt.show()
