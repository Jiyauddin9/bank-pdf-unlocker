# Bank & Insurance PDF Password Recovery Tool 

A smart, optimized, and fast Python utility script designed to recover lost or forgotten passwords for bank statements, credit card statements, and insurance PDFs (like SBI General, HDFC, ICICI, etc.). 

Most financial institutions use a standardized pattern for PDF passwords (e.g., First 4/5 letters of Name + DDMM or YYYY). This tool automates the process using parallelized pattern matching, saving you from manual guesswork.

##  Features
* *Smart Prefix Generation:* Automatically handles names with spaces, short names (like 'Md'), and extracts both 4 and 5-letter combinations.
* *Leap Year Safe:* Validates and generates correct dates, ensuring tricky dates like February 29th are covered.
* *Optimized Search Order:* Tries faster formats (Name + DDMM / Name + YYYY) first before moving to heavier combinations (Name + DDMMYYYY).
* *Progress Bar:* Uses tqdm to show real-time progress and estimated time.

##  Requirements

Before running the script, make sure you have Python installed and install the required dependencies:

```bash
pip install pikepdf tqdm


How to Use
1. Clone this repository or download the script.
2. Open the script and update the configuration section at the bottom:
if _name_ == "_main_":
    # Path to your password-protected PDF
    pdf_file = r"C:\Users\YourName\Desktop\statement.pdf"

    # Add variations of the name
    name_guesses = ["amit", "raj", "harsh"]

    # Define the birth year range to keep the search fast
    start_birth_year = 1990
    end_birth_year = 2000



3. Run the script:
python crack_pdf.py


Supported Password Formats
The script automatically tests the following combinations:
⚙️ PREFIX + DDMM
⚙️ PREFIX + YYYY
⚙️ PREFIX + DDMMYYYY
🔒 Security & Privacy Notice
Disclaimer: This tool is strictly intended for educational purposes and personal recovery of your own lost passwords. Do not use it for unauthorized access.
Important: Never upload your actual bank statements or hardcode your real password/sensitive details into GitHub. Always use sample paths and generic placeholders before pushing code.
📄 License
This project is open-source and available under the MIT License.



