class PriorityQ:

    def __init__(self,priorities):
        self.max_priority = priorities
        self.queues = []
        for i in range(priorities):
            self.queues.append([])      # add a new empty list

    def put(self, x, priority=0):
        if priority > self.max_priority:
            priority = self.max_priority

        # Insert method to add element
        self.queues[priority].insert(0, x)
        return True

    # Pop method to remove element
    def get(self):
        i = 0
        while i < self.max_priority:
            if len(self.queues[i]) > 0:
                return self.queues[i].pop()
            i += 1
        return ("No elements in Queue!")

    def count(self,index = -1):
        if index == -1:
            cnt = 0
            for i in range(self.max_priority):
                cnt += len(self.queues[i])
        else:
            cnt = len(self.queues[index])

        return cnt

if __name__ == '__main__':
    x = PriorityQ(3)
    j = 0
    for i in range(20):
        x.put("emailpkt"+str(i), 2)
        j += 2

    for i in range(10):
        x.put("httppkt"+str(i), 1)

    for i in range(5):
        x.put("gamepkt"+str(i), 0)

    for i in range(10):
        print(x.get())

    print("Adding more game packets")
    for i in range(5):
        x.put("gamepkt"+str(i), 0)

    for i in range(15):
        print(x.get())

    print("Adding more http packets")
    for i in range(5):
        x.put("httppkt"+str(i), 0)

    for i in range(25):
        print(x.get())
