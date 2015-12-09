import informatics_parser
from result import Result
from student import Student

def parse_file(name, to_int):
    f = open(name, 'r')
    txt = f.read()
    f.close()
    out = txt.split('\n')
    if to_int:
        out = [int(x) for x in out]
    return out

def scan_task(id, n_sem, n_task, students):
    submits = informatics_parser.parse_id(id)
    for submit in submits:
        for student in students:
            if submit[1] == student.name:
                r = Result(submit[1], submit[2], submit[3])
                student.process(n_sem, n_task, r)
                print 'Student:', student.name
                print 'Result:', submit[2]


def main(sems):
    names = parse_file('students.txt', False)
    task_ids = []
    for i in range(sems):
        task_ids.append(parse_file('tasks'+str(i+1)+'.txt', True))
    students = [Student(i, len(task_ids), [len(j) for j in task_ids]) for i in names]
    try:
        for n_sem in range(len(task_ids)):
            for n_task in range(len(task_ids[n_sem])):
                print "TASK:", task_ids[n_sem][n_task]
                scan_task(task_ids[n_sem][n_task], n_sem, n_task, students)
    except IndexError():
        pass
    for i in range(sems):
        txt = 'name\t' + '\t'.join([str(x) for x in task_ids[i]])+'\n'
        for student in students:
            l1, l2 = student.get_sem_stats(i)
            txt += l1+'\t'+l2+'\n'
        f = open('results/'+str(i)+'.txt', 'w')
        f.write(txt)
        f.close()


main(6)