from _collections import defaultdict
"""
Steps:
[1]: Implement a stack
[2]: Push the initial node, say it's called "s" onto our stack
[3]: Start a loop that will go on as long as the stack is not empty, the loop will contain the following logic:
    [1]: Pop the last node in the stack, lets call it v
    [2]: mark v as visited
    [3]: Loop over neighbours of v that has not been visited
    [4]: Push unvisited neighbour, say it's called n onto he stack.

Space complexity: O(V)
"""

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def insertEdge(self, v1, v2):
        self.graph[v1].append(v2)
        # v1 => v2

    def DFS(self,startNode):
        visited = set()
        st = []
        st.append(startNode)

        while(len(st)):
            cur = st[-1]
            st.pop()

            if (cur not in visited):
                print(cur, end=" ")
                visited.add(cur)

            for vertex in self.graph[cur]:
                if (vertex not in visited):
                    st.append(vertex)

g = Graph()
g.insertEdge(2,1)
g.insertEdge(2,5)
g.insertEdge(5,6)
g.insertEdge(5,8)
g.insertEdge(6,8)

g.DFS(2)



