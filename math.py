import math


def log(number):
    """
    Returns math.log(number) unless number == 0, in which case returns float('-inf').
    
    :rtype: float
    """
    if number == 0:
        return float('-inf')
    else:
        return math.log(number)

    
def telog(number):
    """
    Returns math.log(number) unless number == 0, in which case returns float('-inf').
    
    When the exceptional case is truly exceptional, this can be faster than testing the conditional.
    
    :rtype: float
    """
    try:
        return math.log(number)
    except ValueError:
        if number == 0:
            return float('-inf')
        else:
            raise


def logsumexp(iterable_of_floats):
    """
    For taking the log of sum(iterable_of_floats).
    """
    max_val = max(iterable_of_floats)
    return max_val + log(sum([math.exp(val - max_val) for val in iterable_of_floats]))


def log_add(log_a, log_b):
    """
    Simplified version of logsumexp for when you only have two values to work with.
    """
    if log_a > log_b:
        return log_a + (1 + math.exp(log_b - log_a))
    else:
        return log_b + (1 + math.exp(log_a - log_b))
