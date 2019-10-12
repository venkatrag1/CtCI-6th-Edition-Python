NUM_CHARS = 256

class TrieNode:
    def __init__(self):
        self.children = [None] * NUM_CHARS
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def _char_to_ind(char):
        return ord(char) - ord('a')

    def insert(self, key):
        current = self.root
        current_len  = len(key)

        for level in range(current_len):
            index = self._char_to_ind(key[level])

            if not current.children[index]:
                current.children[index] = TrieNode()
            current = current.children[index]
        current.is_end = True

    def search(self, key):
        current = self.root
        current_len = len(key)

        for level in range(current_len):
            index = self._char_to_ind(key[level])
            if not current.children[index]:
                return False
            current = current.children[index]
        return current != None and current.is_end


def main():
    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the", "a", "there", "anaswe", "any",
            "by", "their"]
    output = ["Not present in trie",
              "Present in tire"]

    # Trie object
    t = Trie()

    # Construct trie
    for key in keys:
        t.insert(key)

        # Search for different keys
    print("{} ---- {}".format("the", output[t.search("the")]))
    print("{} ---- {}".format("these", output[t.search("these")]))
    print("{} ---- {}".format("their", output[t.search("their")]))
    print("{} ---- {}".format("thaw", output[t.search("thaw")]))


if __name__ == '__main__':
    main()
