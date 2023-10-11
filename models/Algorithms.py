import copy
import numpy
from copy import deepcopy


class Algorithms:
    def __init__(self):
        self.processes = []
        self.executionQueue = [0]
        self.readyQueue = []
        self.queue = []
        self.ctx = 0
        self.quantum = 0
        self.pr = False
        self.timeAround = []
        self.timeAroundtoShow = []
        self.waitingTime = []

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

    def getProcessWithMinArrivedTime(self):
        min_index = -1
        # Inicializamos con un valor positivo infinito
        min_arrived_time = float('inf')

        for index, process in enumerate(self.processes):
            if process.arrivedTime < min_arrived_time:
                min_arrived_time = process.arrivedTime
                min_index = index

        return self.processes.pop(min_index)

    def getProcessByIndex(self, index):
        for process in self.processes:
            if process.arrivedTime == index:
                return process

    def getMinProcesCPUTime(self):
        if not self.readyQueue:
            return None
        return min(self.readyQueue, key=lambda x: x.CPUTIME)

    def calculateTurnaroundTime(self, process):
        try:
            return len([p for p in self.executionQueue if hasattr(p, 'process') and p.process == process.process])
        except AttributeError:
            # Manejar la excepción si el atributo 'process' no está presente
            return 0

    def calculatWaitingTime(self, process):
        wp = 0
        for list in self.queue:
            for p in list:
                if p.process == process.process:
                    wp += 1
        return wp - 1


class Priority(Algorithms):
    def __init__(self):
        super().__init__()

    def sortQueue(self, q):
        return sorted(q, key=lambda x: x.priority)

    def doAlgorithm(self):
        ant = 0
        while self.readyQueue:
            self.queue.append(copy.deepcopy(self.readyQueue))
            ready_process = self.readyQueue.pop(0)
            self.executionQueue.append(ready_process)

            for _ in range(1, ready_process.CPUTIME):
                self.queue.append(copy.deepcopy(self.readyQueue))
                p = ready_process
                p.CPUTIME -= 1

                if ready_process.CPUTIME != 0:
                    self.executionQueue.append(p)
                ready_process = p

            if self.ctx is not None:
                for _ in range(self.ctx):
                    self.executionQueue.append(0)

            if ready_process.CPUTIME == 1:

                self.timeAround.append(
                    ant + self.calculateTuraroundTime(ready_process))
                self.waitingTime.append(
                    self.calculatWaitingTime(ready_process))
                try:
                    ant += self.calculateTuraroundTime(ready_process)
                except:
                    ant = 0
        for tt, wt in zip(self.timeAround, self.waitingTime):
            self.timeAroundtoShow.append(tt + wt)


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
        ant = 0
        while self.readyQueue:
            self.queue.append(copy.deepcopy(self.readyQueue))
            ready_process = self.readyQueue.pop(0)
            self.executionQueue.append(ready_process)

            for _ in range(1, ready_process.CPUTIME):
                self.queue.append(copy.deepcopy(self.readyQueue))
                p = ready_process
                p.CPUTIME -= 1

                if ready_process.CPUTIME != 0:
                    self.executionQueue.append(p)
                ready_process = p

            if self.ctx is not None:
                for _ in range(self.ctx):
                    self.executionQueue.append(0)
            if ready_process.CPUTIME == 1:

                self.timeAround.append(
                    ant + self.calculateTuraroundTime(ready_process))
                self.waitingTime.append(
                    self.calculatWaitingTime(ready_process))
                try:
                    ant += self.calculateTuraroundTime(ready_process)
                except:
                    ant = 0
        for tt, wt in zip(self.timeAround, self.waitingTime):
            self.timeAroundtoShow.append(tt + wt)


