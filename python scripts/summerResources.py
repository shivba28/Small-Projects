import os
import pymupdf  # PyMuPDF
from pathlib import Path

def save_first_page_as_image(pdf_dir, output_dir, image_format="png"):
    pdf_dir = Path(pdf_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    for pdf_file in pdf_dir.rglob("*.pdf"):  # Recursive search
        try:
            doc = pymupdf.open(pdf_file)
            if doc.page_count < 1:
                print(f"Skipping {pdf_file.name}: No pages found.")
                continue

            page = doc.load_page(0)
            pix = page.get_pixmap(dpi=200)

            # Create relative path to preserve folder structure
            relative_path = pdf_file.relative_to(pdf_dir).with_suffix(f".{image_format}")
            image_path = output_dir / relative_path
            image_path.parent.mkdir(parents=True, exist_ok=True)

            pix.save(str(image_path))
            print(f"Saved: {image_path}")
        except Exception as e:
            print(f"Failed to process {pdf_file}: {e}")

# Example usage:
pdf_directory = "/Users/techsupport/Desktop/summer resources/"
output_directory = "/Users/techsupport/Desktop/Output"
save_first_page_as_image(pdf_directory, output_directory)

