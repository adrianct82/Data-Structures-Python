
# # a = "1 2 3 4 5 6"
# arr = [
#     [1, 2, 3, 4, 5, 6]
# ]

# for n in range(6):
#     if n > 0:
#         arr.append([number + n for number in arr[0]])

# for i in arr:
#     print(i)


# print("\nRESULT")
# print("_________________________________________________________")


# rows = [0,1,2]
# result = []

# for _ in range(4):
#     columns = [[0,1,2],[1],[0,1,2]]

#     for _ in range(4):
#         sums = 0
#         for index,row in enumerate(rows):
#             for column in  columns[index]:
#                 sums += arr[row][column]

#         result.append(sums)                
#         columns = ([[number+1 for number in group1] for group1 in columns])
#     rows = ([number+1 for number in rows])

# print(max(result))


    






# # print(result)



# # for column in range(4):
# #     if column > 0:
# #         columns = ([[number+1 for number in group1] for group1 in columns])
# #     print(columns)
# #     for row in range(4):
# #         if row > 0:
# #             rows = ([number+1 for number in rows])
# #         print(rows)
# #         print("SALIDA")
# #         print(columns[column -1],rows[row - 1])



# # for i in columns:
# #     print(i)
# # print("RESULT")
# # for i in columns:
# #     print(i)



# asteroids = [5,10,-5]
# asteroids = [8, -8]
asteroids = [10, 2, -5]



right = []
left = []

for i in asteroids:
    if i < 0:
        left.append(abs(i))
    else:
        right.append(abs(i))

print(asteroids)
print(right)
print(left)


print("\nRESULT")
print("_________________________________________________________")



# print(right)


# a = (right.pop())
# print(a)
# print(right)




result = []
r = ""
l = ""

for _ in range(len(asteroids)):
    if len(right) > 0 and r is None:
         r = abs(right[-1])
    else:
         r = None

    if len(left) > 0 and l is None:
         l = abs(left[-1])
    else:
         l = None
    
    if r is not None and l is not None:
        # print(33)
        print(r, l)

        if r > l:
            l = None
            left.pop()
            result.append(r)

        elif l > r:
            r = None
            right.pop()
            result.append(l)
        else:
            right.pop()
            left.pop()
    elif r is not None:
        result.append(r)
    elif l is not None:
        result.append(l)



print(asteroids)        

result.reverse()

result = list(set(result))
print (result)
# print (right)
# print (left)



print("_________________________________________________________")


# stack = []
 
# # append() function to push
# # element in the stack
# stack.append('a')
# stack.append('b')
# stack.append('c')
 



# print('Initial stack')
# print(stack)
 
# # pop() function to pop
# # element from stack in
# # LIFO order
# print('\nElements popped from stack:')
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
 
# print('\nStack after elements are popped:')
# print(stack)
 