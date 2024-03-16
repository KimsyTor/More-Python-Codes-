import unittest
from find_replace import find_replace


class TestFindReplace(unittest.TestCase):
    def test_find_replace(self):
        self.assertEqual(find_replace([1, 2, 3, 4, 5]), [
                         'ODD', 'EVEN', 'ODD', 'EVEN', 'ODD'])
        self.assertEqual(find_replace([0, 1, 2, 3, 4, 5]), [
                         'EVEN', 'ODD', 'EVEN', 'ODD', 'EVEN', 'ODD'])
        self.assertEqual(find_replace([2, 4, 6, 8]), [
                         'EVEN', 'EVEN', 'EVEN', 'EVEN'])
        self.assertEqual(find_replace([1, 3, 5, 7]), [
                         'ODD', 'ODD', 'ODD', 'ODD'])
        self.assertEqual(find_replace([-1, -2, -3, -4, -5]), [
                         'ODD', 'EVEN', 'ODD', 'EVEN', 'ODD'])
        self.assertEqual(find_replace([]), [])


if __name__ == '__main__':
    unittest.main()
