import argparse
from urlparse import urlparse

from src import std
from src import scanner
from src.web import search
from src.crawler import Crawler


google = search.Google()
crawler = Crawler()

def initparser():
    global parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", dest="dork", help="SQL injection dork", type=str, metavar="inurl:example")
    parser.add_argument("-e", dest="engine", help="Google", type=str, metavar="google")
    parser.add_argument("-p", dest="page", help="quantidade de sites para realizar a busca", type=int, default=3, metavar="100")


if __name__ == "__main__":
    initparser()
    args = parser.parse_args()

    # Busca SQL INJECTION NA DORK
    if args.dork != None and args.engine != None:
        std.stdout("Procurando sites")
        websites = eval(args.engine).search(args.dork, args.page)
        std.stdout("{} sites encontrados".format(len(websites)))
        vulnerables = scanner.scan(websites)

  
