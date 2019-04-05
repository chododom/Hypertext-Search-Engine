import threading
import collections
import time

from domain import *
from spider import Spider
from page_rank import PageRank


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

# print('\n\nVisited pages: ' + str(len(pages)))
PR = PageRank(pages, 0.85)

print("Result")
pi = PR.do_page_rank()
print(pi.toarray()[0])
for pg in pages:
    pages[pg].rank = pi.toarray()[0][int(pages[pg].id) - 1]
# sort by Page Rank
result = list(pages.values())
result.sort(key=lambda x: x.rank, reverse=True)
for page in result:
    print(page)





