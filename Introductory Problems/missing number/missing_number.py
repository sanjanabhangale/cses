#optimised solution
# use sets when concerned with unique value
n = int(input())
a = set([int(x) for x in input().split()])
b = set([int(x) for x in range(1, n + 1)])
# j = iter(b-a) i.e to iterate b-a set.
# next is to print next value in that set.
print(next(iter(b-a)))


# first solution
# n = int(input())
# arr = list(map(int, input().strip().split()))
# arr.sort()
# flag = 0
# i=0
# while i in range(0,n-1) :
#     if arr[i] != i+1:
#         flag = 1
#         print(i+1)
#         break
#     i=i+1
# if flag == 0:
#     print(n)
