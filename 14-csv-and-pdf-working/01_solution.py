import csv
from os import getcwd

'''
Task One: Use Python to extract the Google Drive link from the .csv file. (Hint: Its along the diagonal from top left to bottom right).
Task Two: Download the PDF from the Google Drive link (we already downloaded it for you just in case you can't download from Google Drive) and find the phone number that is in the document. Note: There are different ways of formatting a phone number!
'''

# Task One
csv_path = getcwd()+'/14-csv-and-pdf-working/files/'+'find_the_link.csv'
print(csv_path)
f = open(csv_path, 'r')
csv_data = csv.reader(f)
data_lines = list(csv_data)

link = ''
for num in range(len(data_lines)):
    link += data_lines[num][num]


print(link)

# Task Two
import PyPDF2
import re
pdf_path = getcwd()+'/14-csv-and-pdf-working/files/'+'Find_the_Phone_Number.pdf'
print(pdf_path)
f = open(pdf_path,'rb')
pdf_reader = PyPDF2.PdfFileReader(f)

phone_numbers = set()
for index in range(pdf_reader.numPages):
    page = pdf_reader.getPage(index)
    page_text = page.extractText()
    match = re.search('\d{3}.\d{3}.\d{4}', page_text)
    if match:
        phone_numbers.add(match.group())
print(list(phone_numbers)) # ['505.503.4455']
f.close()

