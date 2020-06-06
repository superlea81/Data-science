# LeetCode 02 Add Two Numbers
## [link](https://leetcode.com/problems/add-two-numbers/)


### Python
```
	class Solution:
		def addTwoNumbers(self, l1, l2, c = 0):
			'''
			l1:ListNode
			l2:ListNode
			return:ListNode
			'''
			val = l1.val + l2.val
			c = val // 10           #要进1位还是不进位
			re = ListNode(val % 10)
			
			while(l1.next != None or l2.next != None or c != 0){
				if l1.next = None:
					l1.next = ListNode(0)
				if l2.next = None:
					l2.next = ListNode(0)
				re.next = self.addTwoNumbers(l1.next, l2.next, c)
			}
```