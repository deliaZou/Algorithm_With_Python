#coding = utf8
class Graph(object):
    def __init__(self):
        self.nodes = []  # 表示图的点集
        self.edge = {}  # 表示图的边集

    def insert(self, a, b):
        # 如果 a 不在图的点集里，则添加 a
        if not(a in self.nodes):
            self.nodes.append(a)
            self.edge[a] = list()
        # 如果 b 不在图的点集里，则添加 b
        if not(b in self.nodes):
            self.nodes.append(b)
            self.edge[b] = list()
        # a 连接 b
        self.edge[a].append(b)
        # b 连接 a
        self.edge[b].append(a)

    def succ(self, a):
        # 返回与 a 连接的点
        return self.edge[a]

    def show_nodes(self):
        # 返回图的点集
        return self.nodes

    def show_edge(self):
        print(self.edge)

'''深度优先搜索(DFS)'''
def dfs(G,s,S=None,res=None):
    if S is None:
        # 储存已经访问节点
        S=set()
    if res is None:
        # 存储遍历顺序
        res=[]
    res.append(s)
    S.add(s)
    for u in G[s]:
        if u in S:
            continue
        S.add(u)
        dfs(G,u,S,res)

    return res

def bfs(graph, start):
    # explored：已经遍历的节点列表，queue:寻找待遍历的节点队列
    explored, queue = [], [start]
    explored.append(start)
    while queue:
        # v:将要遍历的某节点
        v = queue.pop(0)
        # w:节点 v 的邻居
        for w in graph[v]:
            # w:如果 w 未被遍历，则遍历
            if w not in explored:
                # 添加 w 节点到已遍历的节点列表
                explored.append(w)
                # 添加 w 节点到寻找待遍历的节点队列
                queue.append(w)
    return explored

G = {'0': ['1', '2'],
     '1': ['2', '3'],
     '2': ['3', '5'],
     '3': ['4'],
     '4': [],
     '5': []}

print(bfs(G, '0'))

G = {'0': ['1', '2'],
     '1': ['2', '3'],
     '2': ['3', '5'],
     '3': ['4'],
     '4': [],
     '5': []}

print(dfs(G, '0'))


graph = Graph()
graph.insert('0', '1')
graph.insert('0', '2')
graph.insert('0', '3')
graph.insert('1', '3')
graph.insert('2', '3')
graph.show_edge()
