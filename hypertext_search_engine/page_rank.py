from google_matrix import GoogleMatrix


class PageRank:
    matrix = GoogleMatrix

    def __init__(self, matrix):
        self.matrix = matrix
