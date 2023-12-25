from collections import defaultdict, deque


with open("25/input") as file:
    raw = file.read()

if 0: raw = """
jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr
"""

lines = raw.strip().split("\n")
p1 = p2 = 0

graph = defaultdict(lambda: set())
nodes = []
to_disconnect = [("zpc", "xvp"), ("dhl", "vfs"), ("nzn", "pbq")]
for line in lines:
    source, dests = line.split(": ")
    nodes.append(source)
    dests = dests.split(" ")
    for dest in dests:
        if (source, dest) in to_disconnect or (dest, source) in to_disconnect:
            continue
        graph[source].add(dest)
        graph[dest].add(source)


p1 = 1
at = "zpc"
queue = deque([at])
seen = set()

while queue:
    at = queue.pop()
    print(at)
    if at in seen:
        continue
    seen.add(at)
    for next in graph[at]:
        queue.append(next)
p1 *= len(seen)

at = "xvp"
queue = deque([at])
seen = set()

while queue:
    at = queue.pop()
    print(at)
    if at in seen:
        continue
    seen.add(at)
    for next in graph[at]:
        queue.append(next)
p1 *= len(seen)




print(p1, p2)


exit()
import networkx as nx 
import matplotlib.pyplot as plt 
   
  
# Defining a Class 
class GraphVisualization: 
   
    def __init__(self): 
          
        # visual is a list which stores all  
        # the set of edges that constitutes a 
        # graph 
        self.visual = [] 
          
    # addEdge function inputs the vertices of an 
    # edge and appends it to the visual list 
    def addEdge(self, a, b): 
        temp = [a, b] 
        self.visual.append(temp) 
          
    # In visualize function G is an object of 
    # class Graph given by networkx G.add_edges_from(visual) 
    # creates a graph with a given list 
    # nx.draw_networkx(G) - plots the graph 
    # plt.show() - displays the graph 
    def visualize(self): 
        G = nx.Graph() 
        G.add_edges_from(self.visual) 
        nx.draw_networkx(G) 
        plt.show() 

G = GraphVisualization() 
for source in graph:
    for dest in graph[source]:
        G.addEdge(source, dest)


G.visualize()

