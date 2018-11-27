import sys
from urllib2 import HTTPError, URLError


from lib import google

class Search:

    pass

class Google(Search):
    def search(self, query, pages):
        urls = []   
        for url in google.search(query, start=0, stop=pages):
        	urls.append(url)
        
        return urls


