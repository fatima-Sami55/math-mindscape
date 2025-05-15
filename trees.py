import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Step 1: Load the file and prepare the DataFrame
file_path = 'soc-pokec-relationships.txt'
df = pd.read_csv(file_path, sep="\t", header=None, names=["user", "friend"], nrows=30)

# Step 2: Create a directed graph using networkx
G = nx.DiGraph()

# Add directed edges to the graph based on the dataframe
for _, row in df.iterrows():
    G.add_edge(row['user'], row['friend'])

# Step 3: Visualize the directed graph using networkx
plt.figure(figsize=(12, 12))

# Using a layout for better visualization
pos = nx.spring_layout(G, k=0.15, iterations=20)

# Draw the graph
nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=12, font_weight="bold", edge_color="gray", arrows=True)
plt.title("Friendship Tree Visualization (Directed)")
plt.show()

# Step 4: Tree traversal methods

# Preorder traversal (depth-first search, visiting root before children)
def preorder_traversal(G, start_node):
    visited = set()
    def dfs(node):
        if node not in visited:
            visited.add(node)
            print(node, end=" ")
            for neighbor in G[node]:
                dfs(neighbor)
    
    dfs(start_node)

# Postorder traversal (depth-first search, visiting children before root)
def postorder_traversal(G, start_node):
    visited = set()
    def dfs(node):
        if node not in visited:
            visited.add(node)
            for neighbor in G[node]:
                dfs(neighbor)
            print(node, end=" ")

    dfs(start_node)

# Breadth-first search (visiting all neighbors level by level)
def bfs_traversal(G, start_node):
    visited = set()
    queue = [start_node]
    visited.add(start_node)
    
    while queue:
        node = queue.pop(0)
        print(node, end=" ")
        for neighbor in G[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example usage (starting traversal from node 1)
print("Preorder Traversal:")
preorder_traversal(G, 1)
print("\n\nPostorder Traversal:")
postorder_traversal(G, 1)
print("\n\nBreadth-First Search Traversal:")
bfs_traversal(G, 1)
