import copy
import numpy
from copy import deepcopy


class Algorithms:
    def __init__(self):
        self.processes = []
        self.executionQueue = [0]
        self.readyQueue = []
        self.queue = []
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

    def showReadyQueue(self):
        print("------------------------------------------------")
        for process in self.queue:
            a = [str(p) for p in process]
            print(a)

    def getHighestArrivedTime(self):
        total_sum = 0
        for process in self.processes:
            total_sum += process.CPUTIME

        return total_sum

    def getProcessByIndex(self, index):
        for process in self.processes:
            if process.arrivedTime == index:
                return process
    def getMinProcesCPUTime(self):
        if not self.readyQueue:
            return None
        return min(self.readyQueue, key=lambda x: x.CPUTIME)

class Priority(Algorithms):
    def __init__(self):
        super().__init__()

    def sortQueue(self, q):
        return sorted(q, key=lambda x: x.priority)

    def doAlgorithm(self):
        while self.readyQueue:
            self.queue.append(copy.deepcopy(self.readyQueue))
            ready_process = self.readyQueue.pop(0)
            self.executionQueue.append(ready_process)

            for _ in range(1, ready_process.CPUTIME):
                self.queue.append(copy.deepcopy(self.readyQueue))
                p = deepcopy(ready_process)
                p.CPUTIME -= 1

                if ready_process.CPUTIME != 0:
                    self.executionQueue.append(p)
                ready_process = p

            if self.ctx is not None:
                for _ in range(self.ctx):
                    self.executionQueue.append(0)

class SJF(Algorithms):
    def __init__(self):
        super().__init__()

    def sortQueue(self, d):
        return sorted(d, key=lambda x: x.CPUTIME)

    # def doAlgorithm(self):
    #     for ready_process in self.readyQueue:
    #         self.executionQueue.append(ready_process)
    #         for _ in range(1, ready_process.CPUTIME):
    #             p = deepcopy(ready_process)
    #             p.CPUTIME -= 1

    #             if ready_process.CPUTIME != 0:
    #                 self.executionQueue.append(p)
    #             ready_process = p
    #         if self.ctx is not None:
    #             for _ in range(self.ctx):
    #                 self.executionQueue.append(0)

    def doAlgorithm(self):
        while self.readyQueue:
            self.queue.append(copy.deepcopy(self.readyQueue))
            ready_process = self.readyQueue.pop(0)
            self.executionQueue.append(ready_process)

            for _ in range(1, ready_process.CPUTIME):
                self.queue.append(copy.deepcopy(self.readyQueue))
                p = deepcopy(ready_process)
                p.CPUTIME -= 1

                if ready_process.CPUTIME != 0:
                    self.executionQueue.append(p)
                ready_process = p

            if self.ctx is not None:
                for _ in range(self.ctx):
                    self.executionQueue.append(0)

class FCFS(Algorithms):
    def __init__(self):
        super().__init__()

    def doAlgorithm(self):
        i = 0
        while i < self.getHighestArrivedTime():
            pr = self.getProcessByIndex(i)
            if pr is not None:
                self.readyQueue.append(pr)
            self.queue.append(copy.deepcopy(self.readyQueue))
            ready_process = self.readyQueue.pop(0)

            self.executionQueue.append(ready_process)
            if ready_process is not None:
                for _ in range(1, ready_process.CPUTIME):

                    self.queue.append(copy.deepcopy(self.readyQueue))
                    p = deepcopy(ready_process)
                    p.CPUTIME -= 1



                    if ready_process.CPUTIME != 0:
                        self.executionQueue.append(p)
                    ready_process = p
                    i += 1
                    proc = self.getProcessByIndex(i)
                    if proc is not None:
                        self.readyQueue.append(proc)

                if self.ctx is not None:
                    for _ in range(self.ctx):
                        self.executionQueue.append(0)
            i += 1


        self.queue = ["0" if sublist == [] or sublist[0] == None else sublist for sublist in self.queue]

class SRT(Algorithms):
    def __init__(self):
        super().__init__()


    def doAlgorithm(self):
        i = 0
        while i < self.getHighestArrivedTime():
            pr = self.getProcessByIndex(i)
            if pr is not None:
                self.readyQueue.append(pr)
            self.queue.append(copy.deepcopy(self.readyQueue))
            ready_process = self.readyQueue.pop(0)

            self.executionQueue.append(ready_process)
            if ready_process is not None:
                j = 0
                while j < ready_process.CPUTIME:
                    aux = self.getMinProcesCPUTime()
                    p = deepcopy(ready_process)
                    p.CPUTIME -= 1
                    self.queue.append(copy.deepcopy(self.readyQueue))
                    if aux is not None:
                        if p.CPUTIME > aux.CPUTIME:
                            ap = self.executionQueue.pop()
                            idx = self.readyQueue.index(aux)
                            p = self.readyQueue.pop(idx)
                            # _ = self.queue.pop()
                            self.readyQueue.append(ap)
                            # self.executionQueue.append(p)
                            j = 0


                    if ready_process.CPUTIME != 0:
                        self.executionQueue.append(p)
                        j = 0
                    ready_process = p
                    i += 1
                    proc = self.getProcessByIndex(i)
                    if proc is not None:
                        self.readyQueue.append(proc)
                    j += 1
                if self.ctx is not None:
                    for _ in range(self.ctx):
                        self.executionQueue.append(0)
            i += 1
        self.queue = ["0" if sublist == [] or sublist[0] == None else sublist for sublist in self.queue]

