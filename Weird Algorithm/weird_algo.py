n = int(input())
while n!=1:
    print(n)
    if n%2==0:
        n = n//2
    else:
        n = n * 3 +1
print(n)

# def main():
#     n = int(input())
#     weirdalgo(n)

# def weirdalgo(n):
#     print(n)
#     if n==1:
#         return
#     elif(int(n)%2==0):
#         weirdalgo(int(n/2))
#     else:
#         weirdalgo(int(n)*3+1)

# if __name__ == "__main__":
#     main()