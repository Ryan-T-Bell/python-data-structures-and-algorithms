from .priority_queue import PriorityQueue


# !!!! This is not complete yet !!!!
# Need to implement heuristic function in next node selection

class AStarSearch:

	def __init__(self, initial_node):
		
		node = initial_node

		# Leaf nodes of BFS search tree
		frontier = PriorityQueue()
		frontier.insert(node)

		# Already explored nodes in BFS search tree
		explored = []

		while not frontier.is_empty():
			
			node = frontier.pop()
			
			if goal_test(node):	
				return node

			explored.append(node)

			for child in self.expand_node(node):
				if self.check_if_repeat(child, frontier, explored):
					frontier.insert(child)
				else:
					frontier.replace_repeated_entry(child)

	# A Star f(n) = Estimate cost of the cheapest solution through node
	def heuristic_function(self, node):
		g = self.path_cost_to_node(node)
		h = self.est_node_to_goal(node)

		return g + h

	# A Star g(n) = Cost to reach node
	def path_cost_to_node(self, node):
		#TODO: Implement function to evaluate cost from initial state to node
		return False

	# A Star h(n) = Cost to get from node to goal
	def est_node_to_goal(self, node):
		# TODO: Implement function to evaluate cost from node to goal

	def goal_test(self, node):
		# TODO: Implement goal test for node state
		return False


	def expand_node(self, node):
		# TODO: Apply action to node and return list of all children


	# return true if node is in frontier or explored lists
	def check_if_repeat(self, node, frontier, explored):
		in_frontier = frontier.elements.count(node) > 0
		in_explored = explored.count(node) > 0

		return (in_frontier or in_explored)