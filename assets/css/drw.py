class Node:
	def __init__(self, left, right)

def solution(T):
	stack = []
	stack.append(T)
	vals = set()
	output = 1
	visited = set()
	curr_depth = 1

	while stack:
		node = stack[-1]
		visited.add(node)
		if node.x in vals:
			output = max(output, curr_depth)
			continue
		else: 
			vals.add(node.x)
			curr_depth += 1

			right_exists = node.r is not None and node.r not in visited
			left_exists = node.l is not None and node.l not in visited
			if (right_exists or node.r is None) or (left_exists or node.l is None):
				vals.remove(node.x)
				stack.pop()
				curr_depth -= 1
				continue
			if right_exists:
					stack.append(node.r)
			if left_exists:
					stack.append(node.l)
	return output




