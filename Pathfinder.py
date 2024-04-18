from functools import cmp_to_key
from math import sqrt

# Return player position on the game board
def getPlayerPos(board, me):
	for y in range(len(board)):
		for x in range(len(board[0])):
			if board[y][x] == me:
				return x, y
	return None # not found

# Node class to represent game board as connected Nodes
class Node:
	def __init__(self, x, y, cost=0, heuristic=0):
		self.x = x
		self.y = y
		self.cost = cost
		self.heuristic = heuristic
		self.parent = None
	def __hash__(self):
		return hash((self.x, self.y))
	def __eq__(self, other):
		return self.x==other.x and self.y==other.y
	def __str__(self):
		return f"(x:{self.x} y:{self.y})"
	def __repr__(self):
		return f"(x:{self.x} y:{self.y})"
		#return f"x:{self.x} y:{self.y} c:{self.cost} h:{self.heuristic}"

# Node's heuristics comparator for Nodes sorting
def compByHeuristic(n1:Node, n2:Node):
	if n1.heuristic < n2.heuristic:
		return 1
	elif n1.heuristic == n2.heuristic:
		return 0
	else:
		return -1

# Return list of accessible Nodes
def getNeighbors(n:Node, graph):
	neighbors = []
	# (try > if) more efficient if (except happen < 50%)
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

# Retrace the final shortest path (A->B)
def retracePath(startNode, endNode):
	cleanPath = []
	currentNode = endNode
	while (currentNode != startNode):
		cleanPath.append(currentNode)
		currentNode = currentNode.parent
	cleanPath.reverse()
	return cleanPath

# Core of pathfinding algorithm
def shortestPath(graph, start:Node, target:Node):
	closedList = set()
	openList = []
	openList.append(start)
	while len(openList) > 0:
		openList.sort(key=cmp_to_key(compByHeuristic))
		u = openList.pop()
		closedList.add(u)
		if u.y == target.y: # Quoridor only need 'y' check
			print("targeted !")
			path = retracePath(start, u)
			return path
		for v in getNeighbors(u, graph):
			if v not in closedList:
				newCost = u.cost + 1
				if (newCost < v.cost) or (v not in openList):
					v.cost = newCost
					v.heuristic = v.cost # Dijkstra (simple & effective)
					#v.heuristic = v.cost + abs(target.y - v.y) # QuoridorA* (effective but buggy/strange)
					#v.heuristic = v.cost + sqrt(abs(target.x - v.x)**2 + abs(target.y - v.y)**2) # A* (not adapted for Quoridor)
					v.parent = u
					if v not in openList:
						openList.append(v)
	print("Error no path found")
	return None

# Global function usable in game
def Pathfinder(board, me):
	x, y = getPlayerPos(board, me)
	start = Node(x, y, 0, 0)
	if me == 0.0: # color 1
		end = Node(8, 16) # target DOWN
	elif me == 1.0: # color 2
		end = Node(8, 0) # target UP
	return shortestPath(board, start, end)

# Debug function to display path on game board
def displayPath(board, path):
	table = {0.0:'A', 1.0:'B', 2.0:'.', 3.0:'-', 4.0:'#', 5.0:' '}
	display = [[0]*17 for _ in range(17)]

	for y in range(len(board)):
		for x in range(len(board[0])):
			display[y][x] = table[board[y][x]]
	for n in path:
		display[n.y][n.x] = chr(n.cost+97) # always 1 digit

	for y in range(len(board)):
		for x in range(len(board[0])):
			print(display[y][x], end=' ')
		print('')