


# class Cookie:
#     def __init__(self, color):
#         self.color = color
    
#     def get_color(self):
#         return self.color
    
#     def set_color(self, color):
#         self.color = color



# cookie_one = Cookie('green')
# cookie_two = Cookie('blue')


# print('Cookie one is ', cookie_one.get_color())
# print('Cookie two is ', cookie_two.get_color())

# cookie_one.set_color('yellow')

# print('\nCookie one is now ', cookie_one.get_color())
# print('Cookie two is still ', cookie_two.get_color())

    

# num1 = 11

# num2 = num1

# num2 = 11
# print("num1 =", num1)
# print("num2 =", num2)

# print("num1 points to:", id(num1))
# print("num2 points to:", id(num2))


# dict1 = {'value': 11}

# dict2 = dict1
# print(dict1)
# print(dict2)

# print(id(dict1))
# print(id(dict2))

# dict2['value'] = 22

# print(dict1)
# print(dict2)

# print(id(dict1))
# print(id(dict2))





# list = ["a", "b", "c"]

# print(id(list))
# print(id(list[0]))
# print(id(list[1]))
# print(id(list[2]))


# LINKED LIST UNDER THE HOOD


# head = {
#     "value": 11,
#     "next": {
#             "value": 3,
#             "next": {
#                     "value": 23,
#                     "next": {
#                             "value": 7,
#                             "next":  None
#                             }
#                     }
#            }
#         }


# print(head["next"]["next"]["value"])




# # --------------------------------------------------------------------
# # LINKED LISTS
# # --------------------------------------------------------------------


# # LINKED LIST CONSTRUCTOR

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None


# class LinkedList:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1

#     def print_list(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next
    
#     def append(self, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.length += 1
#         return True
    
#     def pop(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         pre = self.head
#         while(temp.next):
#             pre = temp
#             temp = temp.next
#         self.tail = pre
#         self.tail.next = None
#         self.length -= 1
#         if self.length == 0:
#             self.head = None
#             self.tail = None
#         return temp.value
    

#     def prepend(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node
#         self.length += 1
#         return True
    
#     def pop_first(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         self.head = self.head.next
#         temp.next = None
#         self.length -= 1
#         if self.length == 0:
#             self.tail = None
#         return temp.value
    
#     def get(self, index):
#         if index < 0 or index >= self.length:
#             return None
#         temp = self.head
#         for _ in range(index):
#             temp = temp.next
#         return temp
    

#     def set_value(self, index, value):
#         temp = self.get(index)
#         if temp:
#             temp.value = value
#             return True
#         return False
    
#     def insert(self, index, value):
#         if index < 0 or index > self.length:
#             return None
#         if index == 0:
#             return self.prepend(value)
#         if index == self.length:
#             return self.append(value)
#         new_node = Node(value)
#         temp = self.get(index - 1)
#         new_node.next = temp.next
#         temp.next = new_node
#         self.length += 1
#         return True
    

#     def remove(self, index):
#         if index < 0 or index >= self.length:
#             return None
#         if index == 0:
#             return self.pop_first()
#         if index == self.length - 1:
#             return self.pop()
#         pre = self.get(index - 1)
#         temp = pre.next
#         pre.next = temp.next
#         temp.next = None
#         self.length -= 1
#         return temp

        
#     def reverse(self):
#         temp = self.head
#         self.head = self.tail
#         self.tail = temp
#         after = temp.next
#         before = None
#         for _ in range(self.length):
#             after = temp.next
#             temp.next = before
#             before = temp
#             temp = after
            

    

# print("______________________________________________________________________")
        


# # TEST
# my_linked_list = LinkedList(2)
# my_linked_list.append(3)
# my_linked_list.append(4)
# my_linked_list.prepend(1)


# # print("ONE")

# # my_linked_list.print_list()


# # print("TWO")
# # my_linked_list.print_list()

# # print("THREE")
# # # my_linked_list.pop_first()
# # # my_linked_list.pop_first()
# # # my_linked_list.pop_first()
# # my_linked_list.print_list()

