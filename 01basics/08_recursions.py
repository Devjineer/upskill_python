# TAIL RECURSION
'''no work left after recursion'''

def summation(start, stop, acc = 0):
    if start == stop + 1:
        return acc;
    else:
        return summation(start + 1, stop, acc + start);
print(summation(8, 10));


# NON TAIL RECURSION
'''work is left after recursion call'''
def nonTailSummation(start, stop = 5):
    if start == stop:
        return stop;
    else:
        return start + nonTailSummation(start + 1, stop)
    
print(nonTailSummation(1))