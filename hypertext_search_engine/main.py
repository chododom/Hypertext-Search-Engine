import threading
from queue import Queue
import collections
from domain import *
from spider import Spider

HOMEPAGE = 'https://www.fit.cvut.cz/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
THREAD_CNT = 8
# queue = Queue()  -> synchronized queue for later work with threads
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
    while True:
        url = queue.pop()
        Spider.crawl_page(url)
        # Spider.crawl_page(threading.current_thread().name, url)
        # queue.task_done()


# create_spiders()  -> will be used once multithreaded solution is needed

crawl()