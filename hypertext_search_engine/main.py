import threading
import collections
from domain import *
from spider import Spider
import time

HOMEPAGE = 'https://fit.cvut.cz'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
THREAD_CNT = 10
threads = set()
queue = collections.deque()
queue.appendleft(HOMEPAGE)
crawled = set()
Spider(HOMEPAGE, DOMAIN_NAME, queue, crawled)


def create_spiders():
    for x in range(THREAD_CNT):
        thread = threading.Thread(target=crawl)
        threads.add(thread)
        thread.daemon = True
        thread.start()


def crawl():
    while len(queue) < 1000:
        if len(queue) != 0:
            url = queue.pop()
            Spider.crawl_page(url)
            time.sleep(0.1)

create_spiders()
crawl()