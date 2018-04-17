def push_item(x,A):
    A.append((x,min(getmin(A),x)))

def getmin(A):
    if len(A) == 0:
        return None
    else:
        return A[-1][1]

def pop_item(A):
    A.pop()

def top(A):
    if len(A) == 0:
        return -1
    else:
        return A[-1][0]

    
def min_stack(operations):
    A = []
    B = []
    for i in range(len(operations)):
        if operations[i] > 0:
            push_item(operations[i],A)
        elif operations[i] <= -1:
            pop_item(A)
        else:
             B.append(top(A))
    return B

if __name__ == "__main__":
 
    operations_size = int(input())

    operations = []
    for _ in range(operations_size):
        operations_item = int(input())
        operations.append(operations_item)
    res = min_stack(operations)
    print(res)
    
