import re
from urlparse import urlparse

#import std
from nyawc.Options import Options
from nyawc.QueueItem import QueueItem
from nyawc.Crawler import Crawler as nyawcCrawler
from nyawc.CrawlerActions import CrawlerActions
from nyawc.http.Request import Request


class Crawler:
    def __init__(self):
        self.links = []
        self.crawler = None
        self.setoptions()

    def crawl(self, url):
        parsedurl = urlparse(url)
        domain = parsedurl.scheme + "://" + parsedurl.netloc

        self.links = []
        self.crawler.start_with(Request(domain))
        return self.links

    def setoptions(self, depth=1):
        """Definir o quanto o usuário deseja rastrear"""

        options = Options()
        options.scope.max_depth = depth
        options.callbacks.crawler_before_start = self.crawlerstart
        options.callbacks.crawler_after_finish = self.crawlerfinish
        options.callbacks.request_before_start = self.requeststart
        options.callbacks.request_after_finish = self.requestfinish

        self.crawler = nyawcCrawler(options)

    def crawlerstart(self):
        # Chamado antes de o rastreador começar a rastrear. O padrão é uma rota nula.
        pass

    def crawlerfinish(self, queue):
        # Chamado depois que o rastreador terminou de rastrear. O padrão é uma rota nula.
        pass

    def requeststart(self, queue, queue_item):
        # Chamado antes de o rastreador iniciar uma nova solicitação. O padrão é uma rota nula.
        return CrawlerActions.DO_CONTINUE_CRAWLING

    def requestfinish(self, queue, queue_item, new_queue_items):
        # Chamado depois que o rastreador conclui uma solicitação. O padrão é uma rota nula.
        url = queue_item.request.url
        if re.search('(.*?)(.php\?|.asp\?|.apsx\?|.jsp\?)(.*?)=(.*?)', url):
            if not url in self.links:
                self.links.append(url)
        return CrawlerActions.DO_CONTINUE_CRAWLING
