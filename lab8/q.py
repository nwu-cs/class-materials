import queue

############ put on the left, get from the right ##################
def q_put(q,x):
    q.insert(0,x)   # insert this item at index 0,
                    # which effectively slides all other items right one

def q_get(q):
    if len(q) > 0:
        return q.pop()  # return the right most item
    else:
        return None     # return nothing

############ put on the right, get from the left ##################
def q_put2(q,x):
    q.append(x)   # insert this item at index 0,
                    # which effectively slides all other items right one

def q_get2(q):
    if len(q) > 0:
        result = q[0]
        q.remove(result)       # now make the queue just the items to the right of the one we grabbed
        return result  # return the right most item
    else:
        return None     # return nothing


q = []
# method 1
q_put(q,"pkt0")
q_put(q,"pkt1")
q_put(q,"pkt2")
q_put(q,"pkt3")

print(q_get(q))
print(q_get(q))
print(q_get(q))
print(q_get(q))
print(q_get(q))

###############################################
# method 2
q_put2(q,"pkt0")
q_put2(q,"pkt1")
q_put2(q,"pkt2")
q_put2(q,"pkt3")

print(q_get2(q))
print(q_get2(q))
print(q_get2(q))
print(q_get2(q))
print(q_get2(q))
##############################################
q2 = queue.Queue()
q2.put_nowait("p")
q2.put_nowait("a")
q2.put_nowait("c")
q2.put_nowait("k")
q2.put_nowait("e")
q2.put_nowait("t")
print(q2.get_nowait())
print(q2.get_nowait())
print(q2.get_nowait())
print(q2.get_nowait())
print(q2.get_nowait())
print(q2.get_nowait())
print(q2.get_nowait())
print(q2.get_nowait())






