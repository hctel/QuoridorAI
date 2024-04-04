from functools import cmp_to_key

test_input = {
  "players": ["LUR", "HSL"],
  "current": 0,
  "blockers": [10, 10],
   "board": [[2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 0.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 4.0, 5.0, 4.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 1.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0]]
}

def getPlayerPos(board, me):
	for y in range(len(board)):
		for x in range(len(board[0])):
			if board[y][x] == me:
				return x, y
	return None

class Node:
	def __init__(self, x, y, cost=0, heuristic=0):
		self.x = x
		self.y = y
		self.cost = cost
		self.heuristic = heuristic
	def __eq__(self, other):
		return self.x==other.x and self.y==other.y
	def __str__(self):
		return f"(x:{self.x} y:{self.y})"
	def __repr__(self):
		return f"(x:{self.x} y:{self.y})"
		#return f"x:{self.x} y:{self.y} c:{self.cost} h:{self.heuristic}"

def compByHeuristic(n1:Node, n2:Node):
	if n1.heuristic < n2.heuristic:
		return 1
	elif n1.heuristic == n2.heuristic:
		return 0
	else:
		return -1
	
def getNeighbors(n:Node, graph):
	neighbors = []
	# (try > if) car plus efficace si (except < 50%)
	try:
		if (graph[n.y-1][n.x] == 3.0) and (graph[n.y-2][n.x] == 2.0): # up
			neighbors.append(Node(n.x, n.y-2))
	except:
		pass
	try:
		if (graph[n.y+1][n.x] == 3.0) and (graph[n.y+2][n.x] == 2.0): # down
			neighbors.append(Node(n.x, n.y+2))
	except:
		pass
	try:
		if (graph[n.y][n.x-1] == 3.0) and (graph[n.y][n.x-2] == 2.0): # left
			neighbors.append(Node(n.x-2, n.y))
	except:
		pass
	try:
		if (graph[n.y][n.x+1] == 3.0) and (graph[n.y][n.x+2] == 2.0): # right
			neighbors.append(Node(n.x+2, n.y))
	except:
		pass
	#print(f"neighbors: {neighbors}")
	return neighbors

def isInListWithInferiorCost(v, openList):
	for n in openList:
		if v.x==n.x and v.y==n.y and n.cost<v.cost: #tester dans quel sens mettre la consition < ou >
			return True
	return False

def shortestPath(graph, target:Node, start:Node):
	closedList = []
	openList = []
	openList.append(start)
	while len(openList) > 0:
		openList.sort(key=cmp_to_key(compByHeuristic))
		u = openList.pop()
		#if (u.x == target.x) and (u.y == target.y):
		if u.y == target.y: # Qoridor only need 'y' check
			print("targeted !")
			closedList.append(u)
			path = closedList
			return path
		for v in getNeighbors(u, graph):
			#if not(v in closedList):
			if not( (v in closedList) or (isInListWithInferiorCost(v, openList)) ):
				v.cost = u.cost + 1
				v.heuristic = v.cost + abs(target.y - v.y) # A*
				#v.heuristic = v.cost # Dijkstra
				openList.append(v)
		closedList.append(u)
	print("Error no path found")
	return None

def A_Star(board, me):
	x, y = getPlayerPos(board, me)
	start = Node(x, y, 0, 0)
	if me == 0.0: # color 1
		end = Node(8, 16) # target DOWN
	elif me == 1.0: # color 2
		end = Node(8, 0) # target UP
	return shortestPath(board, end, start)

def displayPath(board, path):
	table = {0.0:'A', 1.0:'B', 2.0:'.', 3.0:'-', 4.0:'#', 5.0:' '}
	display = [[0]*17 for _ in range(17)]

	for y in range(len(board)):
		for x in range(len(board[0])):
			display[y][x] = table[board[y][x]]
	for n in path:
		display[n.y][n.x] = n.cost%10 # always 1 digit

	for y in range(len(board)):
		for x in range(len(board[0])):
			print(display[y][x], end=' ')
		print('')