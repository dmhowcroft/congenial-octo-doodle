import math


def log(number):
    # Switched to try-except bc exceptions should be rare so this is faster than testing the conditional every time
    # try:
    #     return math.log(number)
    # except ValueError:
    #     if number == 0:
    #         return float('-inf')
    #     else:
    #         raise
    if number == 0:
        return float('-inf')
    else:
        return math.log(number)



def logsumexp(iterable_of_floats):
    max_val = max(iterable_of_floats)
    return max_val + log(sum([math.exp(val - max_val) for val in iterable_of_floats]))
