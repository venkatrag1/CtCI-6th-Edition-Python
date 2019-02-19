# O(N)
import unittest


def pal_perm(phrase):
    counts = set()
    for c in phrase:
        if c != ' ':
            c_lower = c.lower()
            if c_lower in counts:
                counts.remove(c_lower)
            else:
                counts.add(c_lower)
    return len(counts) <= 1

# Only space ? What about special characters?
# If ASCII can use ord and array and handle upper by - ord(A)

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = pal_perm(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
