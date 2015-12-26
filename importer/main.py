import os
import argparse
import grequests
from itertools import chain, imap, ifilter
from epubzilla.epubzilla import Epub

def iflatmap(proc, sequence):
    return chain.from_iterable(imap(proc, sequence))

def stitch_directory_and_files(triple):
    d, _, fs = triple
    return imap(lambda f: os.path.join(d, f), fs)
    
def list_all_files(directory):
    return iflatmap(stitch_directory_and_files, os.walk(directory))

def list_all_ebooks(directory):
    sequence = list_all_files(directory)
    return ifilter(lambda path: path.endswith('.epub'), sequence)

def analyze_ebook(path):
    try:
        epub = Epub.from_file(path)
        return (epub.author, epub.title, path)
    except:
        return None

def analyze_all_ebooks(path):
    sequence = list_all_ebooks(path)
    return ifilter(lambda item: item, imap(analyze_ebook, sequence))

def handle_response(response, *args, **kwargs):
    if response.status_code == 400:
        print "Skipping already indexed book"
    else:
        try:
            print response.text
        except:
            print "Failed encoding the response text, ignoring"
    response.close()

def post_ebook(triple):
    author, title, path = triple
    data = {
        'author': author,
        'title': title,
        'path': path
    }
    hooks = {'response': handle_response}
    return grequests.post('http://localhost:8001/api/book/', data=data, 
            hooks=hooks, stream=False)

def index_all_ebooks(path):
    sequence = analyze_all_ebooks(path)
    jobs = imap(post_ebook, sequence)
    return list(grequests.imap(jobs, stream=False, size=8))
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Path to index")
    args = parser.parse_args()
    index_all_ebooks(args.path)

main()
