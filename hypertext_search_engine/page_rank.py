from matrix_factory import MatrixFactory


class PageRank:
    matfact = MatrixFactory
    alpha = 0.85
    length = 1
    iteration_count = 50
    debug = False

    def __init__(self, pages, alpha, iteration_count, debug):
        self.matfact = MatrixFactory(pages)
        self.length = len(pages)
        self.alpha = alpha
        self.iteration_count = iteration_count
        self.debug = debug

    # calculates the next PageRank vector iteration using the power method
    # def get_next_iteration(self):
    # todo - split to logical parts
    def do_page_rank(self):
        H = self.matfact.get_matrix_H()
        a = self.matfact.get_dangling_node_vector()
        pi = self.matfact.get_default_page_rank_vector()
        e = self.matfact.get_unit_vector()

        '''
        print("H matrix")
        print(H.todense())
        print("a vector")
        print(a.todense())
        print("PI vector")
        print(pi.todense())
        print("e vector")
        print(e.todense())
        print("pi * a")
        print(pi.dot(a).todense())
        print("pi * H")
        print(pi.dot(H).todense())
        print("pi * H * alpha")
        print(pi.dot(H).multiply(self.alpha).todense())
        '''
        if self.debug:
            print("Iterations:")
        for i in range(self.iteration_count):
            if self.debug:
                print(pi.todense())
            pi = pi.dot(H).multiply(self.alpha) + e.multiply((pi.dot(a).toarray()[0][0] * self.alpha + 1 - self.alpha)/self.length)
        if self.debug:
            print()
        return pi

    def do_page_rank_matrix(self):
        pi = self.matfact.get_default_page_rank_vector()
        e = self.matfact.get_unit_vector()
        S = self.matfact.get_matrix_S()

        E = (e.transpose(copy=True)).dot(e).multiply((1-self.alpha)/self.length)  # matrix of ((1-alpha)/n)*(e * e^T)
        aS = S.multiply(self.alpha)
        aSE = aS+E
        if self.debug:
            print("Iterations:")
        for i in range(self.iteration_count):
            if self.debug:
                print(pi.todense())
            pi = pi.dot(aSE)
        if self.debug:
            print()
        return pi
