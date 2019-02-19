# O(N)
import unittest
from collections import Counter



def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    count = Counter()
    for c in str1:
        count[c] += 1
    for c in str2:
        if count[c] == 0:
            return False
        count[c] -= 1
        if count[c] == 0:
            del count[c]
    return (len(count) == 0)



class Test(unittest.TestCase):
    dataT = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
    dataF = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )

    def test_cp(self):
        # true check
        for test_strings in self.dataT:
            result = check_permutation(*test_strings)
            self.assertTrue(result)
        # false check
        for test_strings in self.dataF:
            result = check_permutation(*test_strings)
            self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
