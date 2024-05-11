import time, random
from copy import deepcopy
from Pathfinder import  *

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

# Return the list of accessible cells
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

	return neighbors

# Return the move's list of valid blockers
def getBlockers(board):
	res = []
	for y in range(1, len(board)-1, 2):
		for x in range(0, len(board[0])-2, 2):
			if (board[y][x]==EMPTY_BLOCKER and board[y][x+2]==EMPTY_BLOCKER) and not (board[y-1][x+1]==BLOCKER and board[y+1][x+1]==BLOCKER):
				move = {'type':"blocker", 'position':[[y, x], [y, x+2]]} # horizontal
				newBoard = applyBoard(board, move)
				playerPath = Pathfinder(newBoard, PAWN1) # slow
				opponentPath = Pathfinder(newBoard, PAWN2) # slow
				if (playerPath != None) and (opponentPath != None): # ok legal move
					res.append(move)
	for y in range(0, len(board)-2, 2):
		for x in range(1, len(board[0])-1, 2):
			if (board[y][x]==EMPTY_BLOCKER and board[y+2][x]==EMPTY_BLOCKER) and not (board[y+1][x-1]==BLOCKER and board[y+1][x+1]==BLOCKER):
				move = {'type':"blocker", 'position':[[y, x], [y+2, x]]} # vertical
				newBoard = applyBoard(board, move)
				playerPath = Pathfinder(newBoard, PAWN1) # slow
				opponentPath = Pathfinder(newBoard, PAWN2) # slow
				if (playerPath != None) and (opponentPath != None): # ok legal move
					res.append(move)
	#print("len(res) = ", len(res))
	return res

# Return the list of valid moves (player + blockers)
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

# Remove player from (local) board
def cleanBoard(board, player):
	for yc in range(len(board)):
		for xc in range(len(board[0])):
			if board[yc][xc] == player:
				board[yc][xc] = EMPTY_PAWN

# Apply a blocker move
def applyBoard(board, move):
	res = deepcopy(board)

	y0 = move['position'][0][0]
	x0 = move['position'][0][1]
	y1 = move['position'][1][0]
	x1 = move['position'][1][1]
	res[y0][x0] = BLOCKER
	res[y1][x1] = BLOCKER

	return res

# Apply any move (player or blocker) and switch player
def apply(state, move):
	player = currentPlayer(state)
	res = deepcopy(state)

	t = move['type']
	if t == "pawn":
		y = move['position'][0][0]
		x = move['position'][0][1]
		cleanBoard(res["board"], player)
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

# Return the winner
def winner(state):
	_, p1y = getPlayerPos(state['board'], PAWN1)
	_, p2y = getPlayerPos(state['board'], PAWN2)
	if p1y == 16:
		return PAWN1
	if p2y == 0:
		return PAWN2
	return None

# Return the end of game condition
def gameOver(state):
	if winner(state) is not None:
		return True

# Return the current player that must play
def currentPlayer(state):
	return state['current']

# Return the manhattan (direct) distance
def Manhattan(board, pawn):
	x, y = getPlayerPos(board, pawn)
	if pawn == PAWN1:
		return 16-y
	else:
		return y

# Return the score of a board state from the current player's perspective
def heuristic(state, weigths, debug=False):
	# player and opponent are switched cause "apply()" already change "current"
	opponent = state['current']
	player = abs(opponent-1) # 1->0 & 0->1

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

# Core of best move searching algorithm
def smoothFinder(state, weigths):
	local_weigths = list(weigths)
	p = state["current"]
	if state["blockers"][p] == 0:
		# Just run to the end
		local_weigths = [-10,0,-1,0,0,0]

	value, move = 0, None
	theValue, theMove = float('-inf'), None
	possibilities = [(move, apply(state, move)) for move in moves(state)]

	for move, successor in possibilities:
		value = heuristic(successor, local_weigths)
		if value > theValue:
			theValue, theMove = value, move

	return theValue, theMove

# Timing decorator
def timeit(fun):
	def wrapper(*args, **kwargs):
		start = time.time()
		res = fun(*args, **kwargs)
		print('Executed in {}s'.format(time.time() - start))
		return res
	return wrapper

# Call the algorithm and return the move
@timeit
def next(state, weigths, fun):
	_, move = fun(state, weigths)
	return move

# Debug function to display game board
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

# Runner to test and debug in local
def run(state, weigths, fun):
	import hashlib

	show(state['board'])
	m = hashlib.sha256()
	m.update(str(state["board"]).encode("utf-8"))
	print(m.hexdigest())
	print('')
	while not gameOver(state):
		move = next(state, weigths, fun)
		print(move)
		state = apply(state, move)
		show(state['board'])
		m = hashlib.sha256()
		m.update(str(state["board"]).encode("utf-8"))
		print(m.hexdigest())
		if input("?") == "p":
			print(state["board"])
		print('------------')

# Global function usable in game
# Network class will call this function during game
def calculate(state, weigths):
	return next(state, weigths, smoothFinder)

#run(empty_input, [-10,14,-4,4,-5,5], smoothFinder)