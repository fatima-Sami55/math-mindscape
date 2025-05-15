from main import pd

# Function to load data from the file
def load_data(filename):
    df = pd.read_csv(filename, sep='\t', header=None, nrows=10)
    df = df[[0, 2, 7]]  # Select relevant columns (user_id, completion_percentage, age)
    df.columns = ['user_id', 'completion_percentage', 'age']
    df['completion_percentage'] = pd.to_numeric(df['completion_percentage'], errors='coerce')
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    return df

# Helper function to map user_ids to a specific attribute and check injectiveness and surjectiveness
def map_and_check(df, attribute_column):
    # Map user_ids to the attribute (completion_percentage or age)
    mapped_data = df[['user_id', attribute_column]].set_index('user_id')
    
    # Determine the domain and range
    domain = df['user_id'].unique()  # Unique user_ids for the domain
    range_ = df[attribute_column].dropna().unique()  # Unique values for the range
    
    # Check if the function is injective (one-to-one)
    is_injective = df[attribute_column].is_unique
    
    # Check if the function is surjective (onto)
    is_surjective = set(df[attribute_column].dropna()) == set(range_)

    return mapped_data, domain, range_, is_injective, is_surjective

# Example usage
filename = 'soc-pokec-profiles.txt'  # Replace with your actual filename
df = load_data(filename)

# Working with completion_percentage
mapped_data_1, domain_1, range_1, injective_1, surjective_1 = map_and_check(df, 'completion_percentage')
print("Completion Percentage Mapping:")
print(mapped_data_1)
print(f"Domain: {domain_1}")
print(f"Range: {range_1}")
print(f"Is injective? {injective_1}")
print(f"Is surjective? {surjective_1}")

print("\n")

# Working with age
mapped_data_2, domain_2, range_2, injective_2, surjective_2 = map_and_check(df, 'age')
print("Age Mapping:")
print(mapped_data_2)
print(f"Domain: {domain_2}")
print(f"Range: {range_2}")
print(f"Is injective? {injective_2}")
print(f"Is surjective? {surjective_2}")
