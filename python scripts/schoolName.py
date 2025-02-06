import os
import re
import pymupdf  # PyMuPDF

# List of school names in GGUSD
school_names = [
    "Ethan Allen Elementary", "Anthony Elementary", "Barker Elementary", "Brookhurst Elementary",
    "Bryant Elementary", "Carrillo Elementary", "Carver Early Childhood Education", "Clinton Elementary",
    "Clinton Corner Family Campus", "Cook Elementary", "Crosby Elementary", "Eisenhower Elementary",
    "Enders Elementary", "Evans Elementary", "Excelsior Elementary", "Faylane Elementary",
    "Garden Park Elementary", "Gilbert Elementary", "Hazard Elementary", "Heritage Elementary Computer Science Immersion Academy",
    "Merton E. Hill Elementary", "Lawrence Elementary", "Marshall Elementary", "Mitchell Elementary",
    "Monroe Elementary Language Academy", "Morningside Elementary", "Murdy Elementary",
    "Newhope Elementary", "Northcutt Elementary", "Paine Elementary", "Parkview Elementary",
    "Patton Elementary", "Peters K-3 Elementary", "Peters 4-6 Elementary", "Post Elementary",
    "Riverdale Elementary", "Rosita Elementary", "Russell Elementary Language Academy",
    "Simmons Elementary", "Skylark Preschool", "Stanford Elementary", "Stanley Elementary",
    "Sunnyside Elementary", "Violette Elementary", "Wakeham Elementary", "Warren Elementary",
    "Woodbury Elementary", "Zeyen Elementary", "Alamitos Intermediate", "Bell Intermediate",
    "Doig Intermediate", "Fitz Intermediate Computer Science Academy", "Irvine Intermediate",
    "Jordan Intermediate", "Lake Intermediate", "McGarvin Intermediate", "Ralston Intermediate",
    "Walton Intermediate", "Bolsa Grande High School", "Garden Grove High School",
    "Hare Continuation High School", "La Quinta High School", "Los Amigos High School",
    "Pacifica High School", "Rancho Alamitos High School", "Santiago High School",
    "The Adult Transition Program at Jordan", "Special Education Center at Mark Twain",
    "CTE", "LEC Adult Education"
]

# Directory containing the PDF files
directory = "/Users/techsupport/Desktop/pdfs"
output = "/Users/techsupport/Desktop/school_output"

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    try:
        with pymupdf.open(pdf_path) as doc:
            text = ""
            for page in doc:
                text += page.get_text("text")  # Extract text from each page
        return text
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return ""

# Iterate over all files in the directory
for filename in os.listdir(directory):
    if filename.lower().endswith(".pdf"):  # Ensure we are working with PDF files
        pdf_path = os.path.join(directory, filename)
        text = extract_text_from_pdf(pdf_path)

        for school in school_names:
            # Check if the school name appears in the PDF content (case-insensitive)
            if re.search(re.escape(school), text, re.IGNORECASE):
                new_filename = f"{school} Bell Schedule.pdf"
                new_path = os.path.join(output, new_filename)
                
                # Rename the file
                try:
                    os.rename(pdf_path, new_path)
                    print(f"Renamed: {filename} -> {new_filename}")
                except Exception as e:
                    print(f"Error renaming {filename}: {e}")
                break  # Stop checking once a match is found
