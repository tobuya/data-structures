"""The below modules will help create a basic visual representation of a Linked List."""
import networkx as nx
import matplotlib.pyplot as plt

# Define the linked list
nodes = [1, 2, 3, 4]
edges = [(1, 2), (2, 3), (3, 4)]

# Create a directed graph
G = nx.DiGraph()

# Add nodes to the graph
G.add_nodes_from(nodes)

# Add edges to the graph
G.add_edges_from(edges)

# Draw the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_weight='bold', font_size=12, arrows=True)
plt.title('Linked List Visualization')
plt.show()
