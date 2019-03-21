class Q:

    def __init__(self):
        self.queue = []

    def put(self, x, priority=0):

        # Insert method to add element

        self.queue.insert(0, x)
        return True

    # Pop method to remove element
    def get(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return ("No elements in Queue!")

    def count(self):
        return len(self.queue)


if __name__ == '__main__':
    x = Q()
    for i in range(20):
        x.put("emailpkt"+str(i))

    for i in range(10):
        x.put("httppkt"+str(i))

    for i in range(5):
        x.put("gamepkt"+str(i))

    for i in range(x.count()):
        print(x.get())

