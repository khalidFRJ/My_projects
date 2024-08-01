class Node:
    def __init__(self, data=None , next=None) :
        self.data = data 
        self.next = next 

 
class Linkedlist :
    def __init__(self) :
        self.head = None

        
    def inset_at_begining (self, data ):
        node = Node(data ,self.head)
        self.head = node

    
    def print(self):
        if self.head is None:
          print("the linkedlist is empty ")
          return
        
        list = self.head
        lin_lis_str = ''

        while list :
            lin_lis_str += str(list.data) + ' --> '
            list = list.next

        print(lin_lis_str)



    def insert_at_and(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        list = self.head 
        while list.next:
            list = list.next

        list.next = Node(data, None)


    
    def insert_values(self, data_list ):
        self.head = None
        for data in data_list:
            self.insert_at_and(data)

    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count
    

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.inset_at_begining(data)
            return

        count = 0
        list = self.head
        while list:
            if count == index - 1:
                node = Node(data, list.next)
                list.next = node
                break

            list = list.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1

        

if __name__ == "__main__":
    link_l = Linkedlist()
    link_l.insert_values(["orange", "mango", "banana", "apple"])
    link_l.print()
    link_l.insert_at(2,"juckfruit")
    link_l.print()
    link_l.remove_at(2)
    link_l.print()
    
