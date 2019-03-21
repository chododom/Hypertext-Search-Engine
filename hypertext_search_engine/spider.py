import urllib.request
from link_finder import LinkFinder
from queue import Queue
import collections
from domain import *


class Spider:
    visitedPages = 0
    project_name = ''
    base_url = ''
    domain_name = ''
    queue = collections.deque()
    crawled = set()

    def __init__(self, base_url, domain_name, queue, crawled):
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue = queue
        Spider.crawled = crawled

    @staticmethod
    def crawl_page(page_url):
        print('Crawling page url: ' + page_url)
        Spider.visitedPages += 1
        print('Visited pages: ' + str(Spider.visitedPages))
        if page_url not in Spider.crawled:
            Spider.enqueue_links(Spider.gather_links(page_url))
            print('queue size: ' + str(len(Spider.queue)))
            Spider.crawled.add(page_url)

    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:
            response = urllib.request.urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)
        except:
            print('Error: could not crawl page')
            return set()
        return finder.page_links()

    @staticmethod
    def enqueue_links(links):
        for url in links:
            if (url in Spider.queue) or (url in Spider.crawled):
                continue
            if Spider.domain_name != get_domain_name(url):
                continue
            Spider.queue.appendleft(url)
