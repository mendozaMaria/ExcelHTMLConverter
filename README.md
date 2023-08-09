# ExcelHTMLConverter
# CSV to HTML Converter

This Python script is designed to convert a single CSV (Comma-Separated Values) file into an HTML (Hypertext Markup Language) file. It reads the data from the CSV file, converts it into an HTML table, and saves the resulting HTML to an output file.

## How to Use

1. **Prerequisites:** Make sure you have Python and the required libraries installed. The script uses the `os` module for file handling, `pandas` (imported as `pd`) for data manipulation, and `sys` for system-related information.

2. **CSV File Preparation:** Place the CSV file you want to convert in the same directory as this script.

3. **Running the Script:** Open a terminal or command prompt and navigate to the directory containing the script. Run the script using the following command:

    ```
    python script_name.py
    ```

    Replace `script_name.py` with the actual name of the Python script file.

4. **Output:** After running the script, an HTML file named `output.html` will be created in the same directory. This HTML file will contain the data from the CSV file in the form of an HTML table.

## Script Explanation

1. **Importing Libraries:** The necessary libraries are imported at the beginning of the script.

2. **Current Directory:** The path of the current directory is obtained using `sys.executable`. This is the directory where the script is being executed.

3. **CSV File Detection:** The script looks for files with a `.csv` extension in the current directory using a list comprehension. If there is not exactly one CSV file present, a `ValueError` is raised.

4. **Loading CSV Data:** The path of the CSV file is constructed using the first CSV file found in the directory. The data is loaded from the CSV file into a Pandas DataFrame using `pd.read_csv()`.

5. **Data to HTML Conversion:** The data in the DataFrame is converted into an HTML table using the `to_html()` method. The parameter `index=False` ensures that the DataFrame index is not included in the HTML table.

6. **Saving HTML Output:** The HTML content is saved to an output file named `output.html` in the current directory. This is done by opening the file in write mode and using the `write()` method.

7. **Completion Message:** After the HTML file is created, a message is printed to the console indicating that the HTML file has been successfully generated.

## Note

- This script assumes that there is only one CSV file in the current directory and that you want to convert its data into an HTML table.

- Make sure to review the generated `output.html` file in a web browser to verify the appearance and correctness of the HTML table.

- You can customize the script to handle different scenarios, such as processing multiple CSV files or modifying the output file name and format.
