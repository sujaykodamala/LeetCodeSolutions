class Trie:

    trie = None
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tempTrie = self.trie
        for c in word:
            if c not in tempTrie.keys():
                tempTrie[c] = {}
            tempTrie = tempTrie[c]
        tempTrie['#'] = 1
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tempTrie = self.trie
        for c in word:
            if c in tempTrie.keys():
                tempTrie = tempTrie[c]
            else:
                return False
        return '#' in tempTrie

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tempTrie = self.trie
        for c in prefix:
            if c in tempTrie.keys():
                tempTrie = tempTrie[c]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)