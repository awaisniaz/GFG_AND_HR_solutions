class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtFront(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            temp = self.head
            self.head = newNode
            self.head.next = temp
    def insertAtMiddle(self,data,key):
        newNode = Node(data)
        if(self.head == None):
            self.head = newNode
        else:
            temp = self.head
            while(temp):
                if(temp.data == key):
                    currentLoc = temp.next
                    temp.next = newNode
                    newNode.next = currentLoc
                temp = temp.next
    def searchElement(self,key):
        temp = self.head
        while(temp):
            if(temp.data == key):
                print("Element Found")
                # break;
                return
            temp = temp.next
        print("Element Not Found")

    def visitLinkedlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp  = temp.next
    def lengthOfElement(self):
        count = 0
        temp = self.head
        while(temp):
            count = count+1
            temp = temp.next
        return count

    def reverseLinkedLIst(self):



if __name__=="__main__":
    ll  = LinkedList()
    ll.insertAtFront(50)
    ll.insertAtFront(46)
    # ll.visitLinkedlist()
    ll.insertAtFront(56)
    ll.insertAtFront(78)
    ll.searchElement(100)
    ll.insertAtMiddle(100,46)
    ll.searchElement(100)
    print(ll.lengthOfElement())


    ll.visitLinkedlist()



