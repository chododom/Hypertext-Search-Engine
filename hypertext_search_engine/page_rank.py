class PageRank:
    pages = {}
    pages_cnt = 0
    matrix = {}

    def __init__(self, pages):
        self.pages = pages
        self.pages_cnt = len(pages)

        # init all page ranks to 1/n
        for url in self.pages:
            pages[url].rank = 1 / self.pages_cnt

    def create_matrix(self):
        print('Creating matrix...')

        for url in self.pages:
            for link in self.pages[url].outlinks:
                if link in self.pages.keys():
                    self.matrix[self.pages[link].page_url][url] = self.pages[url].rank

    # def iterative_formula_calculation(self):
