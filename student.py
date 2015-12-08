class Student():
    def __init__(self, name, all_sem_n, tasks):
        self.name = name
        self.total_points = 0
        self.total_penalty = 0
        self.tasks = [[0 for i in range(tasks[j])] for j in range(all_sem_n)]

    def process(self, n_sem, n_task, result):
        if result.name == self.name:
            self.total_penalty += result.penalty
            self.total_points += int(result.solved)
            self.tasks[n_sem][n_task] = 1

    def get_sem_stats(self, n_sem):
        to_print = "\t".join([str(i) for i in self.tasks[n_sem]])
        solved = 0
        for i in self.tasks[n_sem]:
            solved += i
        return self.name+'\t'+to_print, str(solved)

    def get_total_stats(self):
        sems = []
        for i in range(len(self.tasks)):
            a, b = self.get_sem_stats(i)
            sems.append(b)
        sems.append(str(self.total_points))
        sems.append(str(self.total_penalty))
        return "\t".join(sems)