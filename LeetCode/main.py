from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]):

        arr1 = []
        arr2 = []

        while l1:
            arr1.append(int(l1.val))
            l1 = l1.next

        while l2:
            arr2.append(int(l2.val))
            l2 = l2.next

        # sum 2 arrays

        arr1.reverse()
        arr2.reverse()

        num1 = int("".join(map(str, arr1)))
        num2 = int("".join(map(str, arr2)))

        soma = num1 + num2
        soma = soma[::-1]

        head = ListNode(soma[0])
        temp = head

        for i in range(1, len(soma)):
            temp.next = ListNode(soma[i])
            temp = temp.next

        return head
