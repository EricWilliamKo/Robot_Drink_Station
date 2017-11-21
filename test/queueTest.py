from Queue import *


def yoyo(msg):
    print msg


q = Queue()
q.put((yoyo,'shit'))
q.put((yoyo,'fucker'))

a = []
a.append((yoyo,'shit'))
a.append((yoyo,'fucker'))

# while a:
#     yaya = a.pop()
#     func = yaya[0]
#     arg = yaya[1]
#     func(arg)

A = [1,2,3,4,5,6,'a','b','c','d','e','f','g']
B = [7,8,9,10,11,12]
Q = Queue()

def putinqueue(q,l):
    for i in l:
        q.put(i)

# while q:
#     if q.empty():
#         break
#     yaya = q.get()
#     func = yaya[0]
#     arg = yaya[1]
#     func(arg)

if __name__ == '__main__':
    putinqueue(Q,A)
    putinqueue(Q,B)
    print Q.__dict__