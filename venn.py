from main import pd
import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# Load the dataset (use only the first 1000 rows for simplicity)
file_path = 'soc-pokec-profiles.txt'  # Replace with the correct path
data = pd.read_csv(file_path, delimiter='\t', engine='python', nrows=1000)

# Clean and preprocess the dataset
data.iloc[:, 1] = data.iloc[:, 1].astype(str).str.strip().astype(int)  # Convert 'public' to integers
data.iloc[:, 3] = data.iloc[:, 3].astype(str).str.strip().astype(int)  # Convert 'gender' to integers

# Define sets based on conditions
set_public = set(data[data.iloc[:, 1] == 1].iloc[:, 0])  # Public users (public = 1)
set_above_30 = set(data[data.iloc[:, 7] > 20].iloc[:, 0])  # Users above age 30
set_female = set(data[data.iloc[:, 3] == 0].iloc[:, 0])  # Female users (gender = 0)

# Create Venn diagram
venn3(
    subsets=(set_public, set_above_30, set_female),
    set_labels=("Public Users", "Age > 20", "Female Users")
)

# Add title and show the plot
plt.title("Venn Diagram of User Overlaps")
plt.show()
