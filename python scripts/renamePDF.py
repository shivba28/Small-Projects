import os
import shutil

def process_pdfs(input_folder, output_folder):
    # Check if the input folder exists
    if not os.path.exists(input_folder):
        print(f"The input folder path {input_folder} does not exist.")
        return

    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through all files in the input folder
    for file_name in os.listdir(input_folder):
        # Check if the file is a PDF
        if file_name.endswith('.pdf'):
            # Extract the school name
            parts = file_name.split('_')
            if len(parts) > 2:
                school_name = parts[-1]

                # Remove trailing designators (e.g., IS, HS, ES) if present
                # Check for a second part in the school name and handle designators
                name_parts = school_name.split()
                if name_parts[1] not in ["HS", "IS", "ES", "IS.pdf", "HS.pdf", "ES.pdf"]:
                    school_name = f"{name_parts[0]}-{name_parts[1]}"
                else:
                    school_name = name_parts[0]

                school_name = school_name.lower()
                
                # Generate the new file name
                new_file_name = f"{school_name}-english.pdf"
                
                # Define file paths
                original_file_path = os.path.join(input_folder, file_name)
                new_file_path = os.path.join(output_folder, new_file_name)

                # Copy the file with the new name
                shutil.copy2(original_file_path, new_file_path)
                print(f"Copied and renamed: {file_name} -> {new_file_name}")

if __name__ == "__main__":
    # Specify the input and output folders
    input_folder = "/Users/techsupport/Desktop/All_English/"
    output_folder = "/Users/techsupport/Desktop/Output/"
    process_pdfs(input_folder, output_folder)