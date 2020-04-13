https://leetcode.com/problems/add-two-numbers/submissions/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        move1 = l1
        move2 = l2
        outlist = None
        move3 = None
        flagmove1 = False
        flagmove2 = False
        
        while move1 and move2:
            s = move1.val + move2.val + carry
            carry = s//10
            if not move3:
                outlist = ListNode(s%10)
                move3 = outlist
            else:
                move3.next = ListNode(s%10)
                move3 = move3.next
            move1 = move1.next
            move2 = move2.next
            if not move1:
                flagmove1 = True
            if not move2:
                flagmove2 = True
        
        if flagmove1:
            while move2:
                s = move2.val + carry
                move3.next = ListNode(s%10)
                carry = s//10
                move2 = move2.next
                move3 = move3.next
        if flagmove2:
            while move1:
                s = move1.val + carry
                move3.next = ListNode(s%10)
                carry = s//10
                move1 = move1.next
                move3 = move3.next
                
        if carry != 0:
            move3.next = ListNode(carry)
            
        return outlist