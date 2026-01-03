import sys
import os
from PyPDF2 import PdfReader

def convert_pdf_to_txt(input_pdf):
    # Check if file exists
    if not os.path.exists(input_pdf):
        print(f"Error: File '{input_pdf}' not found.")
        return

    # Create output filename (e.g., "document.pdf" -> "document.txt")
    output_txt = os.path.splitext(input_pdf)[0] + ".txt"
    
    print(f"Converting {input_pdf}...")
    
    try:
        reader = PdfReader(input_pdf)
        text_content = []

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text_content.append(page_text)

        with open(output_txt, "w", encoding="utf-8") as f:
            f.write("\n".join(text_content))
            
        print(f"Success! Created: {output_txt}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python converter.py <filename.pdf>")
    else:
        convert_pdf_to_txt(sys.argv[1])