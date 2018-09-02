# File for utils functions and classes
import numpy as np  # for Mask class
import unittest     # for testing


class Mask(object):
    """
    Mask class to filter features based on array of 0 and 1.
    1 stands for passthrough and 0 stands for block.
    """

    __slots__ = "length", "mask", "scheme"

    def __init__(self, vector=None, length=None):
        self.length = len(vector)
        if vector is None:
            self.mask = np.array([1] * length, dtype=np.bool)
        else:
            self.mask = np.array(vector, dtype=np.bool)

    def __len__(self):
        return self.length

    def __getitem__(self, key):
        return self.mask[key]

    def set_scheme(self, scheme_len):
        self.length = scheme_len

    def multiply(self, other):
        if not isinstance(other, Mask):
            raise ValueError("Param other is not an instance of Mask")

        if len(self) == len(other):
            return Mask(vector=self.mask * other.mask)

        common_len = min(len(self), len(other))
        vector = []
        for i in range(common_len):
            vector.append(self[i] * other[i])
        vector.extend((self.mask if len(self) > len(other) else other.mask)[common_len:])
        return Mask(vector=vector)

    @classmethod
    def generate_from_indexes(cls, allowed, scheme_len=50):
        scheme = [0] * scheme_len

        for index in allowed:
            scheme[index] = 1

        return Mask(vector=scheme)

    def __mul__(self, other):
        return self.multiply(other)

    def __str__(self):
        to_digits = lambda x: '1' if x else '0'
        return ''.join(list(map(to_digits, self.mask)))

    def __eq__(self, other):
        return isinstance(other, Mask) and np.array_equal(self.mask, other.mask)


class TestsMask(unittest.TestCase):

    def test_creation(self):
        array = np.array([1, 1, 0])
        self.assertTrue(np.array_equal(array, Mask(array).mask))

    def test_to_str_1(self):
        array = np.array([1, 1, 1])
        self.assertEqual(str(Mask(array)), "111")

    def test_to_string_0(self):
        array = np.array([0, 0])
        self.assertEqual(str(Mask(array)), "00")

    def test_to_string_mixed(self):
        array = np.array([0, 1, 1, 0, 1])
        self.assertEqual(str(Mask(array)), "01101")

    def test_equal_same_reference(self):
        array = np.array([0, 1])
        self.assertEqual(Mask(array), Mask(array))

    def test_equal_different_reference(self):
        array1 = np.array([0, 1])
        array2 = np.array([0, 1])
        self.assertEqual(Mask(array1), Mask(array2))

    def test_not_equal(self):
        array1 = np.array([0, 1])
        array2 = np.array([1, 0])
        self.assertNotEqual(Mask(array1), Mask(array2))

    def test_multiply_1_to_1(self):
        array1 = np.array([1])
        self.assertEqual(Mask(array1) * Mask(array1), Mask(array1))

    def test_multiply_0_to_0(self):
        array1 = np.array([0])
        self.assertEqual(Mask(array1) * Mask(array1), Mask(array1))

    def test_multiply_1_to_0(self):
        array1 = np.array([1])
        array2 = np.array([0])
        array3 = np.array([0])
        self.assertEqual(Mask(array1) * Mask(array2), Mask(array3))

    def test_multiply_custom(self):
        array1 = np.array([1, 0, 0, 1])
        array2 = np.array([1, 0, 1, 0])
        array3 = np.array([1, 0, 0, 0])
        self.assertEqual(Mask(array1) * Mask(array2), Mask(array3))

    def test_multiply_different_size(self):
        array1 = np.array([0, 1, 1, 1, 0, 1])
        array2 = np.array([1, 0, 1, 1])
        array3 = np.array([0, 0, 1, 1, 0, 1])
        self.assertEqual(Mask(array1) * Mask(array2), Mask(array3))

    def test_check_bit_0(self):
        array = np.array([0, 1])
        self.assertEqual(Mask(array)[0], 0)

    def test_check_bit_1(self):
        array = np.array([0, 1])
        self.assertEqual(Mask(array)[1], 1)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
