import os
import pandas as pd
import sys

# Get the path of the current directory
current_directory = os.path.dirname(sys.executable)

# Look for CSV files in the current directory
csv_files = [file for file in os.listdir(current_directory) if file.endswith('.csv')]

# Check if there is exactly one CSV file
if len(csv_files) != 1:
    raise ValueError("There should be exactly one CSV file in the directory.")

# Load the CSV file
csv_file_path = os.path.join(current_directory, csv_files[0])
data = pd.read_csv(csv_file_path)

# Convert the data to HTML
html = data.to_html(index=False)

# Save the HTML to a file
output_file_path = os.path.join(current_directory, 'output.html')
with open(output_file_path, 'w') as file:
    file.write(html)

print("HTML file created: output.html")

