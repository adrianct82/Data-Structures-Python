
# # # # # a = "1 2 3 4 5 6"
# # # # arr = [
# # # #     [1, 2, 3, 4, 5, 6]
# # # # ]

# # # # for n in range(6):
# # # #     if n > 0:
# # # #         arr.append([number + n for number in arr[0]])

# # # # for i in arr:
# # # #     print(i)


# # # # print("\nRESULT")
# # # # print("_________________________________________________________")


# # # # rows = [0,1,2]
# # # # result = []

# # # # for _ in range(4):
# # # #     columns = [[0,1,2],[1],[0,1,2]]

# # # #     for _ in range(4):
# # # #         sums = 0
# # # #         for index,row in enumerate(rows):
# # # #             for column in  columns[index]:
# # # #                 sums += arr[row][column]

# # # #         result.append(sums)                
# # # #         columns = ([[number+1 for number in group1] for group1 in columns])
# # # #     rows = ([number+1 for number in rows])

# # # # print(max(result))


    






# # # # # print(result)



# # # # # for column in range(4):
# # # # #     if column > 0:
# # # # #         columns = ([[number+1 for number in group1] for group1 in columns])
# # # # #     print(columns)
# # # # #     for row in range(4):
# # # # #         if row > 0:
# # # # #             rows = ([number+1 for number in rows])
# # # # #         print(rows)
# # # # #         print("SALIDA")
# # # # #         print(columns[column -1],rows[row - 1])



# # # # # for i in columns:
# # # # #     print(i)
# # # # # print("RESULT")
# # # # # for i in columns:
# # # # #     print(i)



# # # # asteroids = [5,10,-5]
# # # # asteroids = [8, -8]
# # # asteroids = [10, 2, -5]



# # # right = []
# # # left = []

# # # for i in asteroids:
# # #     if i < 0:
# # #         left.append(abs(i))
# # #     else:
# # #         right.append(abs(i))

# # # print(asteroids)
# # # print(right)
# # # print(left)


# # # print("\nRESULT")
# # # print("_________________________________________________________")



# # # # print(right)


# # # # a = (right.pop())
# # # # print(a)
# # # # print(right)




# # # result = []
# # # r = ""
# # # l = ""

# # # for _ in range(len(asteroids)):
# # #     if len(right) > 0 and r is None:
# # #          r = abs(right[-1])
# # #     else:
# # #          r = None

# # #     if len(left) > 0 and l is None:
# # #          l = abs(left[-1])
# # #     else:
# # #          l = None
    
# # #     if r is not None and l is not None:
# # #         # print(33)
# # #         print(r, l)

# # #         if r > l:
# # #             l = None
# # #             left.pop()
# # #             result.append(r)

# # #         elif l > r:
# # #             r = None
# # #             right.pop()
# # #             result.append(l)
# # #         else:
# # #             right.pop()
# # #             left.pop()
# # #     elif r is not None:
# # #         result.append(r)
# # #     elif l is not None:
# # #         result.append(l)



# # # print(asteroids)        

# # # result.reverse()

# # # result = list(set(result))
# # # print (result)
# # # # print (right)
# # # # print (left)



# # # print("_________________________________________________________")


# # # # stack = []
 
# # # # # append() function to push
# # # # # element in the stack
# # # # stack.append('a')
# # # # stack.append('b')
# # # # stack.append('c')
 



# # # # print('Initial stack')
# # # # print(stack)
 
# # # # # pop() function to pop
# # # # # element from stack in
# # # # # LIFO order
# # # # print('\nElements popped from stack:')
# # # # print(stack.pop())
# # # # print(stack.pop())
# # # # print(stack.pop())
 
# # # # print('\nStack after elements are popped:')
# # # # print(stack)
 

# # # inte = 14
# # # bina = bin(14)
# # # str = "hola"
# # # str = bina.replace("0b","")

# # # print(str)
# # # print(inte)
# # # print(bina)

# # # str = "111001111010100"

# # # print(max(len(i)) for i in len(str.split("0")))

# # # for i in (str.split("0")):
# # #     print(i)

