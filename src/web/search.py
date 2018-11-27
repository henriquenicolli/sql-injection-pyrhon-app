# search vulnerabilities by dock

import sys
from urllib2 import HTTPError, URLError


from lib import google

class Search:
    """basic search class that can be inherited by other search agents like Google, Yandex"""
    pass

class Google(Search):
    def search(self, query, pages=10):
        """search and return an array of urls"""

        urls = []

        try:
            for url in google.search(query, start=0, stop=pages):
                urls.append(url)
        except HTTPError:
            exit("[503] Service Unreachable")
        except URLError:
            exit("[504] Gateway Timeout")
        except:
            exit("Unknown error occurred")
        else:
            return urls


