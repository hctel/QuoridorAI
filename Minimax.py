from collections import defaultdict
import time,sys,random
from copy import deepcopy
from Pathfinder import  *

import random
from Pathfinder import Pathfinder, getPlayerPos

import sys
sys.setrecursionlimit(9999)

# Board tile values
PAWN1 = 0
PAWN2 = 1
EMPTY_PAWN = 2
EMPTY_BLOCKER = 3
BLOCKER = 4
IMP = 5  # for places where no blockers and pawns can be

empty_input = {
  "players": ["LUR", "HSL"],
  "current": 0,
  "blockers": [10, 10],
   "board": [[2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 0.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
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
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 1.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0]]
}

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
def getNeighbors(board, x, y, stop_recursive=False):
	neighbors = []
	# (try > if) more efficient if (except happen < 50%)
	try:
		if board[y-1][x] == EMPTY_BLOCKER: # up
			move = {'type':"pawn", 'position':[[y-2, x]]}
			if board[y-2][x] == EMPTY_PAWN:
				neighbors.append(move)
			elif not stop_recursive:
				neighbors.extend(getNeighbors(board, x, y-2, stop_recursive=True))
	except:
		pass
	try:
		if board[y+1][x] == EMPTY_BLOCKER: # down
			move = {'type':"pawn", 'position':[[y+2, x]]}
			if board[y+2][x] == EMPTY_PAWN:
				neighbors.append(move)
			elif not stop_recursive:
				neighbors.extend(getNeighbors(board, x, y+2, stop_recursive=True))
	except:
		pass
	try:
		if board[y][x-1] == EMPTY_BLOCKER: # left
			move = {'type':"pawn", 'position':[[y, x-2]]}
			if board[y][x-2] == EMPTY_PAWN:
				neighbors.append(move)
			elif not stop_recursive:
				neighbors.extend(getNeighbors(board, x-2, y, stop_recursive=True))
	except:
		pass
	try:
		if board[y][x+1] == EMPTY_BLOCKER: # right
			move = {'type':"pawn", 'position':[[y, x+2]]}
			if board[y][x+2] == EMPTY_PAWN:
				neighbors.append(move)
			elif not stop_recursive:
				neighbors.extend(getNeighbors(board, x+2, y, stop_recursive=True))
	except:
		pass
	#print(f"neighbors: {neighbors}")
	return neighbors

def getBlockers(board):
	res = []
	for y in range(1, len(board)-1, 2):
		for x in range(0, len(board[0])-4, 2):
			if (board[y][x]==EMPTY_BLOCKER and board[y][x+2]==EMPTY_BLOCKER) and (board[y-1][x+1]==EMPTY_BLOCKER and board[y+1][x+1]==EMPTY_BLOCKER):
				move = {'type':"blocker", 'position':[[y, x], [y, x+2]]} # horizontal
				newBoard = applyBoard(board, move)
				playerPath = Pathfinder(newBoard, PAWN1) # slow
				opponentPath = Pathfinder(newBoard, PAWN2) # slow
				if (playerPath != None) and (opponentPath != None): # ok legal move
					res.append(move)
	for y in range(0, len(board)-4, 2):
		for x in range(1, len(board[0])-1, 2):
			if board[y][x]==EMPTY_BLOCKER and board[y+2][x]==EMPTY_BLOCKER and (board[y+1][x-1]==EMPTY_BLOCKER and board[y+1][x+1]==EMPTY_BLOCKER):
				move = {'type':"blocker", 'position':[[y, x], [y+2, x]]} # vertical
				newBoard = applyBoard(board, move)
				playerPath = Pathfinder(newBoard, PAWN1) # slow
				opponentPath = Pathfinder(newBoard, PAWN2) # slow
				if (playerPath != None) and (opponentPath != None): # ok legal move
					res.append(move)
	#print("len(res) = ", len(res))
	return res

def moves(state):
	p = currentPlayer(state)
	x, y = getPlayerPos(state["board"], p)

	playerMoves = getNeighbors(state["board"], x, y)

	if state["blockers"][p] == 0: # no remaining blockers/walls for this player
		return playerMoves
	
	blockers = getBlockers(state["board"])
	random.shuffle(blockers)

	res = playerMoves + blockers
	return res

