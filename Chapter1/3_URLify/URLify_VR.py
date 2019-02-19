# O(N)
import unittest


def urlify(string, length):
    '''function replaces single spaces with %20 and removes trailing spaces'''
    next_idx = len(string) - 1
    for idx in range(length-1, -1, -1):
        if string[idx] != ' ':
            string[next_idx] = string[idx]
            next_idx -= 1
        else:
            string[next_idx - 2: next_idx+1] = '%20'
            next_idx -= 3
    return string


class Test(unittest.TestCase):
    '''Test Cases'''
    # Using lists because Python strings are immutable
    data = [
        (list('much ado about nothing      '), 22,
         list('much%20ado%20about%20nothing')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = urlify(test_string, length)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
