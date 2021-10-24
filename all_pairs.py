"""
def all_pairs(lst):
    if len(lst) < 2:
        yield []
        return
    if len(lst) % 2 == 1:
        # Handle odd length list
        for i in range(len(lst)):
            for result in all_pairs(lst[:i] + lst[i+1:]):
                yield result
    else:
        a = lst[0]
        for i in range(1,len(lst)):
            pair = (a,lst[i])
            for rest in all_pairs(lst[1:i]+lst[i+1:]):
                yield [pair] + rest

for x in all_pairs([0,1,2,3,4,5]):
    print(x)

"""

import itertools

def generate_groups(lst, n):
    if not lst:
        yield []
    else:
        for group in (((lst[0],) + xs) for xs in itertools.combinations(lst[1:], n-1)):
            for groups in generate_groups([x for x in lst if x not in group], n):
                yield [group] + groups

print(list(generate_groups([1, 2, 3, 4, 5 ,6 ], 2)))

"""

import itertools


def all_pairs(lst):
    N = len(lst)
    choice_indices = itertools.product(*[
        range(k) for k in reversed(range(1, N, 2)) ])

    for choice in choice_indices:
        # calculate the list corresponding to the choices
        tmp = lst[:]
        result = []
        for index in choice:
            result.append( (tmp.pop(0), tmp.pop(index)) )
        yield result
    
print(list(all_pairs([1, 2, 3, 4 ])))
"""
