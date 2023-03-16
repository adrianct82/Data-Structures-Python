


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
    
#     def r_insert(self, index, value):
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
# # # HASH TABLE
# # # --------------------------------------------------------------------


# # # HASH TABLE CONSTRUCTOR

# # class Node:
# #     def __init__(self, value):
# #         self.value = value
# #         self.left = None
# #         self.right = None

# class HashTable:
#     def __init__(self, size = 7):
#         self.data_map = [None] * size

#     def __hash(self,key):
#         my_hash = 0
#         for letter in key:
#             my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
#         return my_hash
    
#     def print_table(self):
#         for i, val in enumerate(self.data_map):
#             print(i, ":", val)

#     def set_item(self, key, value):
#         index = self.__hash(key)
#         if self.data_map[index] == None:
#             self.data_map[index] = []
#         self.data_map[index].append([key, value])

#     def get_item(self, key):
#         index = self.__hash(key)
#         if self.data_map[index] is not None:
#             for i in range(len(self.data_map[index])):
#                 if self.data_map[index][i][0] == key:
#                     return self.data_map[index][i][1]
#         return None
    
#     def keys(self):
#         all_keys = []
#         for i in range(len(self.data_map)):
#             if self.data_map[i] is not None:
#                 for j in range(len(self.data_map[i])):
#                     all_keys.append(self.data_map[i][j][0])
#         return all_keys




# print("RESULTS \n______________________________________________________________________\n")

# my_hash_table = HashTable()

# my_hash_table.set_item('bolts', 1400)
# my_hash_table.set_item('washers', 50)
# my_hash_table.set_item('lumber', 70)

# my_hash_table.print_table()

# print("\n TWO")

# print(my_hash_table.get_item("bolts"))
# print(my_hash_table.get_item("washers"))
# print(my_hash_table.get_item("lumber"))

# print("\n THREE")
# print(my_hash_table.keys())

# print("\n______________________________________________________________________")


# # FIRST APROACH, THE WORST ONE
# def item_in_common_1(list1, list2):
#     for i in list1:
#         for j in list2:
#             if i == j:
#                 return True
#     return False


# list1 = [1,3,5]
# list2 = [2,4,5]

# print(item_in_common_1(list1, list2))



# # SECOND APROACH, THE BEST ONE
# def item_in_common_2(list1, list2):
#     my_dict = {}
#     for i in list1:
#         my_dict[i] = True
#     for j in list2:
#         if j in my_dict:
#             return True
#     return False
        


# list1 = [1,3,5]
# list2 = [2,4,5]

# print(item_in_common_1(list1, list2))




# # # # --------------------------------------------------------------------
# # # # GRAPH
# # # # --------------------------------------------------------------------


# # # # GRAPH CONSTRUCTOR

# class Graph:
#     def __init__(self):
#         self.adj_list = {}
    
#     def print_graph(self):
#         for vertex in self.adj_list:
#             print(vertex, ':', self.adj_list[vertex])

#     def add_vertex(self, vertex):
#         if vertex not in self.adj_list.keys():
#             self.adj_list[vertex] = []
#             return True
#         return False
    
#     def add_edge(self, v1, v2):
#         if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
#             self.adj_list[v1].append(v2)
#             self.adj_list[v2].append(v1)
#             return True
#         return False
    
#     def remove_edge(self, v1, v2):
#         if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
#             try:
#                 self.adj_list[v1].remove(v2)
#                 self.adj_list[v2].remove(v1)
#             except ValueError:
#                 pass
#             return True
#         return False
    
#     def remove_vertex(self, vertex):
#         if vertex in self.adj_list.keys():
#             for other_vertex in self.adj_list[vertex]:
#                 self.adj_list[other_vertex].remove(vertex)
#             del self.adj_list[vertex]
#             return True
#         return False




    

# # my_graph = Graph()

# # my_graph.add_vertex('A')
# # my_graph.add_vertex('B')
# # my_graph.add_vertex('C')
# # my_graph.add_vertex('D')

# # my_graph.add_edge('A', 'B')
# # my_graph.add_edge('B', 'C')
# # my_graph.add_edge('C', 'A')

# # my_graph.print_graph()
        
# # print("\n TWO")

# # my_graph.remove_edge('A', 'B')
# # my_graph.remove_edge('A', 'D')
# # my_graph.print_graph()

# print("RESULTS \n______________________________________________________________________\n")


# my_graph = Graph()

# my_graph.add_vertex('A')
# my_graph.add_vertex('B')
# my_graph.add_vertex('C')
# my_graph.add_vertex('D')

# my_graph.add_edge('A', 'B')
# my_graph.add_edge('A', 'C')
# my_graph.add_edge('A', 'D')
# my_graph.add_edge('B', 'D')
# my_graph.add_edge('C', 'D')


# my_graph.print_graph()
        
# print("\n TWO")

# my_graph.remove_vertex('D')
# my_graph.print_graph()

# print("\n______________________________________________________________________")


# # RECURSION

# def funcThree():
#     print("Three")



# def funcTwo():
#     funcThree()
#     print("Two")



# def funcOne():
#     funcTwo()
#     print("One")

# funcOne()




# # # # --------------------------------------------------------------------
# # # # RECURSION
# # # # --------------------------------------------------------------------


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

# print(factorial(4))



# # --------------------------------------------------------------------
# # BINARY SEARCH TREE
# # --------------------------------------------------------------------


# # BINARY SEARCH TREE CONSTRUCTOR

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
    
    def contains(self, value):
        temp = self.root
        while(temp is not None):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
            
        return False
    


