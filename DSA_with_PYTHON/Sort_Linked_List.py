def sort(self):
    if not self.head: return
    end = None
    while end != self.head:
        p = self.head
        while p.next != end:
            if p.data > p.next.data:
                p.data, p.next.data = p.next.data, p.data
            p = p.next
        end = p
