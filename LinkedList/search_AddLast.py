class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next = next 

class LinkedList:
    def __init__(self,head,tail,size=0):
        self.head=head
        self.tail=tail

    def insert(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = self.tail.next

    def search(self,data):
        runner = self.head
        while runner:
            if runner.data == data:
                return runner
            runner = runner.next  
        return None                  
    def travers(self):
        runner = self.head
        while runner:
            print(f'Node is in {runner} and data is {runner.data}')
            runner = runner.next        

linkedList1 = LinkedList(None,None,0) 
listInput = map(int,input().split())

for item in listInput:
    linkedList1.insert(item)

linkedList1.travers()

item = int(input('Enter A value To search : '))
searchResult  = linkedList1.search(item)
if searchResult != None:
    print(f'The Node Is in {searchResult} and The data is {searchResult.data}')
else:
    print("Node Doesn't exist")    




  


        