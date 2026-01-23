import sys
 
input = sys.stdin.readline
 
def read_int():
    return int(input())
 
def invr():
    return list((map(int,input().split())))
 
def insr():
    s = input()
 
    return (list(s[:len(s) - 1]))
 
t = read_int()

for _ in range(t):
    a = invr()
    
    square = True
    
    for i in range(3):
        if (a[i] != a[i+1]):
            square = False
            break
    
    if (not square):
        print("NO")
    
    else:
        print("YES")