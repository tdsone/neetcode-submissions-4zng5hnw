class Node: 

    def __init__(self, val: str = ""):
        self.val = val
        self.children = {} # {<char>: node}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        # if first word
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node(c)
            
            curr = curr.children[c]

        curr.end = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word: 
            if c in curr.children:
                curr = curr.children[c]
                continue
            return False
        return curr.end
        
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix: 
            if c in curr.children:
                curr = curr.children[c]
                continue
            return False
        return True



        
        