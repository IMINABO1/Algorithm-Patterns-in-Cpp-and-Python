import sys
from os import path
def input():
    return sys.stdin.readline().strip()

def SieveOfEratosthenes(num):
    prime = [True for i in range(num+1)]
    primes=[]
# boolean array
    p = 2
    while (p * p <= num):
 
        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):
 
            # Updating all multiples of p
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1
 
    # Print all prime numbers
    for p in range(2, num+1):
        if prime[p]:
            primes.append(p)
    return primes

    
def solve(n,array):
    # YOUR CODE HERE
    pass

def main():
    # testcases = 1 
    
    testcases = int(input()) # multiple testcases
    for _ in range(testcases):
        n = int(input())
        array = list(map(int,input().split()))
        solve(n,array)
        

if __name__ == "__main__":
    if(path.exists('input.txt')):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    main()
