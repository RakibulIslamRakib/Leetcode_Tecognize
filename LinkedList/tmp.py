class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
    

dataArray = list(map(int,input().split()))

headNode=None;currentNode=None;
for el in dataArray:
    newNode = Node(el)
    if headNode is None:
        headNode = newNode;
        currentNode = newNode;
        continue
    currentNode.next = newNode
    currentNode = currentNode.next

tr = headNode
while True:
    print('Node Data : ',tr.data)
    print('Node Address : ',tr)
    if tr.next is None:
        break
    tr=tr.next

    '''
    9 7 5 3 4
    Node Data :  9
    Node Address :  <__main__.Node object at 0x000002843DD56FD0>
    Node Data :  7
    Node Address :  <__main__.Node object at 0x000002843DD56F10>
    Node Data :  5
    Node Address :  <__main__.Node object at 0x000002843DD56E80>
    Node Data :  3
    Node Address :  <__main__.Node object at 0x000002843DD56E20>
    Node Data :  4
    Node Address :  <__main__.Node object at 0x000002843DD56DC0>
    '''

print('Reversing The List')    

back=None;
while headNode:
    front = headNode.next
    headNode.next=back
    back=headNode
    headNode=front

tr = back
while True:
    print('Node Data : ',tr.data)
    print('Node Address : ',tr)
    if tr.next is None:
        break
    tr=tr.next    
