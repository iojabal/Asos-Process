

class Process:
    def __init__(self) -> None:
        self.process = None
        self.CPUTIME = None
        self.priority = None
        self.arrivedTime = None

    def createProcess(self, jsonProcess):
        self.process = jsonProcess['process']
        try:
            self.CPUTIME = int(jsonProcess["cputime"])
        except KeyError:
            self.CPUTIME = None

        try:
            self.priority = int(jsonProcess["priority"])
        except KeyError:
            self.priority = None

        try:
            self.arrivedTime = int(jsonProcess["arrivedTime"])
        except KeyError:
            self.arrivedTime = None

    def __str__(self) -> str:
        return f'{f"process: {self.process}, cputime: {self.CPUTIME}, priority: {self.priority}, arrivedTime: {self.arrivedTime}"}'
