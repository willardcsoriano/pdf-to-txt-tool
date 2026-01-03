# PDF to Text Converter

A lightweight Python utility to extract text from PDF files and save them as `.txt` files. This tool uses `PyPDF2` and is designed to be used via the command line.

## Features
* **Simple CLI:** Convert any PDF by passing the filename as an argument.
* **UTF-8 Support:** Handles special characters and symbols common in academic handbooks and reports.
* **Efficient:** Uses memory-efficient string joining for large documents.

## Prerequisites
* Python 3.x
* A terminal (PowerShell, Bash, or CMD)

## Installation

1. **Clone the repository:**
   ```powershell
   git clone [https://github.com/willardcsoriano/pdf-to-txt-tool.git](https://github.com/willardcsoriano/pdf-to-txt-tool.git)
   cd pdf-to-txt-tool

```

2. **Set up Virtual Environment:**
```powershell
python -m venv venv
# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1

```


3. **Install Dependencies:**
```powershell
pip install -r requirements.txt

```



## Usage

Place the PDF you want to convert into the project folder, then run:

```powershell
python converter.py your-filename.pdf

```

The script will generate a file named `your-filename.txt` in the same directory.

## File Structure

* `converter.py`: The main logic for PDF extraction.
* `requirements.txt`: List of necessary Python packages.
* `.gitignore`: Prevents virtual environments and large PDF/TXT files from being uploaded to GitHub.

## License

MIT License - feel free to use and modify!
