from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileMerger
from PyPDF2 import PdfFileWriter

with open('2018-06_RenewalClient[13079].pdf', 'rb') as file_input, \
        open('sample.txt', 'w') as text_file:

    read_pdf = PdfFileReader(file_input, strict=False)

    number_of_pages = read_pdf.getNumPages()
    for page_number in range(number_of_pages):   # use xrange in Py2
        page_content = read_pdf.getPage(page_number).extractText()
        new_content = ''.join([i if ord(i) < 128 else ' ' for i in page_content])

        text_file.write(new_content)
