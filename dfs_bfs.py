'''
DFS & BFS of a tree
'''
def bfs_tree(root):
  queue = [root]

  while queue:
    currentNode = queue[0]
    del queue[0]
    print(f'{currentNode.val}')
    if currentNode.left != None:
        queue.append(currentNode.left)
    if currentNode.right != None:
        queue.append(currentNode.right)

  return root

def dfs_tree(root):
  stack = [root]

  while stack:
    currentNode = queue.pop()
    print(f'{currentNode.val}')
    if currentNode.left != None:
        queue.append(currentNode.left)
    if currentNode.right != None:
        queue.append(currentNode.right)

  return root

'''
DFS & BFS of a graph
'''

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

graph_2 = {0: [1 ,2],
           1: [2],
           2: [3],
           3: [1, 2]}

import collections
'''
How to use deque's as a FIFO queue:

q = deque()
q.append('eat')
q.append('sleep')
q.append('code')

print(q) --> deque(['eat', 'sleep', 'code'])

q.popleft() --> 'eat'
q.popleft() --> 'sleep'
q.popleft() --> 'code'

q.pop() --> remove and return an element from the RIGHT side of the deque

'''
def bfs_2(graph, root):
  visited, queue = set(), collections.deque([root])
  visited.add(root)
  while len(queue) > 0:

    vertex = queue.popleft()
    
    for neighbour in graph[vertex]:
      if neighbour not in visited:
        visited.add(neighbour)
        queue.append(neighbour)

  return visited

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

print('bfs_2:', bfs_2(graph, 'A'))
print('bfs:', bfs(graph, 'A'))
