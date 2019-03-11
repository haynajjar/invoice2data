from invoice2data import extract_data
from invoice2data.input import pdftotext, tesseract4, pdfminer_wrapper
import os
import pkg_resources
import logging

# Reduce log level of various modules
logging.getLogger('chardet').setLevel(logging.WARNING)
logging.getLogger('pdfminer').setLevel(logging.WARNING)


def get_sample_files(extension):
    compare_files = []
    for path, subdirs, files in os.walk(pkg_resources.resource_filename(__name__, 'compare')):
        for file in files:
            if file.endswith(extension):
                compare_files.append(os.path.join(path, file))
    return compare_files
#result = extract_data('tests/compare/AmazonWebServices.png')

#res = tesseract.to_text('./tests/compare/AmazonWebServices.png')

png_files = get_sample_files('.pdf')
for file in png_files:
	print(file);
	text=tesseract4.to_text(file,'fra')
    	print(text)
    	break;
