# Define the file path
file_path = 'train.py'

# Read the file
with open(file_path, 'r') as file:
    content = file.read()

# Replace the occurrences
new_content = content.replace('experiments/parameters_dgrcl.yaml', 'parameters_dgrcl.yaml')

# Write the changes back to the file
with open(file_path, 'w') as file:
    file.write(new_content)

print("Replacements done.")
