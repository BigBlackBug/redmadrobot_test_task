from math_utils import vector_utils

if __name__ == '__main__':
    vector_size = 6
    first_vector = vector_utils.generate_dense_vector(
        expanded_vector_size=vector_size,
        number_of_pieces=2)
    second_vector = vector_utils.generate_dense_vector(
        expanded_vector_size=vector_size,
        number_of_pieces=2)
    print("Calculating dot product of vectors")
    print(first_vector)
    print(second_vector)
    dot_product = vector_utils.dot_product(first_vector, second_vector)
    print(dot_product)