# # # max(lst, key=len)


# # # inte = 125

# # # print(len(max(bin(inte).replace("0b","").split("0"), key=len)))



# # class Node:
# #     def __init__(self, value):
# #         self.value = value
# #         self.next = None
        

# # class LinkedList:
# #     def __init__(self, value):
# #         new_node = Node(value)
# #         self.head = new_node
# #         self.tail = new_node

        
# #     def append(self, value):
# #         new_node = Node(value)
# #         if self.head == None:
# #             self.head = new_node
# #             self.tail = new_node
# #         else:
# #             self.tail.next = new_node
# #             self.tail = new_node
# #         return True
        
# #     def find_middle_node(self):
# #             slow = self.head
# #             fast = self.head
    
# #             # Move the fast pointer two nodes ahead for every one node that the slow pointer moves ahead
# #             # When the fast pointer reaches the end of the linked list, the slow pointer will be at the middle node
# #             while fast is not None and fast.next is not None:
# #                 slow = slow.next
# #                 fast = fast.next.next
                
                
    
# #             # Return the middle node
# #             return slow
        
        
            
        

# #     # WRITE FIND_MIDDLE_NODE METHOD HERE #
# #     #                                    #
# #     #                                    #
# #     #                                    #
# #     #                                    #
# #     ######################################




# # my_linked_list = LinkedList(1)
# # my_linked_list.append(2)
# # my_linked_list.append(3)
# # my_linked_list.append(4)
# # my_linked_list.append(5)
# # my_linked_list.append(6)
# # my_linked_list.append(7)
# # my_linked_list.append(8)
# # my_linked_list.append(9)
# # my_linked_list.append(10)
# # my_linked_list.append(11)
# # my_linked_list.append(12)
# # my_linked_list.append(1)

# # result = []

# # for i in my_linked_list.len

# # print(my_linked_list)




# # print( my_linked_list.find_middle_node().value )



# # """
# #     EXPECTED OUTPUT:
# #     ----------------
# #     3
    
# # """



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
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.length += 1
#         return True
    
#     def get(self, index):
#         if index < 0 or index >= self.length:
#             return None
#         temp = self.head
#         for _ in range(index):
#             temp = temp.next
#         return temp
    
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

    
#     def remove_duplicates(self):
#         result = []
#         temp = self.head
#         counter = 0
#         while temp.next is not None:
#             if temp.value not in result:
#                 result.append(temp.value)
#                 temp = temp.next
#             else:
#                 temp = temp.next
#                 self.remove(counter)
            
#             counter += 1
#         return True





# my_linked_list = LinkedList(1)
# my_linked_list.append(2)
# my_linked_list.append(3)
# my_linked_list.append(2)
# my_linked_list.append(2)
# my_linked_list.append(5)
# my_linked_list.append(5)
# my_linked_list.append(5)
# my_linked_list.append(4)
# # my_linked_list.remove_duplicates()

# my_linked_list.print_list()


# """
#     EXPECTED OUTPUT:
#     ----------------
#     1
#     2
#     3
#     4
    
# """


Blocks = [
    {
    "gym": False,
    "school": True,
    "store": False,
    },
    {
    "gym": True,
    "school": False,
    "store": False, 
    },
    {
    "gym": True,
    "school": True,
    "store": False, 
    },
    {
    "gym": False,
    "school": True,
    "store": False,
    },
    {
    "gym": False,
    "school": True,
    "store": True, 
},
]
Reqs = ["gym", "school", "store"]
# //gymdist, schooldist, result

print(Blocks[1])
print(Blocks[1]["gym"])
print(Blocks[1]["school"])
print(Blocks[1]["store"])

print("***********************")

result = []

for i in Blocks:
    temp = []
    n = ""
    for j in Reqs:
        # print(Blocks[])
        if i[j]: 
            n = 0 
        else: 
            n = 1
        temp.append(n)
    result.append(temp)

print(result)


for index,n in enumerate(result):
    for index2,j in enumerate(n):
        print(n, j, result[index + 1][index2])

# for i in result[0]:
#     print(i)