class FCFS(Algorithms):
    def __init__(self):
        super().__init__()

    def doAlgorithm(self):
        hgp = self.getHighestArrivedTime()
        ant = 0
        i = 0
        while i < hgp:
            pr = self.getProcessWithMinArrivedTime()
            if pr is not None:
                self.readyQueue.append(pr)
            self.queue.append(copy.deepcopy(self.readyQueue))
            ready_process = self.readyQueue.pop(0)

            self.executionQueue.append(ready_process)
            if ready_process is not None:
                for _ in range(1, ready_process.CPUTIME):

                    self.queue.append(copy.deepcopy(self.readyQueue))
                    p = ready_process
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

                if ready_process.CPUTIME == 1:

                    self.timeAround.append(
                        ant + self.calculateTuraroundTime(ready_process))
                    self.waitingTime.append(
                        self.calculatWaitingTime(ready_process))
                    try:
                        ant += self.calculateTuraroundTime(ready_process)
                    except:
                        ant = 0

            i += 1

        for tt, wt in zip(self.timeAround, self.waitingTime):
            self.timeAroundtoShow.append(tt + wt)

        self.queue = ["0" if sublist == [] or sublist[0]
                      == None else sublist for sublist in self.queue]


class SRT(Algorithms):
    def __init__(self):
        super().__init__()

    def doAlgorithm(self):
        hgm = self.getHighestArrivedTime()
        i = 0
        ant = 0
        while i < hgm:
            pr = self.getProcessByIndex(i)
            if pr is not None:
                self.readyQueue.append(pr)
            self.queue.append(copy.deepcopy(self.readyQueue))
            ready_process = self.readyQueue.pop(0)

            self.executionQueue.append(ready_process)
            if ready_process is not None:
                j = 0
                ant = 0
                while j < ready_process.CPUTIME:
                    aux = self.getMinProcesCPUTime()
                    p = ready_process
                    p.CPUTIME -= 1
                    self.queue.append(copy.deepcopy(self.readyQueue))
                    if aux is not None:
                        if p.CPUTIME > aux.CPUTIME:
                            ap = self.executionQueue.pop()
                            idx = self.readyQueue.index(aux)
                            p = self.readyQueue.pop(idx)
                            ready_process = p
                            # _ = self.queue.pop()
                            self.readyQueue.append(ap)
                            self.executionQueue.append(0)
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

        for ready_process in self.processes:
            self.timeAround.append(
                ant + self.calculateTuraroundTime(ready_process))
            self.waitingTime.append(self.calculatWaitingTime(ready_process))
            try:
                ant += self.calculateTuraroundTime(ready_process)
            except:
                ant = 0

        for tt, wt in zip(self.timeAround, self.waitingTime):
            self.timeAroundtoShow.append(tt + wt)
        self.queue = ["0" if sublist == [] or sublist[0]
                      == None else sublist for sublist in self.queue]


class RR(Algorithms):
    def __init__(self):
        super().__init__()

    def doAlgorithm(self):
        quantum = self.quantum
        time_slice = 0
        ant = 0
        while self.readyQueue:
            self.queue.append(self.readyQueue)
            current_process = self.readyQueue.pop(0)

            # Ejecuta el proceso durante un tiempo igual al quantum o hasta que se complete
            for _ in range(min(quantum, current_process.CPUTIME)):
                self.queue.append(copy.deepcopy(self.readyQueue))
                self.executionQueue.append(copy.deepcopy(current_process))
                current_process.CPUTIME -= 1
                time_slice += 1

            # Verifica si el proceso aún tiene tiempo restante de CPU
            if current_process.CPUTIME > 0:
                self.readyQueue.append(current_process)
                # current_process.waitingTime += 1

            # Agrega cambios de contexto si es necesario
            for _ in range(self.ctx):
                self.executionQueue.append(0)

            # Restablece el contador de tiempo si ha excedido el quantum
            if time_slice >= quantum:
                time_slice = 0

        for current_process in self.processes:
            if isinstance(current_process, int):
                continue
            self.timeAround.append(
                ant + self.calculateTurnaroundTime(current_process))
            self.waitingTime.append(self.calculatWaitingTime(current_process))
            try:
                ant += self.calculateTurnaroundTime(current_process)
            except:
                ant = 0
        for tt, wt in zip(self.timeAround, self.waitingTime):
            self.timeAroundtoShow.append(tt + wt)
