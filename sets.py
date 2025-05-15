from main import pd

# Load the dataset (use only the first 10 rows for simplicity)
file_path = 'soc-pokec-profiles.txt'  # Replace with the correct path
data = pd.read_csv(file_path, delimiter='\t', engine='python', nrows=1000)

# Clean and convert 'public' column to integers
data.iloc[:, 1] = data.iloc[:, 1].astype(str).str.strip().astype(int)

# Set A: All users who are socially public (public column = 1)
socially_public_users = data[data.iloc[:, 1] == 1]
set_A = set(socially_public_users.iloc[:, 0])  # User IDs in the first column

# Set B: All users from Bratislava (region column = 4)
bratislava_users = data[data.iloc[:, 4].str.contains('Bratislava', case=False, na=False)]
set_B = set(bratislava_users.iloc[:, 0])  # User IDs in the first column

# Universal set: All users in the dataset
universal_set = set(data.iloc[:, 0])

# Set operations
union_AB = set_A | set_B          # A ∪ B
intersection_AB = set_A & set_B   # A ∩ B
complement_A = universal_set - set_A  # A'

# Display results
print("Results from the first 1000 rows of the dataset:")
print(f"Set A (Socially Public Users): {set_A}")
print(f"Set B (Users in Bratislava): {set_B}")
print(f"A ∪ B (Union): {union_AB}")
print(f"A ∩ B (Intersection): {intersection_AB}")
print(f"A' (Complement of A): {complement_A}")
