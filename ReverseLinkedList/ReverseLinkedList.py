class ListNode(object):
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
    
class Solution(object):
    def reverseList(self,head):
        if head == None :
            return head
        elif head.next == None:
            return head
        else:
            nextNode=head.next
            reverse=reverseList(nextNode)
            nextNode.next=head
            head.next=None
        return reverse