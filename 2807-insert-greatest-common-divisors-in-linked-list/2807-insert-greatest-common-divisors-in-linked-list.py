# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        currentNode = head

        while currentNode.next != None:
            nextNode = currentNode.next
            gcdNode = ListNode(math.gcd(currentNode.val, nextNode.val), nextNode)
            currentNode.next = gcdNode
            currentNode = nextNode

        return head