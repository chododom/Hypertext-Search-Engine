import threading
import collections
from domain import *
from spider import Spider

HOMEPAGE = 'https://fit.cvut.cz'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
THREAD_CNT = 8
queue = collections.deque()
queue.appendleft(HOMEPAGE)
crawled = set()
Spider(HOMEPAGE, DOMAIN_NAME, queue, crawled)


def create_spiders():
    for x in range(THREAD_CNT):
        thread = threading.Thread(target=crawl)
        thread.daemon = True
        thread.start()


def crawl():
    while True:     # uspat pavouka (milisekunda napr.), pridat omezeni hloubky + poctu stranek
        if len(queue) != 0:
            url = queue.pop()
            Spider.crawl_page(url)


create_spiders()
crawl()