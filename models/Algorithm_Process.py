from queue import PriorityQueue, Queue


class Process:
    def __init__(self) -> None:
        self.process = None
        self.CPUTIME = None
        self.priority = None
        self.arrivedTime = None
