"""The below modules will help create a basic visual representation of a tree."""
import networkx as nx
import matplotlib.pyplot as plt

# Create a basic tree structure
tree = nx.DiGraph()

# Add nodes to the tree
tree.add_nodes_from([1, 2, 3, 4, 5, 6, 7])

# Add edges between nodes to form a tree structure
edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)]
tree.add_edges_from(edges)

# Visualize the tree
pos = nx.spring_layout(tree)

plt.figure(figsize=(8, 6))
nx.draw(tree, pos, with_labels=True, node_size=500, node_color='lightblue', font_weight='bold', font_size=12, arrows=True)
plt.title('Basic Tree Visualization')
plt.axis('off')
plt.show()
