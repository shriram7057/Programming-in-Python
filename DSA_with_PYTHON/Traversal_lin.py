def traversal_linked_list(self):
    temp=self.head
    while temp:
        print(temp.data,end='->')
        temp=temp.next
    print('None')