import copy

from flask import Flask, request
from models.Process import Process
from models.Algorithms import Algorithms, Priority, SJF, FCFS, SRT, RR

app = Flask(__name__)

algorithm = Algorithms()


@app.route("/", methods=["POST"])
def loadProcesses():
    algorithm.processes = []
    processes = request.get_json()
    for process in processes:

        p = Process()
        p.createProcess(process)
        algorithm.processes.append(p)

    return {"Message": "process Created"}, 200


@app.route("/priority", methods=["POST"])
def priorityFunction():

    algorithm.processes = []
    processes = request.get_json()
    for process in processes:

        p = Process()
        p.createProcess(process)
        algorithm.processes.append(p)

    priority = Priority()
    priority.processes = algorithm.processes
    priority.readyQueue = priority.sortQueue(priority.processes)
    priority.doAlgorithm()
    priority.showExecutionQueue()
    exequeue = []
    ququ = []
    for process in priority.queue:
        a = [str(p) for p in process]
        ququ.append(a)

    for process in priority.executionQueue:
        if not isinstance(process, int):
            if isinstance(process, str):
                # Si ya es una cadena, simplemente añádela
                exequeue.append(process)
            else:
                try:
                    a = str(process)  # Intenta convertir a cadena
                    exequeue.append(a)
                except ValueError:
                    print(f"No se pudo convertir {process} en una cadena.")
        else:
            exequeue.append(process)
    return {"ReadyQueue": ququ, "ExecutionQueue": exequeue, "waitingTime": priority.waitingTime, "turnaroundTime": priority.timeAroundtoShow}, 200


@app.route("/SJF", methods=["POST"])
def sjfFunction():

    algorithm.processes = []
    processes = request.get_json()
    for process in processes:

        p = Process()
        p.createProcess(process)
        algorithm.processes.append(p)

    sjf = SJF()
    sjf.processes = algorithm.processes
    sjf.readyQueue = sjf.sortQueue(sjf.processes)
    sjf.doAlgorithm()
    sjf.showExecutionQueue()
    sjf.showReadyQueue()
    ququ = []
    exequeue = []
    for process in sjf.queue:
        a = [str(p) for p in process]
        ququ.append(a)

    for process in sjf.executionQueue:
        if not isinstance(process, int):
            if isinstance(process, str):
                # Si ya es una cadena, simplemente añádela
                exequeue.append(process)
            else:
                try:
                    a = str(process)  # Intenta convertir a cadena
                    exequeue.append(a)
                except ValueError:
                    print(f"No se pudo convertir {process} en una cadena.")
        else:
            exequeue.append(process)
    return {"ReadyQueue": ququ, "ExecutionQueue": exequeue, "waitingTime": sjf.waitingTime, "turnaroundTime": sjf.timeAround}, 200


@app.route("/FCFS", methods=['POST'])
def fcfsFunction():

    algorithm.processes = []
    processes = request.get_json()
    for process in processes:

        p = Process()
        p.createProcess(process)
        algorithm.processes.append(p)

    fcfs = FCFS()
    fcfs.processes = algorithm.processes
    fcfs.doAlgorithm()

    ququ = []
    exequeue = []

    for process in fcfs.queue:
        a = [str(p) for p in process]
        ququ.append(a)
    fcfs.showExecutionQueue()

    for process in fcfs.executionQueue:
        if not isinstance(process, int):
            if isinstance(process, str):
                # Si ya es una cadena, simplemente añádela
                exequeue.append(process)
            else:
                try:
                    a = str(process)  # Intenta convertir a cadena
                    exequeue.append(a)
                except ValueError:
                    print(f"No se pudo convertir {process} en una cadena.")
        else:
            exequeue.append(process)
    return {"ReadyQueue": ququ, "ExecutionQueue": exequeue, "waitingTime": fcfs.waitingTime,
            "turnaroundTime": fcfs.timeAround}, 200


@app.route("/SRT", methods=['POST'])
def srtFunction():

    algorithm.processes = []
    processes = request.get_json()
    for process in processes:

        p = Process()
        p.createProcess(process)
        algorithm.processes.append(p)

    srt = SRT()
    srt.processes = algorithm.processes
    srt.doAlgorithm()

    ququ = []
    exequeue = []

    for process in srt.queue:
        a = [str(p) for p in process]
        ququ.append(a)
    srt.showExecutionQueue()

    for process in srt.executionQueue:
        if not isinstance(process, int):
            if isinstance(process, str):
                # Si ya es una cadena, simplemente añádela
                exequeue.append(process)
            else:
                try:
                    a = str(process)  # Intenta convertir a cadena
                    exequeue.append(a)
                except ValueError:
                    print(f"No se pudo convertir {process} en una cadena.")
        else:
            exequeue.append(process)

    return {"ReadyQueue": ququ, "ExecutionQueue": exequeue, "waitingTime": srt.waitingTime,
            "turnaroundTime": srt.timeAround}, 200


@app.route("/rr", methods=["POST"])
def rrFunction():

    algorithm.processes = []
    jsonRequest = request.get_json()
    processes = jsonRequest["processes"]
    print(type(jsonRequest["quantum"]))

    for process in processes:

        p = Process()
        p.createProcess(process)
        algorithm.processes.append(p)



    rr = RR()
    rr.processes = algorithm.processes
    rr.readyQueue = copy.deepcopy(algorithm.processes)
    rr.ctx = jsonRequest['context']
    rr.quantum = jsonRequest['quantum']
    rr.doAlgorithm()

    ququ = []
    exequeue = []

    for process in rr.queue:
        a = [str(p) for p in process]
        ququ.append(a)
    rr.showExecutionQueue()

    for process in rr.executionQueue:
        if not isinstance(process, int):
            if isinstance(process, str):
                # Si ya es una cadena, simplemente añádela
                exequeue.append(process)
            else:
                try:
                    a = str(process)  # Intenta convertir a cadena
                    exequeue.append(a)
                except ValueError:
                    print(f"No se pudo convertir {process} en una cadena.")
        else:
            exequeue.append(process)

    return {"ReadyQueue": ququ, "ExecutionQueue": exequeue, "waitingTime": rr.waitingTime,
            "turnaroundTime": rr.timeAround}, 200


if __name__ == '__main__':
    app.run(debug=True)
