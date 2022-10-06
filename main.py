# extract_doc_info.py
import PyPDF2
import re
import unidecode

from tabula import read_pdf
from tabulate import tabulate
import camelot
import pandas as pd
import io


def extract_information(pdf_path):

    # pypdf2 to read pdf
    file = open(pdf_path, 'rb')
    reader = PyPDF2.PdfFileReader(file)
    # active_page = reader.getPage(0)
    # data = active_page.extractText()
    # data = unidecode.unidecode(data)
    # result = dict(re.findall(r'(?=\S|^)(.+?): (\S+)', data))

    import pdb;pdb.set_trace()
    # tabulate to read table from pdf..this is main code
    get_page_count = reader.numPages
    for active_page in range(get_page_count):
        pg = active_page+1
        tables = read_pdf(pdf_path, pages=active_page+1, multiple_tables=True, stream=True)
        if tables:
            df = tables[0]
            output = df.to_json()
            print(output)


if __name__ == '__main__':
    path = 'policy_0177702959.pdf'
    extract_information(path)
