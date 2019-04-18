from matrix_factory import MatrixFactory


class PageRank:
    matfact = MatrixFactory
    alpha = 0.85
    length = 1

    def __init__(self, pages, alpha):
        self.matfact = MatrixFactory(pages)
        self.length = len(pages)
        self.alpha = alpha

    # calculates the next PageRank vector iteration using the power method
    # def get_next_iteration(self):
    # todo - split to logical parts
    def do_page_rank(self):
        H = self.matfact.get_matrix_H()
        a = self.matfact.get_dangling_node_vector()
        pi = self.matfact.get_default_page_rank_vector()
        e = self.matfact.get_unit_vector()
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

        for i in range(50):
            pi = pi.dot(H).multiply(self.alpha) + e.multiply((float(pi.dot(a).toarray()[0][0]) * self.alpha + 1 - self.alpha)/self.length)

        return pi

    def do_page_rank_matrix(self):
        H = self.matfact.get_matrix_H()
        a = self.matfact.get_dangling_node_vector()
        pi = self.matfact.get_default_page_rank_vector()
        e = self.matfact.get_unit_vector()
        S = self.matfact.get_matrix_S()

        print(S.todense())

        for i in range(50):
            pi = pi.dot(H).multiply(self.alpha) + e.multiply((float(pi.dot(a).toarray()[0][0]) * self.alpha + 1 - self.alpha)/self.length)

        return pi
