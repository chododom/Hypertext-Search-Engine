import threading
import collections
import time

from hypertext_search_engine.src.domain import *
from hypertext_search_engine.src.spider import Spider
from hypertext_search_engine.src.page_rank import PageRank

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
    while len(crawled) < 1000:
        if len(queue) != 0:
            url = queue.pop()
            Spider.crawl_page(url)
            time.sleep(0.05)


create_spiders()

crawl()

for thread in threads:
    thread.join()
    '''
pages = {
        "1": Page(id=0, page_url="1", text_content='', outlinks=["2", "3"]),
        "2": Page(id=1, page_url="2", text_content='', outlinks=[]),
        "3": Page(id=2, page_url="3", text_content='', outlinks=["1", "2", "5"]),
        "4": Page(id=3, page_url="4", text_content='', outlinks=["5", "6"]),
        "5": Page(id=4, page_url="5", text_content='', outlinks=["4", "6"]),
        "6": Page(id=5, page_url="6", text_content='', outlinks=["4"])
    }
'''
# print('\n\nVisited pages: ' + str(len(pages)))
PR = PageRank(pages, 0.85, 50, False)


def printPagesPR(pgs):
    res = list(pgs.values())
    res.sort(key=lambda x: x.rank, reverse=True)
    for pg in res:
        print(pg)


print("Result - matrix method")
pi_matrix = PR.do_page_rank_matrix()

for pg in pages:
    pages[pg].rank = pi_matrix.toarray()[0][int(pages[pg].id)]
# sort by Page Rank
print("PR sum: "+str(pi_matrix.sum()))
printPagesPR(pages)

print("\nResult - power method")
pi_power = PR.do_page_rank()
for pg in pages:
    pages[pg].rank = pi_power.toarray()[0][int(pages[pg].id)]
# sort by Page Rank
print("PR sum: "+str(pi_power.sum()))
printPagesPR(pages)



