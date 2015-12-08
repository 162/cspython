class Result():
    def __init__(self, name, solved, penalty):
        self.name = name
        self.solved = solved.startswith('+')
        self.penalty = int(penalty)