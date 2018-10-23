class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.visited = False


class Solution:
    def get_or_create_node(self, graph, key):
        if key not in graph:
            graph[key] = Node(key)
        return graph[key]
    
    def visit_nodes(self, node):
        stack = [node]
        while stack:
            cur = stack.pop()
            cur.visited = True
            for o in cur.children:
                if not o.visited:
                    stack.append(o)

    def _numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        graph = {}
        # build the graph
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    node = self.get_or_create_node(graph, (i,j))
                    # above neigbhor
                    if i > 0 and grid[i-1][j] == '1':    
                        above = self.get_or_create_node(graph, (i-1, j))
                        node.children.append(above)
                    # below neighbor
                    if i < len(grid) - 1 and grid[i+1][j] == '1':
                        below = self.get_or_create_node(graph, (i+1, j))
                        node.children.append(below)
                    # left neighbor
                    if j > 0 and grid[i][j-1] == '1':    
                        left = self.get_or_create_node(graph, (i, j-1))
                        node.children.append(left)
                    # right neighbor
                    if j < len(grid[i]) - 1 and grid[i][j+1] == '1':
                        right = self.get_or_create_node(graph, (i, j+1))
                        node.children.append(right)
        
        subgraph_count = 0
        for node in graph.values():
            if node.visited:
                continue
            subgraph_count += 1
            self.visit_nodes(node)
            
        return subgraph_count


    def numIslands(self, grid):
        # use the given array as the graph :) it's essentially an adjacency
        # matrix. then 'mark' nodes as visited by overwriting to '0'. clever.
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid, i, j)

        return count

    def dfs(self, grid, ni, nj):
        stack = [(ni, nj)]
        while stack:
            i, j = stack.pop()
            grid[i][j] = '0'
            if i > 0 and grid[i-1][j] == '1':    
                stack.append((i-1, j))
            # below neighbor
            if i < len(grid) - 1 and grid[i+1][j] == '1':
                stack.append((i+1, j))
            # left neighbor
            if j > 0 and grid[i][j-1] == '1':    
                stack.append((i, j-1))
            # right neighbor
            if j < len(grid[i]) - 1 and grid[i][j+1] == '1':
                stack.append((i, j+1))


if __name__ == '__main__':
    M = [["1","1","1","1","0"],
         ["1","1","0","1","0"],
         ["1","1","0","0","0"],
         ["0","0","0","0","0"]]
    print(Solution().numIslands(M))

    M = [["1","0","1","1","0"],
         ["0","0","0","0","1"],
         ["1","1","1","1","0"],
         ["0","0","0","1","0"]]
    print(Solution().numIslands(M))
