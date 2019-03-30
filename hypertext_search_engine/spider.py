import urllib.request
from link_finder import LinkFinder
import collections

from page import *
from domain import *
from bs4 import BeautifulSoup


class Spider:
    visitedPages = 0
    project_name = ''
    base_url = ''
    domain_name = ''
    queue = collections.deque()
    crawled = set()
    pages = {}

    def __init__(self, base_url, domain_name, queue, crawled, pages):
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue = queue
        Spider.crawled = crawled
        Spider.pages = pages

    @staticmethod
    def crawl_page(page_url):
        # skip pages with names of teachers
        if page_url.find('#') != -1:
            return

        print('Crawling page url: ' + page_url)
        Spider.visitedPages += 1
        print('Visited pages: ' + str(Spider.visitedPages))
        if page_url not in Spider.crawled:
            Spider.enqueue_links(Spider.gather_links(page_url), page_url)
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

            # extract visible text
            soup = BeautifulSoup(html_string, "html.parser")
            for str in soup(['style', 'script', '[document]', 'head', 'title']):
               str.extract() # removes tag

            visible_text = soup.getText()
            outlinks = finder.page_links()

            page = Page(len(Spider.pages), page_url, visible_text, outlinks)
            Spider.pages[page_url] = page
            return outlinks
        except:
            print('Error: could not crawl page')
            return set()

    @staticmethod
    def enqueue_links(links, page_url):
        for url in links:
            if (url in Spider.queue) or (url in Spider.crawled):
                continue
            if Spider.domain_name != get_domain_name(url):
                continue
            Spider.pages[page_url].outlinks.add(url)
            Spider.queue.appendleft(url)
