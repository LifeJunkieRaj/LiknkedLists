# class LinkedList:
#     def __init__(self, value):
#         self.value = value
#         self.next = None


# def removeDuplicatesFromLinkedList(linkedList):
#     if linkedList == None:
# 		return None
# 	else:
# 		visitedValues = set()
# 		currentNode = linkedList
# 		while currentNode.next != None:
# 			print(currentNode.value)
# 			if currentNode.value not in list(visitedValues):
# 				visitedValues.add(currentNode.value)
# 				currentNode = currentNode.next
# 				if currentNode.next.value == currentNode.value and currentNode.next.next == None:
# 					currentNode.next = None
# 			else:
				

# 				currentNode.value = currentNode.next.value
# 				currentNode.next = currentNode.next.next
#     return linkedList

O(n) time | 0(1) space
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
        
def removeDuplicatesFromLinkedList(linkedList):
    currentNode = linkedList
    while currentNode is not None:
        nextDistinctNode = currentNode.next
        while nextDistinctNode is not None and nextDistinctNode.value == currentNode.value:
            nextDistinctNode = nextDistinctNode.next
            
        currentNode.next = nextDistinctNode
        currentNode = nextDistinctNode
    
    return linkedList