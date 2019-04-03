from google_matrix import GoogleMatrix


class PageRank:
    matrix = GoogleMatrix

    def __init__(self, matrix):
        self.matrix = matrix

    # calculates the next PageRank vector iteration using the power method
    # def get_next_iteration(self):

