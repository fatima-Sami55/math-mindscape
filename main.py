import importlib
import os
import pandas as pd
def menu():
    while True:
        print("\nChoose an option:")
        print("1. Propositions")
        print("2. Quantifiers")
        print("3. Set Operations")
        print("4. Venn Diagrams")
        print("5. Functions")
        print("6. Relations")
        print("7. Induction")
        print("8. Permutations and Combinations")
        print("9. Counting")
        print("10. Trees")
        print("11. Graphs")
        print("0. Exit")
        
        choice = input("Enter your choice (press Enter to exit): ")

        # If the user presses Enter without a choice, exit the program
        if choice == "":
            print("Exiting program...")
            break
        
        if choice == "0":
            print("Exiting program...")
            break
        
        # Validate choice and dynamically load the corresponding module
        if choice in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]:
            module_name = [
                "propositions", 
                "Quantifiers", 
                "sets", 
                "venn", 
                "functions", 
                "relations", 
                "strong_and_structural", 
                "perm_and_comb", 
                "counting", 
                "trees", 
                "graphs"
            ][int(choice) - 1]
            
            # Dynamically import the corresponding module
            try:
                module = importlib.import_module(module_name)
                print(f"Running module: {module_name}")
                # If you want to call code in the module directly, you can put it here
                # For example, you can execute the module's content like this:
                os.system(f"python {module_name}.py")  # This runs the file as a script
                input("Press Enter to return to the menu...")  # Wait for user input to return to menu
                
            except ModuleNotFoundError:
                print(f"Module {module_name} not found. Please check your file structure.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
