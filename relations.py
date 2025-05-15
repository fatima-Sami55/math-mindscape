from main import pd
import random

# Function to load friendship data from the file
def load_friendships(filename):
    df = pd.read_csv(filename, sep='\t', header=None, nrows=20000)
    # Each row contains a pair of users who are friends
    df.columns = ['user_1', 'user_2']
    # Convert DataFrame to a list of tuples (relations)
    relation = set(zip(df['user_1'], df['user_2']))
    return relation, set(df['user_1']).union(set(df['user_2']))  # Return relation and unique elements (users)

# Function to check if the relation is reflexive
def is_reflexive(relation, elements):
    reflexive_relations = set()
    # Check if for every element in elements, (a, a) is in the relation
    for element in elements:
        if (element, element) in relation:
            reflexive_relations.add((element, element))
    
    return reflexive_relations

# Function to check if the relation is symmetric
def is_symmetric(relation):
    symmetric_relations = set()
    # Check if for every (a, b) in the relation, (b, a) is also in the relation
    for a, b in relation:
        if (b, a) in relation:
            symmetric_relations.add((a, b))
            symmetric_relations.add((b, a))  # Also add the reflected pair
    return symmetric_relations

# Function to check if the relation is transitive
def is_transitive(relation):
    transitive_relations = set()
    # Check if for every (a, b) and (b, c) in the relation, (a, c) is also in the relation
    for a, b in relation:
        for x, y in relation:
            if b == x and (a, y) in relation:
                # Record the transitive triplet (a, b), (b, c), (a, c)
                transitive_relations.add((a, b, (b, y)))  # (a, b) -> (b, c) -> (a, c)
    
    return transitive_relations

# Example usage
if __name__ == "__main__":
    filename = 'soc-pokec-relationships.txt'  # Replace with your actual file name
    relation, elements = load_friendships(filename)

    # Check reflexive relations
    reflexive_relations = is_reflexive(relation, elements)
    if reflexive_relations:
        print(f"Number of reflexive relations: {len(reflexive_relations)}")
        print("10 random reflexive relations:")
        print(random.sample(list(reflexive_relations), min(10, len(reflexive_relations))))
    else:
        print("No reflexive relations found.")

    # Check symmetric relations
    symmetric_relations = is_symmetric(relation)
    if symmetric_relations:
        print(f"\nNumber of symmetric relations: {len(symmetric_relations)//2}")  # Each pair shows up twice
        print("10 random symmetric relations (including reflected pairs):")
        symmetric_list = list(symmetric_relations)
        # Select 10 random symmetric relations
        random_symmetric_pairs = random.sample(symmetric_list, min(10, len(symmetric_list) // 2))  # Avoid duplicates
        for pair in random_symmetric_pairs:
            # Print both the pair and its reflected pair (if different)
            a, b = pair
            reflected_pair = (b, a) if a != b else None
            print(f"Pair: ({a}, {b})", f"Reflected pair: ({b}, {a})" if reflected_pair else "")
    else:
        print("\nNo symmetric relations found.")
    
    # Check transitive relations
    transitive_relations = is_transitive(relation)
    if transitive_relations:
        print(f"\nNumber of transitive relations: {len(transitive_relations)}")
        print("10 random transitive relations (including the three related pairs):")
        transitive_list = list(transitive_relations)
        # Select 10 random transitive relations (triplets)
        random_transitive_triplets = random.sample(transitive_list, min(10, len(transitive_list)))
        for triplet in random_transitive_triplets:
            a, b, (b, y) = triplet  # Extracting the three pairs: (a, b), (b, c), and (a, c)
            print(f"Pair 1: ({a}, {b}), Pair 2: ({b}, {y}), Transitive Pair: ({a}, {y})")
    else:
        print("\nNo transitive relations found.")
