import math
import time
from Grid               import Grid
from BaseAI             import BaseAI
from EvalFunction 	import EvalFunction


class AlphaBetaPruning(BaseAI):


	INFINITY = 2147483647
	NEG_INFINITY = -2147483646


	def __init__(self):
		self.start_time = time.process_time()
	

	def cutoff_test(self, state, depth):
		return (not state.canMove()) or depth <= 0 or time.process_time() - self.start_time < 0.1


	def get_depth_limit(self, state):
		if len(state.getAvailableCells()) > 5:
			return 3
		else:
			return 5

	def alpha_beta_search(self, state):

		max_v = 0
		action = 0

		for a in state.getAvailableMoves():
			
			temp_state = state.clone()
			temp_state.move(a)

			depth = self.get_depth_limit(temp_state)

			v = self.max_value(temp_state, depth, PlayerAI.NEG_INFINITY, PlayerAI.INFINITY)

			max_v = max(max_v, v)
			if max_v == v: 
				action = a

		return action


	# returns a evaluation_function value
	def max_value(self, state, depth, alpha, beta):

		if self.cutoff_test(state, depth):
			return EvalFunction(state).score
		
		v = PlayerAI.NEG_INFINITY

		for a in state.getAvailableMoves():
			v = max(v, self.min_value(self.Result(True, state, a), depth-1, alpha, beta))

			if v >= beta:
				return v

			alpha = max(alpha, v)

		return v


	# return a evaluation_function value
	def min_value(self, state, depth, alpha, beta):

		if self.cutoff_test(state, depth):
			return EvalFunction(state).score

		v = PlayerAI.INFINITY

		for cell in state.getAvailableCells():
			v = min(v, self.max_value(self.Result(False, state, cell), depth-1, alpha, beta))

			if v <= alpha:
				return v

			beta = min(beta, v)

		return v


	def Result(self, player, state, action):
		
		temp_state = state.clone()

		if player == True:
			temp_state.move(action)

		else:
			temp_state.insertTile(action, 2)
		
		return temp_state

