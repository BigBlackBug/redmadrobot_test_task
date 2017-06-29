from errors import ApplicationError
from generator import Generator


def dot_product(first_vector, second_vector):
    """
    calculates a dot product of vectors of the following format
    [number, sequence_length, ...]
    :param first_vector:
    :param second_vector:
    :return: cross product of these vectors
    """
    first_generator = Generator(first_vector)
    second_generator = Generator(second_vector)
    if first_generator.vector_length != second_generator.vector_length:
        raise ApplicationError("Expanded vector sizes are unequal")

    # a loop is more readable than a one-liner with 'map'
    value = 0
    for piece in zip(first_generator(), second_generator()):
        value += piece[0] * piece[1]
    return value
