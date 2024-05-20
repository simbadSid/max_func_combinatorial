from typing import List

from src.utils.utils import FileParser


def f(x: str) -> int:
    return int(x) ** 2


class Smax:
    def __init__(self):
        # Init all the attributes
        self.k          : int               = -1
        self.m          : int               = -1
        self.k_list     : List[List[int]]   = [[]]

    def parse_input(self, file_relative_path: str = None):
        file_parser = FileParser(file_relative_path=file_relative_path)
        # Read K and M
        line = file_parser.next_line().split()
        self.k      = int(line[0])
        self.m      = int(line[1])

        # Read the data
        self.k_list = [[] for _ in range(self.k)]
        for i in range(self.k):
            line = file_parser.next_line().split()
            ni = int(line[0])
            self.k_list[i] = list(map(f, line[1:ni+1]))


    def find_max(self) -> int:
        # Init the transition matrix (used for the computation)
        transition_0: List[int] = [0]

        for i in range(self.k):
            transition_1: List[int] = []
            line = self.k_list[i]
            for j_line in range(len(line)):
                for past_score in transition_0:
                    s = (line[j_line] + past_score) % self.m
                    transition_1.append(s)

            transition_0 = transition_1

        res : int = transition_0[0]
        for score in transition_0[1::]:
            if score > res:
                res = score

        return res


if __name__ == '__main__':
    sMax = Smax()
    sMax.parse_input(file_relative_path='tests/input/test1.in')
    result = sMax.find_max()
    print(result)
