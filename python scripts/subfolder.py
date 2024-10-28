import os
import shutil

def consolidate_media_files(source_folder, destination_folder):
    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    # Loop through each subfolder in the source directory
    for root, dirs, files in os.walk(source_folder):
        # Skip the top-level source directory itself
        if root == source_folder:
            continue

        # Copy each file from the subfolder to the destination folder
        for file in files:
            src_file_path = os.path.join(root, file)
            dest_file_path = os.path.join(destination_folder, file)

            # If a file with the same name already exists in the destination, append a number to make it unique
            counter = 1
            while os.path.exists(dest_file_path):
                file_name, file_ext = os.path.splitext(file)
                dest_file_path = os.path.join(destination_folder, f"{file_name}_{counter}{file_ext}")
                counter += 1

            shutil.copy2(src_file_path, dest_file_path)
            print(f"Copied {src_file_path} to {dest_file_path}")

    print("All files have been consolidated into the destination folder.")

# Example usage
source_folder = "/Users/techsupport/Desktop/Board Policies/media"  # Replace with the path to your media folder
destination_folder = "/Users/techsupport/Desktop/Board Policies/Policies-Together"  # Replace with the desired output folder
consolidate_media_files(source_folder, destination_folder)