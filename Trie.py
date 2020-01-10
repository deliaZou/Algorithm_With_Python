#coding = utf8
class TrieNode:
    def __init__(self):
        self.nodes = dict()  #构建字典
        self.is_leaf = False

    def insert(self, word:str):   #    添加一个字到字典树中
        curr = self
        for char in word:
            if char not in curr.nodes:
                curr.nodes[char] = TrieNode()
            curr = curr.nodes[char]
        curr.is_leaf = True

    def insert_many(self, words:[str]):  #插入一列表的字到字典树中
        for word in words:
            self.insert(word)

    def search(self, word:str): #在字典树里面查询一个字
        curr = self
        for char in word:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]
        return curr.is_leaf


if __name__ == '__main__':
    t = TrieNode()
    t.insert_many(['d','e','f'])
    t.insert_many(['d', 'e', 'f','g'])
    print(t.search('e'))


