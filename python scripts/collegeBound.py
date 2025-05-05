import os

# Set this to your base directory path where school folders are
BASE_DIR = '/Users/techsupport/Downloads/CollegeBoundIn/'
BASE_URL = 'https://ggusd.us/assets/images/collegesigning/2025'

output_lines = []
output_lines.append('var Photos = new[] {\n')

for root, dirs, files in os.walk(BASE_DIR):
    for file in files:
        if file.lower().endswith(('.jpg', '.jpeg', '.png')):
            relative_path = os.path.relpath(root, BASE_DIR)
            school_name = relative_path.lower().replace(' ', '')
            url = f'{BASE_URL}/{school_name}/{file}'
            output_lines.append(f'    new {{ Photo = "{url}", School = "{school_name}" }},')

# Remove the last comma for valid syntax
if output_lines[-1].endswith(','):
    output_lines[-1] = output_lines[-1].rstrip(',')

output_lines.append('\n}')

# Write to file
with open('image_titles.txt', 'w') as f:
    f.write('\n'.join(output_lines))

print("image_titles.txt generated successfully.")