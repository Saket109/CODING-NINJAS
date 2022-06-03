import queue

# INBUILT QUEUE

# q = queue.Queue()
# q.put(1)
# q.put(2)
# q.put(3)

# while not q.empty():
#     print(q.get())

# INBUILT STACK 

s = queue.LifoQueue()
s.put(2)
s.put(3)
s.put(5)

while not s.empty():
    print(s.get())

    
