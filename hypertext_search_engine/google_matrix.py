from fractions import Fraction


def getMatrixS(_pages, alpha):
    matrix = []
    urls = {x.page_url for x in _pages}

    for pg in _pages:
        matrix.append([])

        # if no outlinks at page
        if not pg.outlinks:
            for j in range(len(_pages)):
                matrix[len(matrix) - 1].append(Fraction(alpha, len(_pages)))
        # else otherwise
        else:
            for link in urls:
                if link in pg.outlinks:
                    matrix[len(matrix) - 1].append(Fraction(alpha, len(pg.outlinks)))
                else:
                    matrix[len(matrix) - 1].append(Fraction(0))
    return matrix


def getMatrixE(length, alpha):
    matrix = []
    for i in range(length):
        matrix.append([])
        for j in range(length):
            matrix[i].append(Fraction(1 - alpha, length))
    return matrix


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

