
def check_two_users_proposition(file_path, user_id_1, user_id_2):
    """
    Checks if the proposition "If a Pokec user is male, then their completion
    percentage is greater than 50%" holds true for the specified users.

    :param file_path: str, path to the file containing user data
    :param user_id_1: int, ID of the first user
    :param user_id_2: int, ID of the second user
    :return: str, result of the proposition check for the two users
    """
    try:
        # Open the file and read line by line
        with open(file_path, 'r', encoding='utf-8') as file:
            user_data = {}
            
            # Read through the file and collect data for both users
            for line in file:
                columns = line.strip().split('\t')
                
                # Check if the line has the expected number of columns
                if len(columns) < 8:
                    continue  # Skip incomplete rows

                user_id = int(columns[0])
                gender = columns[3]  # Gender is in the 4th column
                completion_percentage = columns[2]  # Completion percentage is in the 3rd column
                
                # Only store the users we're interested in
                if user_id == user_id_1 or user_id == user_id_2:
                    user_data[user_id] = (gender, completion_percentage)
                
                # If both users have been found, no need to continue reading
                if len(user_data) == 2:
                    break

        # If we didn't find both users
        if user_id_1 not in user_data or user_id_2 not in user_data:
            return f"Could not find both users (IDs {user_id_1} and {user_id_2}) in the dataset."
        
        # Extract gender and completion percentage for both users
        gender1, completion1 = user_data[user_id_1]
        gender2, completion2 = user_data[user_id_2]

        # Convert completion percentage to integer, handling 'null' values
        completion1 = int(completion1) if completion1 != 'null' else 0
        completion2 = int(completion2) if completion2 != 'null' else 0

        # Function to check the proposition for a single user
        def check_user_proposition(gender, completion_percentage):
            if gender == '1' and completion_percentage <= 50:
                return False  # Male with completion percentage <= 50, proposition fails
            return True  # Either female or male with completion > 50, proposition holds

        # Evaluate proposition for both users
        result_user1 = check_user_proposition(gender1, completion1)
        result_user2 = check_user_proposition(gender2, completion2)

        # Return the results for both users
        return (
            f"User {user_id_1} proposition holds: {result_user1}\n"
            f"User {user_id_2} proposition holds: {result_user2}"
        )
    
    except Exception as e:
        return f"An error occurred: {e}"

# Example Usage
file_path = "soc-pokec-profiles.txt"  # Path to your file
user_id_1 = 5  # Example user ID 1
user_id_2 = 3  # Example user ID 2
result = check_two_users_proposition(file_path, user_id_1, user_id_2)
print(result)
