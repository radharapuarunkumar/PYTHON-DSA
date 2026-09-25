class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked:
    def __init__(self, data=None):
        self.head = Node(data) if data is not None else None

    def big(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new
        return True
    def las(self,data):
        cn=Node(data)
        if cn.next==None:
            cn.head=new
            
            return True
    def traversal(self):
        cn = self.head
        while cn is not None:
            print(cn.data)
            cn = cn.next
        print("None")

# Example Usage
li = Linked()
li.big(10)
li.big(13)
li.big(2)
li.las(4)
li.traversal()
# Output: 2->13->10->None
