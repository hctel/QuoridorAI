from collections import defaultdict
import time
from copy import deepcopy

import random
from Pathfinder import Pathfinder, getPlayerPos

import sys
sys.setrecursionlimit(9999)

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
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 4.0, 2.0, 4.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 4.0, 2.0, 4.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 4.0, 5.0, 4.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 1.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0]]
}

# Return list of accessible cells
def getNeighbors(board, x, y):
	neighbors = []
	# (try > if) more efficient if (except happen < 50%)
	try:
		if (board[y-1][x] == 3.0) and (board[y-2][x] == 2.0): # up
			move = {'type':"pawn", 'position':[[y-2, x]]}
			neighbors.append(move)
	except:
		pass
	try:
		if (board[y+1][x] == 3.0) and (board[y+2][x] == 2.0): # down
			move = {'type':"pawn", 'position':[[y+2, x]]}
			neighbors.append(move)
	except:
		pass
	try:
		if (board[y][x-1] == 3.0) and (board[y][x-2] == 2.0): # left
			move = {'type':"pawn", 'position':[[y, x-2]]}
			neighbors.append(move)
	except:
		pass
	try:
		if (board[y][x+1] == 3.0) and (board[y][x+2] == 2.0): # right
			move = {'type':"pawn", 'position':[[y, x+2]]}
			neighbors.append(move)
	except:
		pass
	#print(f"neighbors: {neighbors}")
	return neighbors

def getBlockers(board):
	res = []
	for y in range(0, len(board)-2, 2):
		for x in range(0, len(board[0])-4, 2):
			if board[y][x+1]==3 and board[y][x+3]==3:
				move = {'type':"blocker", 'position':[[y, x+1], [y, x+3]]}
				res.append(move)
	for y in range(0, len(board)-4, 2):
		for x in range(0, len(board[0])-2, 2):
			if board[y+1][x]==3 and board[y+3][x]==3:
				move = {'type':"blocker", 'position':[[y+1, x], [y+3, x]]}
				res.append(move)

def moves(state):
	p = currentPlayer(state)
	x, y = getPlayerPos(state["board"], p)

	playerMoves = getNeighbors(state["board"], x, y)
	blockers = getBlockers(state["board"])
	random.shuffle(blockers)
	
	res = playerMoves + blockers
	return res

# need optimization !
def cleanBoard(board, x, y, player):
	for yc in range(len(board)):
		for xc in range(len(board[0])):
			if board[yc][xc] == player:
				board[yc][xc] = 2 # empty cell

def apply(state, move):
	player = currentPlayer(state)
	res = deepcopy(state)

	t = move['type']
	if t == "pawn":
		y = move['position'][0][0]
		x = move['position'][0][1]
		cleanBoard(res["board"], x, y, player)
		res["board"][y][x] = player
	elif t == "blocker":
		y0 = move['position'][0][0]
		x0 = move['position'][0][1]
		y1 = move['position'][1][0]
		x1 = move['position'][1][1]
		res["board"][y0][x0] = 4 # wall cell
		res["board"][y1][x1] = 4 # wall cell
	
	res["current"] = abs(res["current"]-1) # switch player
	return res

def winner(state):
	p = currentPlayer(state)
	x, y = getPlayerPos(state['board'], p)
	if p == 0.0 and y == 16:
		return 0.0
	if p == 1.0 and y == 0:
		return 1.0
	return None

def gameOver(state):
	if winner(state) is not None:
		return True
	
def currentPlayer(state):
	return state['current']

def heuristic(state, weigths):
	player = state['current']
	opponent = abs(player-1) # 1->0 & 0->1
	
	playerMoves = len(Pathfinder(state['board'], player)) # slow
	opponentMoves = len(Pathfinder(state['board'], opponent)) # slow

	if playerMoves == 0:
		return 999
	if opponentMoves == 0:
		return -999
	
	playerBlockers = state['blockers'][player]
	opponentBlockers = state['blockers'][opponent]

	res = weigths[0]*playerMoves + weigths[1]*opponentMoves + weigths[2]*playerBlockers + weigths[3]*opponentBlockers
	#print("res: ", res)
	return res

def negamaxWithPruningIterativeDeepening(state, weigths, timeout):
	cache = defaultdict(lambda : 0)
	def cachedNegamaxWithPruningLimitedDepth(state, weigths, depth, alpha=float('-inf'), beta=float('inf')):
		over = gameOver(state)
		if over or depth == 0:
			res = -heuristic(state, weigths), None, over

		else:
			theValue, theMove, theOver = float('-inf'), None, True
			possibilities = [(move, apply(state, move)) for move in moves(state)]
			#print("before : ", possibilities)
			possibilities.sort(key=lambda poss: cache[tuple(poss[1])])
			#print("after : ", possibilities)
			for move, successor in reversed(possibilities):
				value, _, over = cachedNegamaxWithPruningLimitedDepth(successor, weigths, depth-1, -beta, -alpha)
				theOver = theOver and over
				if value > theValue:
					theValue, theMove = value, move
				alpha = max(alpha, theValue)
				if alpha >= beta:
					break
			res = -theValue, theMove, theOver
		cache[tuple(state)] = res[0]
		return res

	value, move = 0, None
	depth = 1
	start = time.time()
	over = False
	# replace -9 with a precise value ?
	while value > -9 and time.time() - start < timeout and not over:
		value, move, over = cachedNegamaxWithPruningLimitedDepth(state, weigths, depth)
		#print('value : ', value)
		depth += 1

	print('depth =', depth)
	return value, move

def timeit(fun):
	def wrapper(*args, **kwargs):
		start = time.time()
		res = fun(*args, **kwargs)
		print('Executed in {}s'.format(time.time() - start))
		return res
	return wrapper

@timeit
def next(state, weigths, timeout, fun):
	_, move = fun(state, weigths, timeout)
	return move

def show(board):
	table = {0.0:'A', 1.0:'B', 2.0:'.', 3.0:'-', 4.0:'#', 5.0:' '}
	display = [[0]*17 for _ in range(17)]

	for y in range(len(board)):
		for x in range(len(board[0])):
			display[y][x] = table[board[y][x]]

	for y in range(len(board)):
		for x in range(len(board[0])):
			print(display[y][x], end=' ')
		print('')

def run(state, weigths, timeout, fun):
	show(state['board'])
	while not gameOver(state):
		move = next(state, weigths, timeout, fun)
		print(move)
		state = apply(state, move)
		show(state['board'])

# Network will call this function during game
def calculate(state, weigths, timeout):
	return next(state, weigths, timeout, negamaxWithPruningIterativeDeepening)

run(test_input, [-1,1,0,0], 0.2, negamaxWithPruningIterativeDeepening)
