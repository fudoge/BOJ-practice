class Node():
    def __init__(self):
        self.children = {}
        self.end = False

class Trie():
    def __init__(self):
        self.root = Node()
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.end = True

    def delete(self, word):
        self.delete_helper(self.root, word, 0)

    def delete_helper(self, node, word, index):
        if index == len(word):
            if node.end:
                node.end = False
            return
        
        char = word[index]
        if char not in node.children:
            return
        
        child_node = node.children[char]
        self.delete_helper(child_node, word, index + 1)

        if not child_node.children and not child_node.end:
            del node.children[char]


a = Trie()
a.insert("algo")
a.insert("aloe")
a.insert("data")
a.insert("date")
a.insert("type")
a.insert("team")
a.insert("tea")

print(a.search("team"))

a.delete("tea")

print(a.search("tea"))
print(a.search("team"))
print(a.search("date"))