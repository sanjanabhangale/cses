def main():
    n = int(input())
    weirdalgo(n)

def weirdalgo(n):
    print(n)
    if n==1:
        return
    else:
        if(int(n)%2==0):
            weirdalgo(int(n/2))
        else:
            weirdalgo(int(n)*3+1)

if __name__ == "__main__":
    main()
