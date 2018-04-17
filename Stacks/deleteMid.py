
def deleteMid(s, i, n):
    if not s or i == n:
        return

    x = s[-1]
    s.pop()

    deleteMid(s, i+1, n)
    if i != int(n/2):
        s.append(x)
    


s = [1,2,3,4,5,6,7,8]
deleteMid(s, 0, len(s))
print('printing elements in the array after deletion:', s)
