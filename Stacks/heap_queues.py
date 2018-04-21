import heapq

h = [5,2,3,6,0,1,2,4]
heapq.heapify(h)

print(h)

heapq.heappush(h,20)
print(h)
heapq.heappop(h)
print(h)

heapq.heappushpop(h,4)
print(h)

heapq.heapreplace(h,0)
print(h)
