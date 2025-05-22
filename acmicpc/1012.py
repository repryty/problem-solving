class Graph:
    def __init__(self):
        self.vertex: dict[tuple, dict[int, set|bool]]=dict() # self.vertex = {"1": {"ways": {1, 2, 3}, "is_visited": False}, ... }

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
    
def dfs(from_vertex: int, graph: Graph, lettuces: set):
    dfs_stack = [from_vertex]

    while dfs_stack:
        visiting = dfs_stack.pop()

        if graph.get_is_vistied(visiting):
            continue
            
        graph.visit_vertex(visiting)
        # print(visiting, end=" ")
        lettuces.remove(visiting)

        ways = graph.get_ways(visiting)
        ways.reverse()
        for i in ways:
            dfs_stack.append(i)

    return lettuces

T = int(input())

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

graph = Graph()

lettuces = set()
for _ in range(T):
    M, N, K = [int(i) for i in input().split()]

    for _ in range(K):
        x, y = [int(i) for i in input().split()]
        lettuces.add((x, y))
        graph.add_vertex((x, y))
        
        for i, j in DIRECTIONS:
            if (x+i, y+j) in lettuces:
                graph.add_edge_indirectional((x+i, y+j), (x, y))
    counter = 0
    while lettuces:
        lettuces = dfs(list(lettuces)[0], graph, lettuces)
        # print()
        counter += 1
    print(counter)