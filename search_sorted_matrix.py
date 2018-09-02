'''
Given a sorted matrix, horizontally sorted as well as vertically sorted.
Return the index if number if found, else return None

Input:
    2D sorted matrix
    n
Output:
    (i, j) if n is found else return None
'''


'''
    You start from bottom left or top-right
    mean (0, N) or (N, 0).
    Start traversing the matrix from that point and
    move upwards if number is smaller
    and rightward if number is bigger.
'''

def find_element(inp, search):
    N = len(inp[0])
    i,j = 0, N-1
    while(i<N and j>=0):
        val = inp[i][j]
        if val == search:
            return (i, j)
        if val > search:
            j -= 1
        if val < search:
            i += 1
    return -1

if __name__ == '__main__':
    N = int(raw_input())
    inp = []
    for j in range(N):
        inp.append([int(i) for i in raw_input().split(',')])
    
    search = int(raw_input())
    print find_element(inp, search)


