def Insertion_Lin(self,data):
    node=Node(data)
    node.next=self.head
    self.head=node

    # Inserion at begining of linked list