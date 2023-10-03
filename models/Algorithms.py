import queue
from copy import deepcopy

class Algorithms:
    def __init__(self):
        self.processes = []
        self.executionQueue = []
        self.readyQueue = []
        self.ctx = None
        self.pr = False
        self.fcfs = False
        self.sjf = False
        self.srt = False
    def showReadyQueue(self):
        for process in self.readyQueue:
            print(process)

    def showProcesses(self):
        for process in self.processes:
            print(process)
    def showExecutionQueue(self):
        for process in self.executionQueue:
            print(process)

class Priority(Algorithms):
    def __init__(self):
        super().__init__()

    def sortQueue(self, q):
        return sorted(q, key=lambda x: x.priority)

    def doAlgorithm(self):
        for ready_process in self.readyQueue:
            self.executionQueue.append(ready_process)
            for i in range(1, ready_process.CPUTIME):
                p = deepcopy(ready_process)
                p.CPUTIME -= 1

                if ready_process.CPUTIME != 0:
                    self.executionQueue.append(p)
                ready_process = p
            if self.ctx is not None:
                for i in range(self.ctx):
                    self.executionQueue.append(0)