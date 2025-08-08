 # Create an empty __init__.py file inside the app/api/ directory
import os
# Define the directory path
directory_path = "app/api"
# Ensure the directory exists
os.makedirs(directory_path, exist_ok=True)
# Create the empty __init__.py file
init_file_path = os.path.join(directory_path, "__init__.py")
with open(init_file_path, "w") as f:
    pass
print(f"Empty __init__.py file created at {init_file_path}")



