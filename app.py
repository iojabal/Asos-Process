from flask import Flask, request
from models.Process import Process
from models.Algorithms import Algorithms, Priority

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
    return {"Message": "ok"}


if __name__ == '__main__':
    app.run(debug=True)