# need optimization !
def cleanBoard(board, x, y, player):
	for yc in range(len(board)):
		for xc in range(len(board[0])):
			if board[yc][xc] == player:
				board[yc][xc] = EMPTY_PAWN

def applyBoard(board, move):
	res = deepcopy(board)

	y0 = move['position'][0][0]
	x0 = move['position'][0][1]
	y1 = move['position'][1][0]
	x1 = move['position'][1][1]
	res[y0][x0] = BLOCKER
	res[y1][x1] = BLOCKER

	return res

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
		res["blockers"][player] -= 1
		y0 = move['position'][0][0]
		x0 = move['position'][0][1]
		y1 = move['position'][1][0]
		x1 = move['position'][1][1]
		res["board"][y0][x0] = BLOCKER
		res["board"][y1][x1] = BLOCKER
	
	res["current"] = abs(res["current"]-1) # switch player
	return res

def winner(state):
	_, p1y = getPlayerPos(state['board'], PAWN1)
	_, p2y = getPlayerPos(state['board'], PAWN2)
	if p1y == 16:
		return PAWN1
	if p2y == 0:
		return PAWN2
	return None

def gameOver(state):
	if winner(state) is not None:
		return True
	
def currentPlayer(state):
	return state['current']

def Manhattan(board, pawn):
	x, y = getPlayerPos(board, pawn)
	if pawn == PAWN1:
		return 16-y
	else:
		return y
	

def heuristic(state, weigths, debug=False):
	player = state['current']
	opponent = abs(player-1) # 1->0 & 0->1

	playerManhattan = Manhattan(state["board"], player)
	opponentManhattan = Manhattan(state["board"], opponent)

	if playerManhattan == 0: # win
		return 9999
	if opponentManhattan == 0: # lose
		return -9999
	
	playerPath = Pathfinder(state['board'], player) # slow
	opponentPath = Pathfinder(state['board'], opponent) # slow
	playerDijkstra = len(playerPath)
	opponentDijkstra = len(opponentPath)

	if debug:
		print("playerPath:", playerPath, ", playerDijkstra:", playerDijkstra)
		print("opponentPath:", opponentPath, ", opponentDijkstra:", opponentDijkstra)
	
	playerBlockers = state['blockers'][player]
	opponentBlockers = state['blockers'][opponent]

	res = (weigths[0]*playerDijkstra + weigths[1]*opponentDijkstra + 
		   weigths[2]*playerManhattan + weigths[3]*opponentManhattan +
		   weigths[4]*playerBlockers + weigths[5]*opponentBlockers)
	#print("res: ", res)
	return res

def negamaxWithPruningIterativeDeepening(state, weigths, timeout):
	cache = defaultdict(lambda : 0)
	def cachedNegamaxWithPruningLimitedDepth(state, weigths, depth, start, timeout, alpha=float('-inf'), beta=float('inf')):
		over = gameOver(state)
		if over or depth == 0:
			res = -heuristic(state, weigths), None, over

		else:
			theValue, theMove, theOver = float('-inf'), None, True
			possibilities = [(move, apply(state, move)) for move in moves(state)]
			possibilities.sort(key=lambda poss: cache[tuple(poss[1])])
			
			for move, successor in possibilities:
				value, _, over = cachedNegamaxWithPruningLimitedDepth(successor, weigths, depth-1, start, timeout, -beta, -alpha)

				theOver = theOver and over
				if value > theValue:
					theValue, theMove = value, move
				alpha = max(alpha, theValue)
				if alpha >= beta:
					break
				#if time.time() - start > timeout:
					#break
			res = -theValue, theMove, theOver
		cache[tuple(state)] = res[0]
		return res

	value, move = 0, None
	depth = 1
	start = time.time()
	over = False

	while value > -9999 and time.time() - start < timeout and not over:
		value, move, over = cachedNegamaxWithPruningLimitedDepth(state, weigths, depth, start, timeout)
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
	print('')
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

run(empty_input, [-10,1,0,0,0,0], 0.03, negamaxWithPruningIterativeDeepening)