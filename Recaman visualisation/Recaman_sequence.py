from sortedcollections import OrderedSet


def sequence_recaman():
    sequence = OrderedSet([0])
    step = 1
    while True:
        previous_number = sequence[-1] - step
        next_number = sequence[-1] + step
        if (previous_number in sequence) or (previous_number < 0):
            yield next_number
            sequence.add(next_number)
            step += 1
        else:
            yield previous_number
            sequence.add(previous_number)
            step += 1
