def add(*numbers):
    """
    Add all the numbers and return the sum.
    Ignore any bad input.
    """
    sum_total = 0
    for number in numbers:
        try:
            sum_total += number
        except TypeError:
            pass
    return sum_total
