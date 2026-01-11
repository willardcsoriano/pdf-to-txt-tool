import sys
import os
import re
from PyPDF2 import PdfReader


def clean_text(text: str) -> str:
    """
    Cleans extracted PDF text for RAG usage.
    """
    # Remove non-printable / control characters
    text = re.sub(r"[^\x09\x0A\x0D\x20-\x7E]", " ", text)

    # Remove repeated whitespace
    text = re.sub(r"\s+", " ", text)

    # Remove very common calendar / table noise patterns
    noise_patterns = [
        r"\bS M T W TH F S\b",
        r"\bJANUARY\b|\bFEBRUARY\b|\bMARCH\b|\bAPRIL\b|\bMAY\b|\bJUNE\b|\bJULY\b|\bAUGUST\b|\bSEPTEMBER\b|\bOCTOBER\b|\bNOVEMBER\b|\bDECEMBER\b",
        r"\b\d{4}\b",  # years
    ]

    for pattern in noise_patterns:
        text = re.sub(pattern, "", text, flags=re.IGNORECASE)

    return text.strip()


def convert_pdf_to_txt(input_pdf, max_pages=20):
    if not os.path.exists(input_pdf):
        print(f"Error: File '{input_pdf}' not found.")
        return

    output_txt = os.path.splitext(input_pdf)[0] + ".txt"

    print(f"Converting '{input_pdf}' (first {max_pages} pages)...")

    try:
        reader = PdfReader(input_pdf)
        cleaned_pages = []

        for i, page in enumerate(reader.pages):
            if i >= max_pages:
                break

            raw_text = page.extract_text()
            if not raw_text:
                continue

            cleaned = clean_text(raw_text)

            # Skip pages that are still mostly garbage
            if len(cleaned) < 300:
                continue

            cleaned_pages.append(cleaned)

        with open(output_txt, "w", encoding="utf-8") as f:
            f.write("\n\n".join(cleaned_pages))

        print(f"Success! Clean RAG-ready text saved to: {output_txt}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python converter.py <filename.pdf>")
    else:
        convert_pdf_to_txt(sys.argv[1])
