# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        remainder=0
        answer= l1
        while(True):
            mid=l1.val+l2.val+remainder
            l1.val= mid%10
            remainder= mid//10
            if not (l1.next and l2.next):
                break
            l1,l2=l1.next,l2.next
        if(l2.next):
            l2= l2.next
            l1.next=l2
            while(True):
                mid=l2.val+remainder
                l2.val= mid%10
                remainder= mid//10
                if not l2.next:
                    break
                l2=l2.next
            if(remainder>0):
                l2.next= ListNode(remainder, None)
        elif(l1.next):
            l1=l1.next
            while(True):
                mid=l1.val+remainder
                l1.val= mid%10
                remainder= mid//10
                if not l1.next:
                    break
                l1= l1.next
            if remainder>0:
                l1.next= ListNode(remainder, None)
        else:
            print('check if both inputs are of equal length if not shit went wrong')
            if (remainder>0):
                l1.next= ListNode(remainder, None)
        return answer
    #def takeCareofRunAway(l1,remaining,remainder):
        