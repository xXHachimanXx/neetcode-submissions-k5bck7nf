class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        node = self.root
        
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch] # walk ahead in trie

        node.is_end = True


    def search(self, word: str) -> bool:
        node = self.root
        
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch] # walk ahead in trie

        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch] # walk ahead in trie
        return True
        
        