# O(N)
import unittest


def string_compression(string):
    compressed = []
    last_seen = string[0]
    last_seen_cnt = 1
    for c in string[1:]:
        if c == last_seen:
            last_seen_cnt += 1
        else:
            compressed.extend([last_seen, str(last_seen_cnt)])
            last_seen_cnt = 1
        last_seen = c
    compressed.extend([last_seen, str(last_seen_cnt)])
    return min(string, ''.join(compressed), key=len)

# Can instead initialize to size of original string and exit out
# when size is exceeded instead of doing min at end

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
