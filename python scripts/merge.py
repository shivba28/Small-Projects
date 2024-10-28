import os
import pymupdf # PyMuPDF

def merge_pdfs(source_folder, output_pdf):
    # Initialize a new PDF file
    merged_pdf = pymupdf.open()

    # List and sort all PDF files in the source folder
    pdf_files = [f for f in os.listdir(source_folder) if f.endswith('.pdf')]
    pdf_files.sort()

    # Loop through each PDF file and add it to the merged PDF
    for pdf_file in pdf_files:
        pdf_path = os.path.join(source_folder, pdf_file)
        current_pdf = pymupdf.open(pdf_path)
        
        # Append each page from the current PDF
        merged_pdf.insert_pdf(current_pdf)
        print(f"Added {pdf_path} to the merged PDF")
        
        # Close the current PDF file
        current_pdf.close()

    # Write the merged PDF to the output file
    merged_pdf.save(output_pdf)
    merged_pdf.close()
    print(f"Merged PDF saved as {output_pdf}")

# Example usage
source_folder = "/Users/techsupport/Desktop/Board Policies/Policies-Together"  # Replace with the path to your destination folder
output_pdf = "/Users/techsupport/Desktop/Board Policies/merged_document.pdf"  # Replace with the desired output file path
merge_pdfs(source_folder, output_pdf)
