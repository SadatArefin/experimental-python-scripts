import PyPDF2
import pyttsx3

def read_pdf_aloud(pdf_path, page_number):
    # Initialize the PDF reader
    pdf_reader = PyPDF2.PdfReader(open(pdf_path, 'rb'))
    
    # Check if the page number is valid
    if page_number < 0 or page_number >= len(pdf_reader.pages):
        print(f"Invalid page number: {page_number}. The PDF has {len(pdf_reader.pages)} pages.")
        return
    
    # Extract text from the specified page
    page = pdf_reader.pages[page_number]
    text = page.extract_text()
    
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    
    # Read the text aloud
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    pdf_path = "data-jujitsu.pdf"  # Replace with your PDF file name
    page_number = 16  # Replace with the page number you want to read
    
    read_pdf_aloud(pdf_path, page_number)