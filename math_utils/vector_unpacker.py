class VectorUnpacker:
    def __init__(self, vector):
        if len(vector) % 2 != 0:
            raise ValueError("Number of items in a vector is not even")
        self._vector = vector
        self._vector_length = self._calculate_vector_length(vector)
        self._current_piece = self._get_piece(self._vector, 0)
        self._piece_index = 0
        self._counter = 0

    def __iter__(self):
        while self._piece_index < int(len(self._vector) / 2):
            if self._counter < self._current_piece[1]:
                yield self._current_piece[0]
                self._counter += 1
                # used all numbers in the current sequence
                if self._counter == self._current_piece[1]:
                    # extract next piece
                    self._piece_index += 1
                    self._current_piece = self._get_piece(
                        self._vector,
                        self._piece_index)
                    self._counter = 0

    def __call__(self, *args, **kwargs):
        return iter(self)

    @property
    def unpacked_vector_length(self):
        return self._vector_length

    @staticmethod
    def _get_piece(vector, piece_index):
        return vector[piece_index * 2:piece_index * 2 + 2]

    @staticmethod
    def _calculate_vector_length(vector):
        return sum(vector[1:len(vector):2])
