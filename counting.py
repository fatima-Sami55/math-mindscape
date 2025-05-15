from main import pd

# Function to load the dataset and select relevant columns
def load_data(filename):
    # Load the dataset and select relevant columns
    df = pd.read_csv(filename, sep='\t', header=None, nrows=10)  # Adjust nrows if needed
    df = df[[0, 1, 2, 4]]  # Select columns: 0 (user_id), 1 (public_profile), 2 (completion_percentage), 4 (region)
    df.columns = ['user_id', 'public_profile', 'completion_percentage', 'region']  # Rename columns
    
    # Convert columns to numeric values, coercing errors (in case of invalid values)
    df['completion_percentage'] = pd.to_numeric(df['completion_percentage'], errors='coerce')
    df['public_profile'] = pd.to_numeric(df['public_profile'], errors='coerce')
    
    return df

# Counting Users with Profile Completion Above 80% (Using Sum Rule)
def count_users_profile_above_80(df):
    # Apply the sum rule: Count users with completion > 80% and those with completion <= 80%
    above_80_count = len(df[df['completion_percentage'] > 80])
    below_or_equal_80_count = len(df) - above_80_count  # Subtraction rule
    
    return above_80_count, below_or_equal_80_count

# Counting Users in Each Region (Using Sum Rule for Multiple Regions)
def count_users_in_region(df):
    # Extract region name before the comma
    df['region'] = df['region'].str.split(',').str[0]  # Split the string at the comma and keep the first part
    
    # Apply the sum rule: Count users in each distinct region
    region_counts = df['region'].value_counts()
    
    return region_counts

# Counting Users with Public Profiles (Using Difference or Subtraction Rule)
def count_public_profiles(df):
    # Apply the difference rule: Count the users with public profiles
    total_users = len(df)
    public_profiles_count = len(df[df['public_profile'] == 1])
    private_profiles_count = total_users - public_profiles_count  # Subtraction rule
    
    return public_profiles_count, private_profiles_count

# Example usage
if __name__ == "__main__":
    filename = 'soc-pokec-profiles.txt'  # Replace with your actual file name
    
    # Load the dataset
    df = load_data(filename)
    
    # Count users with profile completion above 80%
    above_80, below_or_equal_80 = count_users_profile_above_80(df)
    print(f"Total number of users with profile completion above 80%: {above_80}")
    print(f"Total number of users with profile completion <= 80%: {below_or_equal_80}")
    
    # Count users in each region
    region_counts = count_users_in_region(df)
    print("\nNumber of users in each region:")
    print(region_counts.to_string(index=True))
    
    # Count public profiles
    public_profiles, private_profiles = count_public_profiles(df)
    print(f"\nTotal number of public profiles: {public_profiles}")
    print(f"Total number of private profiles: {private_profiles}")
