import numpy


class Projection:
    def __init__(self, points, plain=[[10, 0, 0], [0, 0, 0], [0, 10, 0]]):
        if self.checkPlainIsValid(plain):
            self.plain = plain
            self.points = points
        else:
            print("The plain cannot be formed")
            raise

    def calculate(self):
        A = self.plain[0]
        B = self.plain[1]
        C = self.plain[2]
        vectorBA = numpy.array([A[0] - B[0], A[1] - B[1], A[2] - B[2]])
        vectorBC = numpy.array([C[0] - B[0], C[1] - B[1], C[2] - B[2]])
        normalVector = numpy.cross(vectorBA, vectorBC)
        answer = []
        for point in self.points:
            ratio = (-(point[0] * normalVector[0] + point[1] * normalVector[1] + point[2] * normalVector[2] - (
                    normalVector[0] * B[0] + normalVector[1] * B[1] + normalVector[2] * B[2])) / (
                             normalVector[0] ** 2 + normalVector[1] ** 2 + normalVector[2] ** 2))
            px = point[0] + normalVector[0] * ratio
            py = point[1] + normalVector[1] * ratio
            pz = point[2] + normalVector[2] * ratio
            answer.append([px, py, pz])
        return answer

    @staticmethod
    def checkPlainIsValid(plain):
        return any([
            plain[0][0] * plain[2][0] != plain[1][0] * plain[1][0],
            plain[0][1] * plain[2][1] != plain[1][1] * plain[1][1],
            plain[0][2] * plain[2][2] != plain[1][2] * plain[1][2]
        ])


# hip = Projection([[2, -7.00, 8], [-4, 3, 10], [5, 3, 2], [8, 2, 3]], [[1, 2, 1], [2, 2, 2], [3, 3, 3]])
# print(hip.calculate())
