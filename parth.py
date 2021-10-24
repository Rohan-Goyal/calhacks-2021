import itertools

class Student:
    all_students = []

    def __init__(self, name, times):
        self.name = name
        self.times = times #1 or 0. for now, list of 5 entries
        Student.all_students.append(self)

def group_making(size=2):
    #print(Student.all_students)
    all_combs_list = list(generate_groups(Student.all_students, size))
    #print(all_combs_list)
    #all_combs_list = combination_gen(Student.all_students)
    combs_scores = compatability_score(all_combs_list, size)
    print(combs_scores)
    index = combs_scores.index(max(combs_scores))
    #print(all_combs_list[index][0])
    for a,b in all_combs_list[index]:
        print(a.name, b.name)
    #print((x.name, y.name) for (x,y) in all_combs_list[combs_scores.index(max(combs_scores))])
    
def generate_groups(lst, n):
    if not lst:
        yield []
    else:
        for group in (((lst[0],) + xs) for xs in itertools.combinations(lst[1:], n-1)):
            for groups in generate_groups([x for x in lst if x not in group], n):
                yield [group] + groups

def combination_gen(all_students):
    pairs = []
    for i in all_students:
        for j in all_students[i+1:]:
            pairs.append([i, j])
    return pairs


def compatability_score(all_combs_list, size):
    score_list = []
    score_worlds = []
    i=0
    for world in all_combs_list:
        score_list.append([])
        for student1, student2 in world:
            s = 0
            for t in range(len(student1.times)):
                if student1.times[t] == 1 and student2.times[t] ==1:
                   s += 1
            score_list[i].append( s/len(student1.times) )
            
        if min(score_list[i]) > 0:
            score_worlds.append( sum(score_list[i]) )
        else: 
            score_worlds.append(0)
        i+=1
    return score_worlds

s1 = Student('s1', [1, 1, 0, 0, 1])
s2 = Student('s2', [1, 0, 0, 0, 1])
s3 = Student('s3', [1, 0, 0, 1, 0])
s4 = Student('s4', [1, 1, 1, 1, 0])
# s5 = Student('s5', [1, 1, 0, 0, 1])
# s6 = Student('s6', [1, 1, 0, 0, 1])
# s7 = Student('s7', [1, 1, 0, 0, 1])
# s8 = Student('s8', [1, 1, 0, 0, 1])
# s9 = Student('s9', [1, 1, 0, 0, 1])
# s10 = Student('s10', [1, 1, 0, 0, 1])

group_making()