# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
	
	#O(1) time | O(1) space
    def setHead(self, node):
        if self.head is None:
			self.head = node
			self.tail = node
			return
		self.insertBefore(self.head, node)
	
	# O(1) time | O(1) space
    def setTail(self, node):
        if self.tail is None:
			self.setHead(node)
			return
		self.insertAfter(self.tail, node)

	# O(1) time | O(1) space
    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
			return
		self.remove(nodeToInsert)
		nodeToInsert.prev = node.prev
		nodeToInsert.next = node
		if node.prev is None:
			self.head = nodeToInsert
		else:
			node.prev.next = nodeToInsert
		node.prev = nodeToInsert

	# O(1) time | O(1) space
    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
			return
		self.remove(nodeToInsert)
		nodeToInsert.prev = node
		nodeToInsert.next = node.next
		if node.next is None:
			self.tail = nodeToInsert
		else:
			node.next.prev = nodeToInsert
		node.next = nodeToInsert

	# O(p) time | O(1) space
    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
			self.setHead(nodeToInsert)
			return
		node = self.head
		currentPosition = 1
		while node is not None and currentPosition != position:
			node = node.next
			currentPosition += 1
		if node is not None:
			self.insertBefore(node, nodeToInsert)
		else:
			self.setTail(nodeToInsert)
	
	#O(n) time | O(1) space
    def removeNodesWithValue(self, value):
        node = self.head
		while node is not None:
			nodeToRemove = node
			node = node.next
			if nodeToRemove.value == value:
				self.remove(nodeToRemove)
	
	# O(1) time | O(1) space
    def remove(self, node):
        if (node == self.head):
			self.head = self.head.next
		if (node == self.tail):
			self.tail = self.tail.prev
		self.removeNodeBindings(node)

	# O(n) time | O(1) space
    def containsNodeWithValue(self, value):
		node = self.head
        while node  is not None and node.value is not value:
			node = node.next
		return node is not None
        
	def removeNodeBindings(self, node):
		if node.prev is not None:
			node.prev.next = node.next
		if node.next is not None:
			node.next.prev = node.prev
		node.prev = None
		node.next = None
	
#Notes:
# 1.  containsNodeWithValue(self, value):
# 2.  remove(self, node):
#      -removeNodeBindings(self, node):
# 3.  removeNodesWithValue(self, value):
# 4.  insertBefore(self, node, nodeToInsert):
# 5.  insertAfter(self, node, nodeToInsert):
# 6.  setHead(self, node):
#      -self.insertBefore(self.head, node)
# 7.  setTail(self, node):
#      -self.insertAfter(self.head, node)
# 8.  insertAtPosition(self, position, noteToInsert):	


# Sri's Attempt
# # This is an input class. Do not edit.
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.prev = None
#         self.next = None


# # Feel free to add new properties and methods to the class.
# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def setHead(self, node):
# 		if node.prev !=None or node.next!=None:
# 	        prevNode= node.prev
# 			nextNode= node.next
# 			node.prev=None
# 			node.next=self.head
# 			prevNode.next= nextNode
# 			nextNode.prev= prevNode
# 		self.head = node
		
        

#     def setTail(self, node):
#         self.tail = node
        

#     def insertBefore(self, node, nodeToInsert):
# 		node.prev = nodeToInsert
# 		nodeToInsert.next = node
			
# 		if node.prev==None:
# 			self.setHead(nodeToInsert)
#     	elif (node.prev != None):
# 			previousNode = node.prev
# 			previousNode.next = nodeToInsert
# 			nodeToInsert.prev = previousNode
			
# 	def insertAfter(self, node, nodeToInsert):
# 		node.next = nodeToInsert
# 		nodeToInsert.prev = node
			
# 		if node.next==None:
# 			self.setTail(nodeToInsert)
#         elif (node.next != None):
# 			nextNode = node.next
# 			nextNode.prev = nodeToInsert
# 			nodeToInsert.next = nextNode

#     def insertAtPosition(self, position, nodeToInsert):
#         if (self.head == None and position == 1):
# 			self.setHead(nodeToInsert)
# 		elif self.head!=None and position==1:
# 			self.insertBefore(self.head, nodeToInsert)
# 			self.head= self.head.prev
# 		else:
# 			index=1
# 			node= self.head
# 			while node.next!=None and index<position:
# 				node= node.next
#         	if index== position-1:
# 				self.insertAfter(node,nodeToInsert)

#     def removeNodesWithValue(self, value):
#         if self.head!=None and self.head.value==value:
# 			self.head= self.head.next
# 			if self.head !=None:
# 				self.head.prev=None
# 				index+=1
# 		if self.tail!=None and self.tail.value== value:
# 			self.tail=self.tail.prev
# 			if self.tail!=None:
# 				self.tail.next=None
# 		currentNode= self.head
# 		while currentNode!=self.tail:
# 			currentNode= currentNode.next
# 			if currentNode.value== value:
# 				self.remove(currentNode)

#     def remove(self, node):
#         # Write your code here.
# 		if node==self.head:
# 			self.head= self.head.next
# 			if self.head !=None:
# 				self.head.prev=None
# 		elif node==self.tail:
# 			self.tail=self.tail.prev
# 			if self.tail!=None:
# 				self.tail.next=None
# 		else:
# 			prevNode= node.prev
# 			nextNode= node.next
# 			prevNode.next= nextNode
# 			nextNode.prev= prevNode
# 			node.prev=node.next= None
# 			node= None
					

#     def containsNodeWithValue(self, value):
#         currentNode= self.head
# 		while currentNode.next!=None:
# 			currentNode= node.next
# 			if currentNode.value==value:
# 				return True