import math 
import sys 
import os 

def advance_collatz(i):
    if i % 2 == 0: 
        return i//2
    else: 
        return i*3 + 1
 
def collatz_process(n): 
    # Populate data 
    i = advance_collatz(n)
    collatz_arr = [n, i]

    # Proceed to iterate the collatz process
    while collatz_arr[-1] != 1: 
        i = advance_collatz(i)
        collatz_arr.append(i)

    return collatz_arr     

def build_collatz_tree():
    file_name = os.path.basename(__file__) 
    if len(sys.argv) != 2:
            print(f"Usage: python {file_name} <n>")
            sys.exit(1)
    elif not isinstance(int(sys.argv[1]), int):
        print(f"Usage: python {file_name} <n>. Where <n> is an integer") 
        sys.exit(1)

    # Initialize the data
    N = int(sys.argv[1])
    collatz_tree = {}

    # Run them jewels fast 
    for n in range(1, N+1):
        collatz_tree[n] = collatz_process(n)
    
    print(collatz_tree)

if __name__ == '__main__':  
    build_collatz_tree()