# # print("FOUR")
# # print(my_linked_list.get(3))

# # print("FOUR")
# # my_linked_list.print_list()
# # my_linked_list.set_value(2,11)
# # print("FIVE")
# # my_linked_list.print_list()


# # print("SIX")
# # my_linked_list.remove(7,44444)
# # my_linked_list.print_list()

# # REVERSE
# my_linked_list.print_list()
# my_linked_list.reverse()
# print("REVERSE")
# my_linked_list.print_list()





# # print(my_linked_list.pop())
# # print(my_linked_list.pop())
# # print(my_linked_list.pop())

# # print("original")
# # my_linked_list.print_list()


# # print("after")
# # my_linked_list.pop()
# # my_linked_list.print_list()


# # # print("after")
# # my_linked_list.pop()
# # my_linked_list.print_list()


# print("______________________________________________________________________")





# # --------------------------------------------------------------------
# # DOUBLE LINKED LISTS
# # --------------------------------------------------------------------


# # DOUBLE LINKED LIST CONSTRUCTOR

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#         self.prev = None


# class DoublyLinkedList:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1

#     def print_list(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next
#     def append(self, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             new_node.prev = self.tail
#             self.tail = new_node
#         self.length += 1
#         return True
    
#     def pop(self):
#         if self.length == 0:
#             return None
#         temp = self.tail
#         if self.length == 1:
#             self.head = None
#             self.tail = None
#         else:
#             self.tail = self.tail.prev
#             self.tail.next = None
#             temp.prev = None
#         self.length -= 1
#         return temp
    
#     def prepend(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head.prev = new_node
#             self.head = new_node
#         self.length += 1
#         return True
        
#     def pop_first(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         if self.length == 1:
#             self.head = None
#             self.tail = None
#         else:
#             self.head = self.head.next
#             self.head.prev = None
#             temp.next = None
#         self.length -= 1
#         return temp   

#     def get(self, index):
#         if index < 0 or index >= self.length:
#             return None
#         temp = self.head
#         if index < self.length/2:
#             for _ in range(index):
#                 temp = temp.next
#         else:
#             temp = self.tail
#             for _ in range(self.length - 1,index, -1):
#                 temp = temp.prev
#         return temp
    
#     def set_value(self, index, value):
#         temp = self.get(index)
#         if temp:
#             temp.value = value
#             return True
#         return False
    
#     def insert(self, index, value):
#         if index < 0 or index > self.length:
#             return None
#         if index == 0:
#             return self.prepend(value)
#         if index == self.length:
#             return self.append(value)
#         new_node = Node(value)
#         before = self.get(index - 1)
#         after = before.next
#         new_node.prev = before
#         new_node.next = after
#         before.next = new_node
#         after.prev = new_node
#         self.length += 1
#         return True
         
#     def remove(self, index):
#         if index < 0 or index >= self.length:
#             return None
#         if index == 0:
#             return self.pop_first()
#         if index == self.length - 1:
#             return self.pop()
#         temp = self.get(index)
#         before = temp.prev
#         after = temp.next
#         before.next = after
#         after.prev = before
#         temp.next = None
#         temp.prev = None
#         self.length -= 1
#         return temp
        
    
        

#         # self.tail = pre
#         # self.tail.next = None
#         # self.length -= 1

#         # return temp.value
    
    

# print("______________________________________________________________________")
# print("")

# my_doubly_linked_list = DoublyLinkedList(2)

# my_doubly_linked_list.append(3)
# my_doubly_linked_list.append(4)
# my_doubly_linked_list.append(5)

# # my_doubly_linked_list.pop()
# # my_doubly_linked_list.pop()

# # print("ONE")

# # my_doubly_linked_list.print_list()


# my_doubly_linked_list.prepend(1)


# # print("TWO")
# # my_doubly_linked_list.print_list()

# # my_doubly_linked_list.pop_first()
# # my_doubly_linked_list.pop_first()
# # my_doubly_linked_list.pop_first()
# # my_doubly_linked_list.pop_first()
# # my_doubly_linked_list.pop_first()

