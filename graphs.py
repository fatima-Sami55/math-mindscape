import pandas as pd
import networkx as nx
import random
import matplotlib.pyplot as plt

# Load the dataset in chunks
file_path = 'soc-pokec-relationships.txt'
chunk_size = 1000000  # Adjust chunk size based on your system's memory

# Create an undirected graph
G = nx.Graph()

# Process the file in chunks
for chunk in pd.read_csv(file_path, sep='\t', header=None, names=['user1', 'user2'], chunksize=chunk_size, nrows=100000):
    for _, row in chunk.iterrows():
        G.add_edge(row['user1'], row['user2'])

# Step 1: Select a random sample of 3000 users from the graph (ensure the graph has at least 3000 nodes)
if len(G.nodes()) >= 3000:
    sample_users = random.sample(list(G.nodes()), 3000)  # Convert G.nodes() to a list
else:
    raise ValueError("Graph has fewer than 3000 nodes.")

# Create a subgraph with these 3000 users
subgraph = G.subgraph(sample_users)

# Step 2: Check if the subgraph is bipartite (by checking for odd-length cycles)
def contains_odd_cycle(subgraph):
    try:
        # Directly check if the graph is bipartite (which also checks for odd-length cycles)
        return not nx.is_bipartite(subgraph)
    except nx.NetworkXError:
        return False

# Check for odd-length cycles
if contains_odd_cycle(subgraph):
    print("The subgraph contains an odd-length cycle, so it is NOT bipartite.")
else:
    # Check if the subgraph is bipartite using the existing check
    is_bipartite = nx.is_bipartite(subgraph)
    print(f"Is the subgraph bipartite? {is_bipartite}")

# Step 3: Compute the Minimum Spanning Tree (MST) using Prim's algorithm
mst = nx.minimum_spanning_tree(subgraph)

# Convert MST edges to Python int and display
mst_edges_int = [(int(u), int(v)) for u, v in mst.edges()]
print(f"MST edges (first 10): {mst_edges_int[:10]}")  # Display first 10 edges for brevity

# Visualization

# Plotting the original subgraph
plt.figure(figsize=(12, 12))
pos_subgraph = nx.spring_layout(subgraph, k=0.15, iterations=20)
nx.draw(subgraph, pos=pos_subgraph, with_labels=True, node_size=10, node_color="skyblue", font_size=5, font_weight="bold", edge_color="gray")
plt.title("Subgraph Visualization")
plt.show()

# Plotting the Minimum Spanning Tree (MST)
plt.figure(figsize=(12, 12))
pos_mst = nx.spring_layout(mst, k=0.15, iterations=20)
nx.draw(mst, pos=pos_mst, with_labels=True, node_size=10, node_color="lightgreen", font_size=5, font_weight="bold", edge_color="blue")
plt.title("Minimum Spanning Tree (MST) Visualization")
plt.show()
