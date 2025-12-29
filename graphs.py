graph = {
 'a': {'b': 1, 'c': 2},
 'b': {'d': 4, 'e': 3},
 'c': {'f': 4, 'g': 3},
 'd': {},
 'e': {},
 'f': {},
 'g': {}
}

def dfs(start, goal):
 cost = 0
 path = []
 visited = set()
 stack = [(cost, start)]
 while stack:
  cost, current = stack.pop()
  if current == goal:
   path.append(current)
   return cost, path
  if current not in visited:
   visited.add(current)
   path.append(current)
   for x, y in graph.get(current, {}).items():
    stack.append((y + cost, x))
 return float('inf'), None

print(dfs('a', 'g'))