# # # # --------------------------------------------------------------------
# # # # TREE TRAVERSAL
# # # # --------------------------------------------------------------------

    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)
        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results
    
    def dfs_pre_order(self):
        results = []

        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return results
    

    def dfs_post_order(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)

        traverse(self.root)
        return results
    
    def dfs_in_order(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return results
    
    
# print("______________________________________________________________________")
    

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

# print(my_tree.BFS())
# print(my_tree.dfs_pre_order())
# print(my_tree.dfs_post_order())
print(my_tree.dfs_in_order())

# my_tree.insert(2)
# my_tree.insert(1)
# my_tree.insert(3)

# print(my_tree.root.value)
# print(my_tree.root.left.value)
# print(my_tree.root.right.value)

# print("TWO")
# print(my_tree.contains(4))

# print("______________________________________________________________________")




# # # # --------------------------------------------------------------------
# # # # RECURSIVE BINARY SEARCH TREES
# # # # --------------------------------------------------------------------

#     def __r_contains(self, current_node, value):
#         if current_node == None:
#             return False
#         if value == current_node.value:
#             return True
#         if value < current_node.value:
#             return self.__r_contains(current_node.left, value)
#         if value > current_node.value:
#             return self.__r_contains(current_node.right, value)

#     def r_contains(self, value):
#         return self.__r_contains(self.root, value)
    
#     def __r_insert(self, current_node, value):
#         if current_node == None:
#             return Node(value)
#         if value < current_node.value:
#             current_node.left = self.__r_insert(current_node.left, value)
#         if value > current_node.value:
#             current_node.right = self.__r_insert(current_node.right, value)
#         return current_node
    
#     def r_insert(self, value):
#         if self.root == None:
#             self.root = Node(value)
#         self.__r_insert(self.root, value)
    
#     def min_value(self, current_node):
#         while current_node.left is not None:
#             current_node = current_node.left
#         return current_node.value
    
#     def print_tree(self):
#         current_node = self.root
        
#         print(current_node.value)
#         l = current_node.left
#         r = current_node.right
#         print (l.value, r.value)
#         while l.left is not None or l.right is not None or r.left is not None or r.right is not None:
#             print(l.left.value, l.right.value, r.left.value, r.right.value)
#             break

#     def __delete_node(self, current_node, value):
#         if current_node == None:
#             return None
#         if value < current_node.value:
#             current_node.left = self.__delete_node(current_node.left, value)
#         elif value > current_node.value:
#             current_node.right = self.__delete_node(current_node.right, value)
#         else:
#             if current_node.left == None and current_node.right == None:
#                 return None
#             elif current_node.left == None:
#                 current_node = current_node.right
#             elif current_node.right == None:
#                 current_node = current_node.left
#             else:
#                 sub_tree_min = self.min_value(current_node.right)
#                 current_node.value = sub_tree_min
#                 current_node.right = self.__delete_node(current_node.right, sub_tree_min)
#         return current_node
    

#     def delete_node(self, value):
#         self.__delete_node(self.root, value)
        
    


# # my_tree = BinarySearchTree()
# # my_tree.insert(47)
# # my_tree.insert(21)
# # my_tree.insert(76)
# # my_tree.insert(18)
# # my_tree.insert(27)
# # my_tree.insert(52)
# # my_tree.insert(82)

# # my_tree.print_tree()



# # print(my_tree.min_value(my_tree.root))
# # print(my_tree.min_value(my_tree.root.right))


# # my_tree.r_insert(47)
# # my_tree.r_insert(21)
# # my_tree.r_insert(76)
# # my_tree.r_insert(18)
# # my_tree.r_insert(27)
# # my_tree.r_insert(52)
# # my_tree.r_insert(82)


# # print(my_tree.r_contains(6))
# # print(my_tree)

# my_tree = BinarySearchTree()
# my_tree.r_insert(2)
# my_tree.r_insert(1)
# my_tree.r_insert(3)

# print("Root:", my_tree.root.value)
# print("Root --> Left:", my_tree.root.left.value)
# print("Root --> Right:", my_tree.root.right.value)


# print("\n DELETE")

# my_tree.delete_node(2)

# print("Root:", my_tree.root.value)
# print("Root --> Left:", my_tree.root.left.value)
# print("Root --> Right:", my_tree.root.right)




# # # # --------------------------------------------------------------------
# # # # BASIC SORTS
# # # # --------------------------------------------------------------------


def bubble_sort(my_list):
    for i in range(len(my_list) -1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list

def selection_sort(my_list):
    for i in range(len(my_list) - 1):
        min_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list

def insertion_sort(my_list):
    for i in range(1,len(my_list)):
        temp = my_list[i]
        j = i-1
        while temp < my_list[j] and j >-1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list


def merge(list1, list2):
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined


def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    mid_index = int(len(my_list)/2)
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])

    return merge(left, right)


def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp

def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index+1, end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index

def quick_sort_helper(my_list, left, right):
    if left < right:
        pivot_index =  pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index-1)
        quick_sort_helper(my_list, pivot_index+1, right)
    return my_list

def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list)-1)



# my_list = [4,6,1,7,3,2,5]
# print(my_list)
# # print(pivot(my_list, 0, 6))
# print(quick_sort(my_list))
# print(my_list)

# my_list = [4, 2, 6, 5, 1, 3]
# print(my_list)
# # print(bubble_sort(my_list))
# # print(selection_sort(my_list))
# print(insertion_sort(my_list))


# print(merge([1,2,7,8],[3,4,5,6]))

# list1 = [3,1,4,2]
# print(merge_sort(list1))
# print(list1)



