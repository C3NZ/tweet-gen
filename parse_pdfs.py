from pathlib import Path
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

import os
import sys, getopt

output_file = open('./corpus/corpus.txt', 'a+')

def get_files():
    '''
        Gets all files in that have a pdf extension in the directory provided
        Returns the file paths  of all the pdfs inside of our corpus
    '''
    return Path('./corpus/books').glob('*/*.pdf')

def process_pdf(file_name, pages=None):
    '''
        process a single pdf into a string. Assumes file name is a path to a file
        and pages is the pages that you would like to specifically target
        Returns a string containing the entire pdf stringified
    ''' 
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    pdf_file = open(file_name, 'rb')

    for page in PDFPage.get_pages(pdf_file, pagenums):
        interpreter.process_page(page)

    pdf_file.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text

def clean_text(pdf_text):
    '''
        strips the text of any new line characters that they may have.
        Returns the stripped string
    '''
    new_string = ''
    for line in pdf_text:
        new_string += line.strip('\n')

    return new_string

if __name__ == '__main__':
    for file in get_files():
        try:
            print('Attempting to process {}'.format(file))
            pdf_text = process_pdf(file)
            processed_text = clean_text(pdf_text)
            output_file.write(processed_text)
        except Exception as e:
            print('couldnt open pdf')
            print(e)
    print('done processing text')
    output_file.close()
