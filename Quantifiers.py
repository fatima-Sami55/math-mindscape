from main import pd

# Load the data assuming the file is named 'soc-pokec-profiles.txt' and columns are separated by tab spaces
def load_data(filename):
    df = pd.read_csv(filename, sep='\t', header=None, nrows=100)
    df = df[[2, 4, 7]]  # Select relevant columns (completion_percentage, region, age)
    df.columns = ['completion_percentage', 'region', 'age']
    df['completion_percentage'] = pd.to_numeric(df['completion_percentage'], errors='coerce')
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    return df

# Function to handle Criteria 1
def criteria_1(df):
    # Filter users in the "Zilinsky kraj" region who are above 25 and have a completion percentage above 70
    filtered_users = df[(df['region'].str.contains('zilinsky kraj', case=False)) & 
                        (df['age'] > 25) & 
                        (df['completion_percentage'] > 70)]

    if not filtered_users.empty:
        print("\n" + "="*50)
        print(" **Criteria 1: Users from 'Zilinsky kraj' who are above 25 and have a completion percentage above 70** ")
        print("="*50)
        for index, row in filtered_users.iterrows():
            print(f"User {index}:")
            print(f"  Region             : {row['region']}")
            print(f"  Age                : {row['age']}")
            print(f"  Completion Percentage: {row['completion_percentage']}")
    else:
        print("\n**Criteria 1: No users satisfy the condition in 'Zilinsky kraj'.**")

# Function to handle Criteria 2
def criteria_2(df):
    # Filter users above 18 years old
    above_18 = df[df['age'] > 18]

    valid_regions = []

    # Group by region and check the condition for each region
    for region, group in above_18.groupby('region'):
        # Check if all users in this region (above 18) have a completion percentage of at least 50%
        if (group['completion_percentage'] >= 50).all():
            valid_regions.append(region)

    # Check if there are any regions that satisfy the condition
    if valid_regions:
        print("\n" + "="*50)
        print("** Criteria 2: The following regions satisfy the condition where every user above 18 has completed at least 50% of their profile **")
        print("="*50)
        
        for region in valid_regions:
            print(f"  - {region}")
            print("-" * 50)
    else:
        print("\n**Criteria 2: No regions satisfy the condition.**")

# Main execution block
if __name__ == "__main__":
    # Load the dataset
    df = load_data('soc-pokec-profiles.txt')

    # Handle Criteria 1
    criteria_1(df)

    # Handle Criteria 2
    criteria_2(df)
