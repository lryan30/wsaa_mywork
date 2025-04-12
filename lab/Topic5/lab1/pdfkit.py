# This script converts a webpage to a PDF file using pdfkit and wkhtmltopdf. 
#  pdfkit is a Python wrapper for wkhtmltopdf, which is a command-line tool that converts HTML to PDF using the WebKit rendering engine.
#  The script specifies the path to the wkhtmltopdf executable, sets the target URL to be converted, and saves the resulting PDF file with a specified name.
#  No API jey needed, just file location for wkhtmltopdf.exe
import pdfkit


path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'  # where the file is stored

config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf) 

# The URL of the webpage you want to convert to PDF
targeturl = 'https://en.wikipedia.org/wiki/Python_(programming_language)'

# Convert the webpage to a PDF and save it with the name "wikipedia_page_python.pdf"
pdfkit.from_url(targeturl, 'wikipedia_page_python.pdf', configuration=config)

print("PDF saved")


# 