from main import pd
import math

def count_completions_and_permutation(file_path):
    """
    Counts how many users have 50% completion from the first 1000 rows
    and calculates the permutation of those users.
    
    :param file_path: str, path to the file containing user data
    :return: tuple (count_50_percent, permutation_value)
    """
    try:
        # Read only the first 1000 rows of the file (assuming tab-delimited data)
        data = pd.read_table(file_path, header=None, nrows=10000, sep='\t')  # Adjust nrows to 1000
        
        # Assuming the completion percentage is in the second column (index 1)
        completion_percentage_col = 2  # Column 2 corresponds to index 1
        
        # Filter users with 50% completion
        users_with_50_percent = data[data[completion_percentage_col] == 50]
        
        # Count the number of users with 50% completion
        count_50_percent = len(users_with_50_percent)
        
        # If there are users with 50% completion, calculate the permutation
        if count_50_percent > 1:
            permutation_value = math.perm(count_50_percent, 2)  # P(n, 2) where n = count_50_percent
        else:
            permutation_value = 0  # If less than 2 users, no valid permutation
        
        return count_50_percent, permutation_value
    
    except Exception as e:
        return f"An error occurred: {e}"

# Load the dataset (first 1000 rows for simplicity)
file_path = 'soc-pokec-profiles.txt'  # Replace with the correct path
data = pd.read_csv(file_path, delimiter='\t', engine='python', nrows=1000)

# Clean the data
data.iloc[:, 1] = data.iloc[:, 1].astype(str).str.strip().astype(int)

# Filter users who are over 25 and from Bratislava
over_25_bratislava_users = data[(data.iloc[:, 2] > 25) & (data.iloc[:, 4].str.contains('Bratislava', case=False, na=False))]

# Get the number of users in this filtered subgroup
num_users = len(over_25_bratislava_users)

# Example: Count the number of ways to select 3 users from this subgroup (C(n, k) formula)
k = 3  # You can change this value to select any number of users
if num_users >= k:
    combinations = math.comb(num_users, k)
else:
    combinations = 0  # Not enough users to select k

# Print total users and combinations for verification
print(f"Total users over 25 and from Bratislava: {num_users}")
print(f"Number of ways to select {k} users from this subgroup (combinations): {combinations}")

# Count completions and calculate permutation for users with 50% completion
count_50_percent, permutation_value = count_completions_and_permutation(file_path)
print(f"Number of users with 50% completion: {count_50_percent}")
print(f"Permutation of users with 50% completion: {permutation_value}")
