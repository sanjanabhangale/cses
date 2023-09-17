s = str(input())
l = 1
sub =1
for i in range(1, int(len(s))):
    if s[i] == s[i-1]:
        l = l + 1
    else:
        l = 1

    if l > sub :
        sub = l
print(sub)
