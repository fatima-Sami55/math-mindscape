from main import pd
import sys

sys.setrecursionlimit(10000)  # Set a higher recursion limit (double the default)

def induction_proof_recursive(data, threshold, X, index=0, count=0):
    """
    Recursively checks the number of users with a completion percentage above a threshold
    and proves by structural induction that this number is greater than X.
    
    :param data: DataFrame, the dataset
    :param threshold: int, the threshold for completion percentage
    :param X: int, the value to compare the count against
    :param index: int, the current index in the dataset being checked
    :param count: int, the count of users with completion percentage above the threshold
    :return: bool, whether the count is greater than X after processing all users
    """
    # Base case: If we've checked all the users (or up to the given index)
    if index >= len(data):
        print(f"Base case reached: {count} users have a completion percentage above {threshold}.")
        return count > X
    
    # Recursively check the completion percentage of the current user
    current_value = data.iloc[index, 2]  # Assuming completion_percentage is in the second column (index 1)
    
    if current_value > threshold:
        count += 1  # Increment count if the completion percentage is above the threshold
    
    # Inductive step: process the next user
    print(f"Checking user {index + 1}, current count is {count}.")
    
    # Recursively call the function with the next user
    return induction_proof_recursive(data, threshold, X, index + 1, count)

def induction_proof_iterative(data, threshold, X):
    """
    Iteratively checks the number of users with a completion percentage above a threshold
    and proves by structural induction that this number is greater than X.

    :param data: DataFrame, the dataset
    :param threshold: int, the threshold for completion percentage
    :param X: int, the value to compare the count against
    :return: bool, whether the count is greater than X after processing all users
    """
    count = 0

    # Iterate through each user's completion percentage
    for index, row in data.iterrows():
        current_value = row.iloc[2]  # Use .iloc[] to access by position (third column)

        if current_value > threshold:
            count += 1  # Increment count if the completion percentage is above the threshold

        print(f"Checking user {index + 1}, current count is {count}.")

        # Early exit if count already exceeds X
        if count > X:
            print(f"Early exit: The count ({count}) has exceeded {X}.")
            return True

    # Final conclusion after iterating through all users
    print(f"Final count: {count} users have a completion percentage above {threshold}.")
    return count > X

def induction_proof(file_path, threshold, X, method='recursive'):
    """
    This function chooses whether to use the recursive or iterative method for induction proof.

    :param file_path: str, the path to the dataset file
    :param threshold: int, the threshold for completion percentage
    :param X: int, the value to compare the count against
    :param method: str, the method to use for induction ('recursive' or 'iterative')
    """
    # Load only the first 1000 rows of the dataset
    data = pd.read_csv(file_path, delimiter='\t', engine='python', nrows=50)


    # Assuming the completion percentage is in the second column (index 1)
    # Clean and process the dataset
    data.iloc[:, 1] = data.iloc[:, 1].astype(str).str.strip().astype(int)

    # Choose the method to use
    if method == 'recursive':
        result = induction_proof_recursive(data, threshold, X)
    elif method == 'iterative':
        result = induction_proof_iterative(data, threshold, X)
    else:
        print("Invalid method. Please choose 'recursive' or 'iterative'.")
        return

    # Final conclusion after the process
    if result:
        print(f"\nConclusion: The number of users with a completion percentage above {threshold} is greater than {X}.")
    else:
        print(f"\nConclusion: The number of users with a completion percentage above {threshold} is not greater than {X}.")

# Now, call the function outside
file_path = 'soc-pokec-profiles.txt'  # Path to your dataset
threshold = 50  # Example threshold for completion percentage
X = 100  # Example value for X, change it as needed

# To use recursion
induction_proof(file_path, threshold, X, method='recursive')

# To use iteration
induction_proof(file_path, threshold, X, method='iterative')
