class Node:
	"""docstring for ClassName"""
	def __init__(self, item):
		self.item = item
		self.next = None


class LinkedList:
	"""docstring for ClassName"""
	def __init__(self):
		self.head = None
		self.tail = None

	def __str__(self):
		out = ""
		cur = self.head
		while cur:
			out += str(cur.item) + '|'
			cur = cur.next
		return out

	def insertBeg(self, item):
		newNode = Node(item)
		if self.head is None:
			self.head = newNode
		else:
			newNode.next = self.head
			self.head = newNode

	def insertEnd(self,item):
		newNode = Node(item)
		cur = self.head
		if self.head is None:
			self.head = newNode
		else:
			while cur.next:
				cur = cur.next
			cur.next = newNode


	def removeNthNode(self,pos):
		curA = self.head
		curB = self.head
		prev = None
		count = 0

		while count < pos:
			curB = curB.next
			count += 1

		while curB:
			prev = curA
			curA = curA.next
			curB = curB.next
		prev.next = curA.next


	def revLinkedList(self):
		cur = self.head
		prev = None

		while cur:
			Next = cur.next 
			cur.next = prev
			prev = cur
			cur = Next
		self.head = prev

	def getSize(self):
		cur = self.head
		length = 0

		while cur:
			cur = cur.next
			length += 1
		return length

	def isPalindrom(self):
		cur = self.head
		lst = []

		while cur:
			lst.append(cur.val)
			cur = cur.next
		return lst[:] == lst[::-1]

class Solutions:
	"""docstring for ClassName"""
	def __init__(self):
		self.head = None

	def getIntersectionNode1(self, list1, list2):
		cur1 = list1.head
		cur2 = list2.head
		length1 = list1.getSize()
		length2 = list2.getSize()
		diff = length1 - length2

		i = 0
		while i < diff:
			i += 1
			if length1 > length2:
				cur1 = cur1.next
			else:
				cur2 = cur2.next


		while cur1 and cur2:
			if cur1.item == cur2.item:
				return str(cur1.item)
			else:
				cur1 = cur1.next
				cur2 = cur2.next

    def getIntersectionNode2(self, A: ListNode, B: ListNode) -> ListNode:
	    S = set()
	    while A != None: A, _ = A.next, S.add(A) 
	    while B != None:
	        if B in S: return B
	        B = B.next


	def revPolishNot(self,rpnlist):
		stack_lst = []

		for i in rpnlist:
			if not i in ['+', '-', '*', '/']:
				stack_lst.append(int(i))
			else:
				a = stack_lst.pop()
				b = stack_lst.pop()
				if i == '+':
					stack_lst.append(a+b)
				elif i == '-':
					stack_lst.append(a-b)
				elif i == '*':
					stack_lst.append(a*b)
				else:
					if a*b < 0 and a%b!= 0:
						stack_lst.append(a//b+1)
					else:
						stack_lst.append(a//b)				
		return stack_lst.pop()

if __name__ == '__main__':
	ll1 = LinkedList()
	ll2 = LinkedList()
	sol = Solutions()

	A = [0,9,1,2,4]
	B = [3,2,4]

	for i in A:
		ll1.insertEnd(i)
	print(ll1)
	for i in B:
		ll2.insertEnd(i)
	print(ll2)

	print(sol.getIntersectionNode(ll1,ll2))

	#print(ll.isPalindromeLinkedList())
	# rpnlist = ["4","-2","/","2","-3","-","-"]
	# lst = sol.revPolishNot(rpnlist)
	# print(lst)

	# A = [4,1,8,4,5]
	# B = [5,0,1,8,4,5]

	# ll1.revLinkedList()
	# print(ll1)

	# ll1.palindromeLinkedList()
	# print(ll1)

	# for i in B:
	# 	ll2.insertEnd(i)
	# print(ll2)

	# ab = sol.getIntersectionNode(ll1,ll2)
	# print(ab)

	# ll1.removeNthNode(3)
	# print(ll1)










		
		