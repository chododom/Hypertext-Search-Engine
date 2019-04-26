import shutil
import threading
import collections
import time

from hypertext_search_engine.src.domain import *
from hypertext_search_engine.src.search_engine import *
from hypertext_search_engine.src.config import *
from hypertext_search_engine.src.spider import Spider
from hypertext_search_engine.src.page_rank import *

DOMAIN_NAME = get_domain_name(HOMEPAGE)
pages = {}
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
    while len(crawled) < PAGE_CNT:
        if len(queue) != 0:
            url = queue.pop()
            Spider.crawl_page(url)
            time.sleep(0.05)


if CRAWL:
    try:
        shutil.rmtree("../page_contents")
    except:
        print("Page_contents folder couldn't be removed as it doesn't exist")
    os.mkdir("../page_contents")
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

if CALC_PR:
    PR = PageRank(pages, ALPHA, ITERATION_CNT, False)


if CALC_PR and METHOD == "matrix":
    print("Result - matrix method")
    pi_matrix = PR.do_page_rank_matrix()
    for pg in pages:
        pages[pg].rank = pi_matrix.toarray()[0][int(pages[pg].id)]
    # sort by Page Rank
    print("PR sum: "+str(pi_matrix.sum()))
    PageRank.printPagesPR(pages)

if CALC_PR and METHOD == "power":
    print("\nResult - power method")
    pi_power = PR.do_page_rank()
    for pg in pages:
        pages[pg].rank = pi_power.toarray()[0][int(pages[pg].id)]
    # sort by Page Rank
    print("PR sum: "+str(pi_power.sum()))
    PageRank.printPagesPR(pages)

if INIT_SEARCH_INDEX:
    createSearchableData("../page_contents")
    print("Created searchable data schema")

if SEARCH:
    search(SEARCH_WORD, RESULT_CNT)
