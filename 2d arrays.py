
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


    

lis = [1, 2, 3, 4, 10, 11]

print(lis)
x = 0
print(sum(lis))