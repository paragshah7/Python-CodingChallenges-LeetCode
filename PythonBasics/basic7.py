# coding=utf-8

import unittest


class A(unittest.TestCase):

    def setUp(self):
        pass

    def test_assert(self):
        assert 'OCP' in 'OCP', 'Mismatch'

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()

# print('Imported basic7 . . .')
#
# test = 'Test String'
#
#
# def find_index(courses_list, target):
#     """find the index of a value in a sequence"""
#     for i, value in enumerate(courses_list):
#         if value == target:
#             return i
#
#     return -1
