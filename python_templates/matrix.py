import sys
from os import path
def input():
    return sys.stdin.readline().strip()

    
def solve(n,array):
    # YOUR CODE HERE
    pass

def main():
    # testcases = 1 
    
    testcases = int(input()) # multiple testcases
    for _ in range(testcases):
        n = int(input())
        array = list(map(int,input().split()))
        row, col= list(map(int,input.split()))
        mat=[[int(x) for x in input().split()] for j in range(row)]

        solve(n,array)
        

if __name__ == "__main__":
    if(path.exists('input.txt')):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()
