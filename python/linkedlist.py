class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

class SLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next

    def insertSLL(self,value,location):
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            if location==0:
                newNode.next=self.head
                self.head=newNode
            elif location==-1:                
                newNode.next=None
                self.tail.next=newNode
                self.tail=newNode
            else:
                tempNode=self.head
                index=0
                while index<location-1:
                    tempNode=tempNode.next
                    index+=1
                nextNode=tempNode.next
                tempNode.next=newNode
                newNode.next=nextNode
                if tempNode==self.tail:
                    self.tail=newNode
    #traverse Singly Linked List 
    def traverseSLL(self):
        if self.head is None:
            print("The Singly Linked List does not exist")
        else:
            node=self.head
            while node is not None:
                print(node.value)
                node=node.next

    def searchSLL(self,nodeValue):
        if self.head is None:
            return "The list does not exist"
        else:
            node=self.head
            while node is not None:
                if node.value==nodeValue:
                    return node.value
                node=node.next
            return "The value does not exist in the list"

    def deleteNode(self,location):
        if self.head is None:
            print("The SLL does not exist")
        else:
            if location==0:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
            elif location==-1:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    node=self.head
                    while node is not None:
                        if node.next==self.tail:
                            break
                        node =node.next
                    node.next=None
                    self.tail=node
            else:
                tempNode=self.head
                index=0
                while index<location-1:
                    tempNode=tempNode.next
                    index+=1
                nextNode=tempNode.next
                tempNode.next=nextNode.next

    def deleteEntireSLL(self):
        if self.head is None:
            print("The SLL does not exist")
        else:
            self.head=None
            self.tail=None







singlyLinkedList=SLinkedList()
node1=Node(1)
node2=Node(2)

singlyLinkedList.head=node1
singlyLinkedList.head.next=node2
singlyLinkedList.tail=node2

singlyLinkedList.insertSLL(4,-1)
singlyLinkedList.insertSLL(0,0)

singlyLinkedList.insertSLL(10,2)

print([node.value for node in singlyLinkedList])

singlyLinkedList.traverseSLL()

print(singlyLinkedList.searchSLL(110))
print([node.value for node in singlyLinkedList])
singlyLinkedList.deleteNode(0)
singlyLinkedList.deleteNode(-1)

print([node.value for node in singlyLinkedList])

singlyLinkedList.deleteEntireSLL()
print([node.value for node in singlyLinkedList])
