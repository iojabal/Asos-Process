from flask import Flask, request
from models.Process import Process
from models.Algorithms import Algorithms, Priority, SJF, FCFS

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

    return {"Message": processes}


@app.route("/priority", methods=["POST"])
def priorityFunction():
    priority = Priority()
    priority.processes = algorithm.processes
    priority.readyQueue = priority.sortQueue(priority.processes)
    priority.doAlgorithm()
    priority.showExecutionQueue()
    ququ = []
    for process in priority.queue:
        a = [str(p) for p in process]
        ququ.append(a)
    return {"Message": ququ}

@app.route("/SJF", methods=["POST"])
def sjfFunction():
    sjf = SJF()
    sjf.processes = algorithm.processes
    sjf.readyQueue = sjf.sortQueue(sjf.processes)
    sjf.doAlgorithm()
    sjf.showExecutionQueue()
    sjf.showReadyQueue()
    ququ = []
    for process in sjf.queue:
        a = [str(p) for p in process]
        ququ.append(a)
    return {"Message": ququ}


@app.route("/FCFS", methods=['POST'])
def fcfsFunction():
    fcfs = FCFS()
    fcfs.processes = algorithm.processes
    fcfs.doAlgorithm()

    ququ = []
    for process in fcfs.queue:
        a = [str(p) for p in process]
        ququ.append(a)
    fcfs.showExecutionQueue()
    return {"message": ququ}

if __name__ == '__main__':
    app.run(debug=True)
