#coding = utf8
class TrieNode:
    def __init__(self):
        self.nodes = dict()  #构建字典
        self.is_leaf = False

    def insert(self, word:str):
        curr = self
        