# Import pandas library
import pandas as pd

# Define the function to merge employee and timekeeper data
def merge_employee_and_timekeeper_data(file_path, output_file):
    # Load the employee and timekeeper data into DataFrames using pandas
    employee_df = pd.read_excel(file_path, sheet_name="Employee Data")
    timekeeper_df = pd.read_excel(file_path, sheet_name="Timekeeper Data")
    
    # Display the first few rows of both DataFrames to inspect
    print("Employee Data:")
    print(employee_df.head())
    
    print("Timekeeper Data:")
    print(timekeeper_df.head())

    print("Employee Data Columns:", employee_df.columns)
    print("Timekeeper Data Columns:", timekeeper_df.columns)
    
    # Merge employee data with timekeeper data on "Location Code"
    merged_df = pd.merge(employee_df, timekeeper_df, on="Location Code", how="left")
    
    # Display the first few rows of the merged DataFrame
    print("Merged Data:")
    print(merged_df.head())
    
    # Save the merged data to a new Excel file (using Pandas, no openpyxl)
    merged_df.to_excel(output_file, sheet_name="Merged Data", index=False)
    
    print(f"Merged data saved to '{output_file}'.")

# Specify the path to the input Excel file and output Excel file
input_file = "/Users/techsupport/Downloads/dataset.xlsx"  # Replace with your actual file path
output_file = "/Users/techsupport/Downloads/merged_output.xlsx"   # The output file path

# Call the function to merge the data
merge_employee_and_timekeeper_data(input_file, output_file)