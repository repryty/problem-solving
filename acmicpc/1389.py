class Graph:
    def __init__(self):
        self.vertex: dict[int, dict[int, set|bool]]=dict() # self.vertex = {"1": {"ways": {1, 2, 3}, "is_visited": False}, ... }

    def add_vertex(self, vertex_id: int): # add_vertex(1)
        self.vertex[vertex_id] = {"ways": set(), "is_visited": False} 
    
    def add_edge(self, from_id: int, to_id: int): # add_edge(1, 3)
        self.vertex[from_id]["ways"].add(to_id)
    
    def add_edge_indirectional(self, from_id: int, to_id: int): # add_edge_indirectional(1, 3)
        self.vertex[from_id]["ways"].add(to_id)
        self.vertex[to_id]["ways"].add(from_id)
    
    def get_ways(self, vertex_id: int)->list: # get_ways(1) >> [2, 4] (3은 방문함)
        ways = [i for i in self.vertex[vertex_id]["ways"] if not self.get_is_vistied(i)]
        ways.sort()
        return ways
    
    def get_all_ways(self, vertex_id: int)->list: # get_all_ways(1) >> [2, 4] (3은 방문함)
        ways = list(self.vertex[vertex_id]["ways"])
        ways.sort()
        return ways
        
    def get_is_reachable(self, from_id: int, to_id: int)->bool: # get_is_reachable(1, 3) >> True
        return to_id in self.vertex[from_id]["ways"]
    
    def get_is_vistied(self, vertex_id)->bool: # get_is_vistied(1) >> False
        return self.vertex[vertex_id]["is_visited"]
    
    def visit_vertex(self, vertex_id: int): # visit_vertex(1)
        self.vertex[vertex_id]["is_visited"] = True

def bfs(from_vertex: int, to_vertex: int, graph: Graph):
    bfs_queue = [from_vertex]

    distance = 0

    while bfs_queue:
        visiting = bfs_queue.pop(0)

        if visiting == to_vertex:
            break

        if graph.get_is_vistied(visiting):
            continue
            
        graph.visit_vertex(visiting)
        # print(visiting+1, end=" ")

        ways = graph.get_ways(visiting)
        for i in ways:
            bfs_queue.append(i)

        distance+=1
    
    return distance

N, M = [int(i) for i in input().split()]
graph = Graph()

for i in range(1, N+1):
    graph.add_vertex(i)

for _ in range(M):
    x, y = [int(i) for i in input().split()]
    graph.add_edge_indirectional(x, y)

bacon_number: dict[frozenset, int] = dict()

keys = graph.vertex.keys()
for i in keys:
    for j in keys:
        this_key = frozenset([i, j])
        if i == j or this_key in bacon_number.keys():
            continue
        bacon_number[this_key] = bfs(i, j, graph)
    
ones_bacon_number = []
for i in keys:
    for j in keys:
        this_key = frozenset([i, j])
        if i == j or this_key in bacon_number.keys():
            continue
        ones_bacon_number[i]+=bacon_number[this_key]

print(ones_bacon_number)