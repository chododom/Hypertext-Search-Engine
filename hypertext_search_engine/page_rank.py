class PageRank:
    pages = {}
    pages_cnt = 0
    matrix = {}

    def __init__(self, pages):
        self.pages = pages
        self.pages_cnt = len(pages)

        # init all page ranks to 1/n
        for page in pages:
            page.rank = 1 / self.pages_cnt

    def create_matrix(self):
        for page in self.pages:
            for link in page.outlinks:
                if link.page_url in self.pages:
                    self.matrix[link.page_url][page.page_url] = page.rank


    # def iterative_formula_calculation(self):
    #    for page in self.pages:
    #        return
