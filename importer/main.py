import os
import re
import argparse
import grequests
from itertools import chain
from epub_meta import get_epub_metadata
from PyPDF2 import PdfFileReader


accepted_formats = ['epub', 'pdf']

def iflatmap(proc, sequence):
    return chain.from_iterable(map(proc, sequence))

def stitch_directory_and_files(quadruple):
    d, _, fs = quadruple
    return map(lambda f: os.path.join(d, f), fs)
    
def list_all_files(directory):
    return iflatmap(stitch_directory_and_files, os.walk(directory))

def get_extension(path):
    return path.split('.')[-1]

def list_all_ebooks(directory):
    sequence = list_all_files(directory)
    return filter(lambda path: get_extension(path) in accepted_formats, sequence)

def get_year_from_date_string(d_str):
    match = re.search('\d{4}', d_str)
    year = match.group(0) if match else None
    return year

def analyze_epub(path):
    try:
        epub_metadata = get_epub_metadata(path)
        date = epub_metadata.get('publication_date')
        year = get_year_from_date_string(date)
        author = epub_metadata['authors'][0]
        title = epub_metadata['title']
        return (author, title, year, path, 'epub')
    except:
        return None

def analyze_pdf(path):
    try:
        with open(path, 'rb') as f:
            metadata = PdfFileReader(f).getDocumentInfo()
            metadata = {re.sub('[^A-Za-z]+', '', k): v for k, v in metadata.items()}
            author = metadata.get('Author')
            title = metadata.get('Title')
            date = metadata.get('CreationDate')
            year = get_year_from_date_string(date)
        return (author, title, year, path, 'pdf')
    except:
        return None

def analyze_ebook(path):
    extension = get_extension(path)
    if extension == 'epub':
        return analyze_epub(path)
    elif extension == 'pdf':
        return analyze_pdf(path)
    else:
        raise RuntimeError("Tried to analyze book with unimplemented extension %s. Accepted formats: %s" % (extension, accepted_formats))

def analyze_all_ebooks(path):
    sequence = list_all_ebooks(path)
    return filter(lambda item: item, map(analyze_ebook, sequence))

def handle_response(response, *args, **kwargs):
    if response.status_code == 400:
        print("Skipping already indexed book")
    else:
        try:
            print(response.text)
        except:
            print("Failed encoding the response text, ignoring")
    response.close()

def post_ebook(quadruple):
    author, title, year, path, extension = quadruple
    data = {
        'author': author,
        'title': title,
        'year': year,
        'path': path,
        'extension': extension
    }
    hooks = {'response': handle_response}
    return grequests.post('http://localhost:8001/api/book/', data=data, 
            hooks=hooks, stream=False)

def index_all_ebooks(path):
    sequence = analyze_all_ebooks(path)
    jobs = map(post_ebook, sequence)
    return list(grequests.imap(jobs, stream=False, size=8))
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Path to index")
    args = parser.parse_args()
    index_all_ebooks(args.path)

main()
