
import argparse
from urlparse import urlparse
from src import std
from src import scanner
from src.web import search

google = search.Google()


def initparser():
    global parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", dest="dork", type=str, metavar="inurl:example")
    parser.add_argument("-p", dest="page",default=10, metavar="100")



if __name__ == "__main__":
    initparser()
    args = parser.parse_args()

    # Busca SQL INJECTION NA DORK
    if args.dork != None:
        std.stdout("Procurando sites")
        websites = eval("google").search(args.dork, args.page)
        std.stdout("{} sites encontrados".format(len(websites)))
        vulnerables = scanner.scan(websites)

  