# # print(my_doubly_linked_list.get(5))
# # my_doubly_linked_list.insert(6,11)

# my_doubly_linked_list.remove(5)

# my_doubly_linked_list.print_list()




# # --------------------------------------------------------------------
# # STACK
# # --------------------------------------------------------------------


# # STACK CONSTRUCTOR

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
        
# class Stack:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.top = new_node
#         self.height = 1
    
#     def print_stack(self):
#         temp = self.top
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next
    
#     def push(self, value):
#         new_node = Node(value)
#         if self.height > 0:
#             new_node.next = self.top
#         self.top = new_node
#         self.height += 1
#         return True
    
#     def pop(self):
#         if self.height == 0:
#             return None
#         temp = self.top
#         self.top = temp.next
#         temp.next = None
#         self.height -= 1
#         return temp
            

# print("______________________________________________________________________")
    
# my_stack = Stack(7)


# my_stack.push(1)
# my_stack.push(2)


# my_stack.print_stack()

# print("TWO")
# my_stack.pop()
# my_stack.print_stack()


# print("THREE")
# my_stack.pop()
# my_stack.print_stack()



# print("______________________________________________________________________")





# # --------------------------------------------------------------------
# # STACK
# # --------------------------------------------------------------------


# # STACK CONSTRUCTOR

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
        
# class Queue:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.first = new_node
#         self.last = new_node
#         self.length = 1

#     def print_queue(self):
#         temp = self.first
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next
    
#     def enqueue(self, value):
#         new_node = Node(value)
#         if self.first is None:
#             self.first = new_node
#         else:
#             self.last.next = new_node
#         self.last = new_node
#         self.length += 1
#         return True
    
#     def dequeue(self):
#         if self.first is None:
#             return None
#         temp = self.first
#         self.first = temp.next
#         temp.next = None
#         self.length -= 1
#         if self.length == 0:
#             temp.last = None
#         return temp



# print("______________________________________________________________________")

# my_queue = Queue(4)

# my_queue.enqueue(33)
# my_queue.enqueue(11)
# my_queue.enqueue(12)
# my_queue.print_queue()

# print("TWO")
# my_queue.dequeue()
# my_queue.dequeue()
# my_queue.print_queue()

# print("______________________________________________________________________")




# # # --------------------------------------------------------------------
# # # BINARY SEARCH TREE
# # # --------------------------------------------------------------------


# # # BINARY SEARCH TREE CONSTRUCTOR

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# class BinarySearchTee:
#     def __init__(self):
#         self.root = None

#     def insert(self, value):
#         new_node = Node(value)
#         if self.root is None:
#             self.root = new_node
#             return True
#         temp = self.root
#         while (True):
#             if new_node.value == temp.value:
#                 return False
#             if new_node.value < temp.value:
#                 if temp.left is None:
#                     temp.left = new_node
#                     return True
#                 temp = temp.left
#             else:
#                 if temp.right is None:
#                     temp.right = new_node
#                     return True
#                 temp = temp.right
    
#     def contains(self, value):
#         temp = self.root
#         while(temp is not None):
#             if value < temp.value:
#                 temp = temp.left
#             elif value > temp.value:
#                 temp = temp.right
#             else:
#                 return True
            
#         return False
# print("______________________________________________________________________")
    

# my_tree = BinarySearchTee()

# my_tree.insert(2)
# my_tree.insert(1)
# my_tree.insert(3)

# print(my_tree.root.value)
# print(my_tree.root.left.value)
# print(my_tree.root.right.value)

# print("TWO")
# print(my_tree.contains(4))

# print("______________________________________________________________________")




# # --------------------------------------------------------------------
# # HASH TABLE
# # --------------------------------------------------------------------


# # HASH TABLE CONSTRUCTOR

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self,key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None




print("RESULTS \n______________________________________________________________________\n")

my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
# my_hash_table.set_item('lumber', 70)

my_hash_table.print_table()

print("\n TWO")

print(my_hash_table.get_item("bolts"))
print(my_hash_table.get_item("washers"))
print(my_hash_table.get_item("lumber"))


print("\n______________________________________________________________________")

