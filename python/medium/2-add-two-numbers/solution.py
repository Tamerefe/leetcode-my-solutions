class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        while l1:
            list1.append(l1.val)
            l1 = l1.next

        list2 = []
        while l2:
            list2.append(l2.val)
            l2 = l2.next

        value1 = int(''.join(map(str, list1[::-1])))
        value2 = int(''.join(map(str, list2[::-1])))
        num = value1 + value2
        valueLast = [int(d) for d in str(num)][::-1]

        lastlist = ListNode(0)
        cur = lastlist
        for l in valueLast:
            cur.next = ListNode(l)
            cur = cur.next
        return lastlist.next
        