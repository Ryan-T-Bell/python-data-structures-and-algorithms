from .priority_queue import PriorityQueue

class UniformCostSearch:

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

			for child in expand_node(node):
				if check_if_repeat(child, frontier, explored):
					frontier.insert(child)
				else:
					frontier.replace_repeated_entry(child)


	def goal_test(node):
		# TODO: Implement goal test for node state
		return False


	def expand_node(node):
		# TODO: Apply action to node and return list of all children


	# return true if node is in frontier or explored lists
	def check_if_repeat(node, frontier, explored):
		in_frontier = frontier.elements.count(node) > 0
		in_explored = explored.count(node) > 0

		return in_frontier or in_explored