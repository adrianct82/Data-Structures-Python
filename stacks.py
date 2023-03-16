




# print(asteroids)

# print("RIGHT")
# for i in right[::-1]:
#     print(i)


# print("LEFT")
# for i in left[::-1]:
#     print(i)


# print("\nRESULT")
# print(right[-1])
# print(left[-1])


def aster(asteroids):
    res = []
    for asteroid in asteroids:
                # We only need to resolve collisions under the following conditions:
                # - stack is non-empty
                # - current asteroid is -ve
                # - top of the stack is +ve
                while len(res) and asteroid < 0 and res[-1] > 0:
                    # Both asteroids are equal, destroy both.
                    if res[-1] == -asteroid: 
                        res.pop()
                        break
                    # Stack top is smaller, remove the +ve asteroid 
                    # from the stack and continue the comparison.
                    elif res[-1] < -asteroid:
                        res.pop()
                        continue
                    # Stack top is larger, -ve asteroid is destroyed.
                    elif res[-1] > -asteroid:
                        break
                else:
                    # -ve asteroid made it all the way to the 
                    # bottom of the stack and destroyed all asteroids.
                    res.append(asteroid)
    return res    
    # right = []
    # left = []

    # for i in asteroids:
    #     if i < 0:
    #         left.append(abs(i))
    #     else:
    #         right.append(abs(i))

    # if sorted(set(right)) == sorted(set(left)):
    #     return asteroids

    # r = ""
    # l = ""
    # result = []

    # for i in range(4):
    #     if right != []: 
    #         r = right[-1] 
    #     else: 
    #         r = None

    #     if left != []: 
    #         l = left[-1] 
    #     else: 
    #         l = None

        
    #     if l == None and r == None:
    #         return []
        
    #     if l == None:
    #         return right

    #     if r == None:
    #         return left

    #     if  r > l:
    #         left.pop()
    #     elif l > r:
    #         right.pop()
    #     elif l == r:
    #         right.pop()
    #         left.pop()





# asteroids = [5,10,-5]
# asteroids = [8, -8]
# asteroids = [10, 2, -5]

print(aster([5,10,-5]))
print(aster([8, -8]))
print(aster([10, 2, -5]))
print(aster([-2,-1,1,2]))




# print("\nRESULT2")
# print(right)
# print(left)
