import pdfkit
import os
html_filename = f"{os.path.dirname(__file__)}\\stackoverflow.html"
pdf_filename= f"{os.path.dirname(__file__)}\\output_stackoverflow.pdf"
# Download wkhtmltopdf (zip executable file) from https://wkhtmltopdf.org/downloads.html
# Set the path to the wkhtmltopdf executable
wkhtmltopdf_path = r'C:\Program Files\wkhtmltox\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)
# pdfkit.from_file(html_filename,pdf_filename,configuration=config)

if not os.path.exists(html_filename):
    print(f"HTML file {html_filename} does not exists")
else:
    try:
        # conver file to pdf
        pdfkit.from_file(html_filename,pdf_filename,configuration=config,options={"enable-local-file-access": ""})
        print(f"Html succesfully converted to: {pdf_filename}")
    except Exception as e:
        print(f"an error as occured: {e}")
    