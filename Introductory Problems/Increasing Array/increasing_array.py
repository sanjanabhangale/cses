n = int(input())
l = list([int(x) for x in input().split()])
count = 0
for i in range(1 , n):
    if l[i-1] > l[i]:
        value = l[i-1]-l[i]
        count = count + value
        l[i] = l[i-1]

print(count)
