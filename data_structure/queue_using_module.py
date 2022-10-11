import queue

q = queue.Queue()

q.put(7)
q.put(3)
q.put(1)
q.put(8)
q.put(2)

print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())