class Solution:
    def insertionSortList(self, h):
        if not h or not h.next:
            return h
        d = ListNode(0)
        c = h
        while c:
            nxt = c.next
            p = d
            while p.next and p.next.val < c.val:
                p = p.next
            c.next = p.next
            p.next = c
            c = nxt
        return d.next