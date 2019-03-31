from fractions import Fraction


# return stochastic matrix S multiplied by parameter alpha
def getMatrixS(_pages, alpha):
    matrix = []
    urls = {page_url for page_url in _pages}  # list of all URLs

    for purl in _pages:
        pg = _pages[purl]  # iterated page
        matrix.append([])

        # if no outlinks at page
        if not pg.outlinks:
            for j in range(len(_pages)):
                matrix[len(matrix) - 1].append(Fraction(alpha, len(_pages)))
        # else otherwise
        else:
            for link in urls:  # for all pages
                if link in pg.outlinks:  # if pg has outlink to link append alpha*(1 / (count of pg' outlinks))
                    matrix[len(matrix) - 1].append(Fraction(alpha, len(pg.outlinks)))
                else:  # append 0 otherwise
                    matrix[len(matrix) - 1].append(Fraction(0))
    return matrix


# return primitive matrix E multiplied by parameter (1 - alpha)
def getMatrixE(length, alpha):
    matrix = []
    for i in range(length):
        matrix.append([])
        for j in range(length):
            matrix[i].append(Fraction(1 - alpha, length))
    return matrix


# return Google matrix by sum of stochastic matrix S and primitive matrix E
def getMatrixG(matrixS, matrixE):
    matrix = []
    for i in range(len(matrixS)):
        matrix.append([])
        for j in range(len(matrixS)):
            matrix[i].append(matrixS[i][j] + matrixE[i][j])
    return matrix


class GoogleMatrix:
    data = []

    def __init__(self, pages, alpha):
        self.data = getMatrixG(getMatrixS(pages, alpha), getMatrixE(len(pages), alpha))

    def __str__(self):
        for row in self.data:
            for elem in row:
                print(elem, end="\t")
            print()

