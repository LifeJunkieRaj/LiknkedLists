# Average: O(log(n)) time | O(log(n)) space
# Worst: O(n) time | O(n) space
# Recursive Search
def findClosestValueInBst(tree, target):
    return findClosestValueInBSTHelper(tree, target, tree.value)

def findClosestValueInBSTHelper(tree, target, closest):
	if tree is None:
		return closest
	if abs(target - closest) > abs(target - tree.value):
		closest = tree.value
	if target < tree.value:
		return findClosestValueInBSTHelper(tree.left, target, closest)
	elif target > tree.value:
		return findClosestValueInBSTHelper(tree.right, target, closest)
	else:
		return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Average: O(log(n)) time | O(n) space
# Worst: O(n) time | O(1) space
# Iterative Search
def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, tree.value)


def findClosestValueInBstHelper(tree, target, closest):
	currentNode = tree
	while currentNode is not None:
		if abs(target - closest) > abs(target - currentNode.value):
			closest = currentNode.value
		if target < currentNode.value:
			currentNode = currentNode.left
		elif target > currentNode.value:
			currentNode = currentNode.right
		else:
			break
	return closest
		
	
# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None