from argparse import ArgumentParser

from math_utils import vector_utils

DEFAULT_NUMBER_OF_PIECES = 2
if __name__ == '__main__':
    parser = ArgumentParser(description='Dot product calculation test client')
    parser.add_argument("-s", "--expanded_vector_size", type=int, default=6,
                        help="generated vectors will have the specified size")
    args = parser.parse_args()
    first_vector = vector_utils.generate_dense_vector(
        expanded_vector_size=args.expanded_vector_size,
        number_of_pieces=DEFAULT_NUMBER_OF_PIECES)
    second_vector = vector_utils.generate_dense_vector(
        expanded_vector_size=args.expanded_vector_size,
        number_of_pieces=DEFAULT_NUMBER_OF_PIECES)
    print("Calculating dot product of dense vectors")
    print(first_vector)
    print(second_vector)
    dot_product = vector_utils.dot_product(first_vector, second_vector)
    print("Dot product: {}".format(dot_product))
