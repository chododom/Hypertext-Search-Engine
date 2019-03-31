import threading
import collections
import time

from .domain import *
from .spider import Spider
from .page_rank import PageRank
from .google_matrix import GoogleMatrix


HOMEPAGE = 'https://fit.cvut.cz'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
pages = {}
pages_lock = threading.RLock()
THREAD_CNT = 30
threads = set()
queue = collections.deque()
queue.appendleft(HOMEPAGE)
crawled = set()
Spider(HOMEPAGE, DOMAIN_NAME, queue, crawled, pages)


def create_spiders():
    for x in range(THREAD_CNT):
        thread = threading.Thread(target=crawl)
        threads.add(thread)
        thread.daemon = True
        thread.start()


def crawl():
    while len(crawled) < 10:
        if len(queue) != 0:
            url = queue.pop()
            Spider.crawl_page(url)
            time.sleep(0.05)


create_spiders()

crawl()

for thread in threads:
    thread.join()

PR = PageRank(pages)
PR.create_matrix()

GM = GoogleMatrix(pages, 0.85)
print(str(GM))
# for page in pages:
#    print(str(page.id) + ": " + page.page_url)





