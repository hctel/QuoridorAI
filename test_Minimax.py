from Minimax import *

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

full_input = {
  "players": ["LUR", "HSL"],
  "current": 1,
  "blockers": [0, 0],
   "board": [[2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 0.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [4.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [4.0, 5.0, 4.0, 5.0, 3.0, 5.0, 3.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [4.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0, 5.0, 3.0, 5.0, 3.0, 5.0, 4.0, 5.0, 4.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [4.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 1.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0]]
}

def test_getNeighbors():
	assert getNeighbors(empty_input["board"], x=0, y=0) == [{'type': 'pawn', 'position': [[2, 0]]}, {'type': 'pawn', 'position': [[0, 2]]}]
	assert getNeighbors(empty_input["board"], x=6, y=0) == [{'type': 'pawn', 'position': [[2, 6]]}, {'type': 'pawn', 'position': [[0, 4]]}, {'type': 'pawn', 'position': [[2, 8]]}, {'type': 'pawn', 'position': [[0, 6]]}, {'type': 'pawn', 'position': [[0, 10]]}]
	assert getNeighbors(empty_input["board"], x=6, y=6) == [{'type': 'pawn', 'position': [[4, 6]]}, {'type': 'pawn', 'position': [[8, 6]]}, {'type': 'pawn', 'position': [[6, 4]]}, {'type': 'pawn', 'position': [[6, 8]]}]

def test_getBlockers():
	assert getBlockers(full_input["board"]) == [{'type': 'blocker', 'position': [[7, 4], [7, 6]]}, {'type': 'blocker', 'position': [[13, 10], [13, 12]]}, {'type': 'blocker', 'position': [[6, 5], [8, 5]]}, {'type': 'blocker', 'position': [[6, 7], [8, 7]]}, {'type': 'blocker', 'position': [[6, 15], [8, 15]]}, {'type': 'blocker', 'position': [[12, 1], [14, 1]]}, {'type': 'blocker', 'position': [[12, 9], [14, 9]]}, {'type': 'blocker', 'position': [[12, 11], [14, 11]]}]

def test_moves():
	assert moves(full_input) == [{'type': 'pawn', 'position': [[16, 6]]}, {'type': 'pawn', 'position': [[16, 10]]}]

def test_cleanBoard():
	px, py = getPlayerPos(empty_input["board"], PAWN1)
	new_board = deepcopy(empty_input["board"])
	cleanBoard(new_board, PAWN1)
	assert new_board != empty_input["board"]
	assert empty_input["board"][py][px] == PAWN1
	assert new_board[py][px] == EMPTY_PAWN

def test_applyBoard():
	move = {'type': 'blocker', 'position': [[7, 4], [7, 6]]}
	new_board = deepcopy(empty_input["board"])
	y0 = move['position'][0][0]
	x0 = move['position'][0][1]
	y1 = move['position'][1][0]
	x1 = move['position'][1][1]
	new_board[y0][x0] = BLOCKER
	new_board[y1][x1] = BLOCKER
	new_board2 = applyBoard(empty_input["board"], move)
	assert new_board != empty_input["board"]
	assert new_board2 == new_board

def test_apply():
	move = {'type': 'pawn', 'position': [[0, 6]]}
	new_state = apply(empty_input, move)
	assert new_state != empty_input
	assert empty_input["board"][0][6] == EMPTY_PAWN
	assert new_state["board"][0][6] == PAWN1
	assert new_state["current"] != empty_input["current"]

def test_winner():
	winner_state = deepcopy(empty_input)
	winner_state["board"][0][8] = PAWN2
	winner_state["board"][16][8] = EMPTY_PAWN
	winner_state["board"][15][8] = PAWN1
	assert winner(empty_input) == None
	assert winner(winner_state) == PAWN2

def test_gameOver():
	winner_state = deepcopy(empty_input)
	winner_state["board"][0][8] = PAWN2
	winner_state["board"][16][8] = EMPTY_PAWN
	winner_state["board"][15][8] = PAWN1
	assert gameOver(empty_input) == None
	assert gameOver(winner_state) == True

def test_currentPlayer():
	assert currentPlayer(empty_input) == PAWN1
	assert currentPlayer(full_input) == PAWN2

def test_Manhattan():
	assert Manhattan(empty_input["board"], PAWN1) == 16
	assert Manhattan(empty_input["board"], PAWN2) == 16

def test_heuristic():
	assert heuristic(empty_input, [-10,14,-4,4,5,-5]) == 32
	assert heuristic(empty_input, [-10,0,-1,0,0,0]) == -96
	assert heuristic(full_input, [-10,14,-4,4,5,-5]) == 176
	assert heuristic(full_input, [-10,0,-1,0,0,0]) == -456

def test_smoothFinder():
	assert smoothFinder(empty_input, [-10,14,-4,4,5,-5]) == (36, {'type': 'pawn', 'position': [[2, 8]]})
	assert smoothFinder(empty_input, [-10,0,-1,0,0,0]) == (-84, {'type': 'pawn', 'position': [[2, 8]]})
	assert smoothFinder(full_input, [-10,14,-4,4,5,-5]) == (-446, {'type': 'pawn', 'position': [[16, 10]]})
	assert smoothFinder(full_input, [-10,0,-1,0,0,0]) == (-446, {'type': 'pawn', 'position': [[16, 10]]})