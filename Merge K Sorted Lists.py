https://leetcode.com/problems/merge-k-sorted-lists/
# My Implementation ....Mehnat 130/131 test cases passed
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        it, out, move, k= 1, None, None, len(lists)
        l = k
        start = 0
        while k > 0:
            if lists[start] == None:
                lists[start] = -1
                k -= 1
                start += 1
                continue
            if lists[start] == -1:
                start += 1
                continue
            m, index, i = lists[start].val, start, start+1
            
            while i < l:
                if lists[i] == None:
                    lists[i] = -1
                    k -= 1
                    i += 1
                    continue
                if lists[i] == -1:
                    i += 1
                    continue
                if lists[i].val < m:
                    m = lists[i].val
                    index = i
                i += 1
                
            if it == 1:
                out = ListNode(m)
                lists[index] = lists[index].next
                move = out
            else:
                move.next = ListNode(m)
                move = move.next
                lists[index] = lists[index].next
            it += 1
                 
        return out        
        