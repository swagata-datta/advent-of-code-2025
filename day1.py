"""
Day 1: 2025. 
"""

from tools import *

test = inputfile('inputs/tests/day1.txt')
actual = inputfile('inputs/day1.txt')

def tracking_dict(input_):
    """Takes the input list, runs the algo, returns dict of how many times each number appeared"""
    tracking_dict = defaultdict(int)
    tracking_dict[50] = 1
    start = 50
    for i in input_:
        if i[0] == "L":
            start = (start - int(i[1:])) % 100
            tracking_dict[start] += 1
        else:
            start = (start + int(i[1:])) % 100
            tracking_dict[start] += 1
    return tracking_dict

def part1(input_, goal):
    dict_ = tracking_dict(input_)
    return dict_[goal]

assert part1(test, 0) == 3

# print(part1(actual, 0))
### 1064

############### PART TWO ############################

def tracking_dict2(input_):
    """Modifying for part 2"""
    tracking_dict = defaultdict(int)
    tracking_dict[50] = 1
    start = 50
    for i in input_:
        step = int(i[1:])
        if step > 100:
            tracking_dict[0] += step // 100
            step = step % 100
        if start == 0:
            if i[0] == "L":
                start = (start - step) % 100
                tracking_dict[start] += 1
            else:
                start = (start + step) % 100
                tracking_dict[start] += 1
        else:
            if i[0] == "L":
                start = (start - step) 
                if start < 0:
                    tracking_dict[0] += 1
                start = start % 100
                tracking_dict[start] += 1
            else:
                start = (start + step) 
                if start > 100:
                    tracking_dict[0] += 1
                start = start % 100
                tracking_dict[start] += 1

        
    return tracking_dict

assert tracking_dict2(test)[0] == 6
# print(tracking_dict2(actual))[0]

# 6122

