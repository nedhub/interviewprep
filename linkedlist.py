#Every Node has 2 parts. data and a pointer to the next Node

#Attributes


#root- pointer to the beginning of the Lis
#size- number of the nodes in List



#Operations: find(data) add(data) remove(data) print_list()




#add operation




class Node:



    def __init__ (self, d, n=None, p=None):
        self.data = d
        self.next_node = n
        self.prev_node = p



    def __str__ (self):
        return ('(' + str(self.data) + ')')






class LinkedList:

    def __init__(self, r = None):
        self.root = r
        self.size = 0



    def add(self,d):
        new__node = Node(d, self.root)
        self.root = new__node
        self.size += 1



    def find(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                return d

            else:
                this_node = this_node.next_node
        return None



    def remove(self, d):
        this_node = self.root
        prev_node = None

        while this_node is not None:
            if this_node.data == d:
                if prev_node is not None:
                    prev_node.next_node = this_node.next_node
                else:
                    self.root = this_node.next_node
                
                self.size -=1
                return True
            else:
                prev_node = this_node
                this_node = this_node.next_node

        return False




    def print_list(self):
        this_node = self.root
        while this_node is not None:
            print(this_node, end='->')
            this_node = this_node.next_node

        print('None')



#Advantage over regular (singly) linked lists


#Ideal for modelling continuosly looping objects, such as a Monopoly board or a race track.
class CircularLinkedList:
    
    def __init__ (self, r = None):
                self.root = r
                self.size = 0



    def add (self, d):
        if self.size == 0:
            self.root = Node(d)
            self.root.next_node = self.root

        else:
            new_node = Node (d, self.root.next_node)
            self.root.next_node = new_node

        self.size += 1



    def find (self, d):
        this_node = self.root
        while True:
            if this_node.data == d:
                return d
            elif this_node.next_node == self.root:
                return False

            this_node = this_node.next_node


    def remove (self, d):
        this_node = self.root
        prev_node = None


        while True:
            if this_node.data == d: #found
                if prev_node is not None:
                    prev_node.next_node = this_node.next_node

                else:
                    while this_node.next_node != self.root:
                        this_node = this_node.next_node
                    this_node.next_node = self.root.next_node
                    self.root = self.root.next_node
                self.size -=1
                return True # data removed
            elif this_node.next_node == self.root:
                return False # data not found
            prev_node = this_node
            this_node = this_node.next_node 



    def print_list (self):
        if self.root is None:
            return
        this_node = self.root
        print (this_node, end='->')
        while this_node.next_node != self.root:
            this_node = this_node.next_node
            print (this_node, end='->')
        print()



class DoublyLinkedList:

    def __init__ (self, r = None):
        self.root = r
        self.last = r
        self.size = 0



    def add (self, d):
        if self.size == 0:
            self.root = Node(d)
            self.last = self.root



        else:
            new_node = Node(d, self.root)
            self.root.prev_node = new_node
            self.root = new_node
        self.size += 1



    def find (self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                return d
            elif this_node.next_node == None:
                return False
            else:
                this_node = this_node.next_node


    def remove (self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                if this_node.prev_node is not None:
                    if this_node.next_node is not None: # delete a middle 
                        this_node.prev_node.next_node = this_node.next_node
                        this_node.next_node.prev_node = this_node.prev_node
                    else:
                        this_node.prev_node.next_node = None
                        self.last = this_node.prev_node

                else:
                    self.root = this_node.next_node
                    this_node.next_node.prev_node = self.root
                self.size -= 1
                return True # data removed

            else:
                this_node = this_node.next_node

        return False # data not found


    def print_list (self):
        if self.root is None:
            return
        this_node = self.root
        print (this_node, end='->')
        while this_node.next_node is not None:
            this_node = this_node.next_node
            print (this_node, end="->")
        print()











































myList = LinkedList()
myList.add(5)
myList.add(8)
myList.add(12)
myList.print_list()



print("size="+str(myList.size))
myList.remove(8)
print("size="+str(myList.size))
print(myList.find(5))
print(myList.root)


cll = CircularLinkedList()
for i in [5,7,3,8,9]:
    cll.add(i)




    print("size="+str(cll.size))
    print(cll.find(8))
    print(cll.find(12))




    my_node = cll.root
    print (my_node, end="->")
    for i in range(8):
        my_node = my_node.next_node
        print (my_node, end="->")
    print()



    cll.print_list()
    cll.remove(8)
    print(cll.remove(15))
    print("size="+str(cll.size))
    cll.remove(5)
    cll.print_list()


    #Doubly Linked List


    #Advantages over egular (singly) linked lis
    #Can iterate the list in either direction
    #Can delete a node without iterating through the list (if given a pointer to the node)




#Doubly Linked Lisr Test Code

dll = DoublyLinkedList()
for i in [5,9,3,8,9]:
    dll.add(i)


print("size="+str(dll.size))
dll.print_list()
dll.remove(8)
print("size="+str(dll.size))


print(dll.remove(15))
print(dll.find(15))
dll.add(21)
dll.add(22)
dll.remove(5)
dll.print_list()
print(dll.last.prev_node)
















    





