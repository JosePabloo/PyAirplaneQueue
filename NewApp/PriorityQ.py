import heapq


class PriorityQueue:
    def __init__(self):
        self.__q = []
        self.__index = 0

    def push(self, item, priority, priority2):
        heapq.heappush(self.__q, (priority, priority2, self.__index, item))
        self.__index += 1

    def pop(self):
        return heapq.heappop(self.__q)[-1]

    def empty(self):
        return len(self.__q) == 0