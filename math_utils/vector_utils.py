from random import randint

from math_utils.errors import ApplicationError
from math_utils.vector_unpacker import VectorUnpacker


def dot_product(first_vector, second_vector):
    """
    calculates dot product of vectors of the following format
    [number, sequence_length, ...]
    :param first_vector:
    :param second_vector:
    :return: dot product of these vectors
    """
    first_unpacker = VectorUnpacker(first_vector)
    second_unpacker = VectorUnpacker(second_vector)
    if first_unpacker.unpacked_vector_length != second_unpacker.unpacked_vector_length:
        raise ApplicationError("Unpacked vector sizes are unequal")

    # looks better than a 'map' one-liner to me
    value = 0
    for piece in zip(first_unpacker(), second_unpacker()):
        value += piece[0] * piece[1]

    return value


def generate_dense_vector(expanded_vector_size, number_of_pieces):
    """
    generates a dense vector with the following format
    [number, sequence_length, ...] to be used in dot_product function
    :param expanded_vector_size: size of the vector if it was expanded(unpacked)
    :param number_of_pieces: number of (number, sequence_length) pieces
    :return: a dense vector
    """
    vector = []
    remaining = expanded_vector_size
    piece_length = int(expanded_vector_size / number_of_pieces)
    for i in range(number_of_pieces - 1):
        number = randint(1, 10)
        vector.extend([number, piece_length])
        remaining -= piece_length
    vector.extend([randint(1, 10), remaining])
    return vector
