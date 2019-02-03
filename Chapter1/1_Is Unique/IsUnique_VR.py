# O(N)
import unittest

# O(c) space where c is length of charset
# and O(n) time - using set
# Is it ASCII set? Going for general solution instead

def unique(string):
    seen_chars = set([])
    for ch in string:
        if ch in seen_chars:
            return False
        seen_chars.add(ch)
    return True

def unique_no_space(string):
    string = sorted(string)
    for idx in range(0, len(string)-1):
        if string[idx] == string[idx + 1]:
            return False
    return True


class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = unique(test_string)
            self.assertFalse(actual)

    def test_unique_no_space(self):
        # true check
        for test_string in self.dataT:
            actual = unique_no_space(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = unique_no_space(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()
