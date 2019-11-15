def depth_first_search(graph):
  visited, stack = set(), [root]
  while stack:
      vertex = stack.pop()
      if vertex not in visited:
          visited.add(vertex)
          stack.extend(graph[vertex] - visited)
  return visited

def depth_first_search_recursive(graph, start, visited=None):
  if visited is None:
      visited = set()
  visited.add(start)
  for next in graph[start] - visited:
      depth_first_search_recursive(graph, next, visited)
  return visited

graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}

import collections
         
def bfs(graph, initial):
    
  visited = []
  queue = [initial]
  while queue: 
      node = queue.pop(0)
      if node not in visited:
          visited.append(node)
          neighbours = graph[node]
      
          for neighbour in neighbours:
              queue.append(neighbour)

  return visited
 
print(bfs(graph,'A'))