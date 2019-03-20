# System modules
from myQ import Q
from threading import Thread
import time
import random
import matplotlib.pyplot as plt

# these value are in Hz, or # of times per second
kids_datarate = 500
netflix_datarate = 100000
game_datarate = 2000
processing_rate = 20000
num_packets_to_send = 200
done = [False, False, False]

def KidsInternet(q: Q):
    fh = open("kids.txt")
    data = fh.readlines()
    fh.close()
    i = 0
    for line in data:
        d = line.replace("\n",'')
        q.put(d)
        i += 1
        time.sleep(1/kids_datarate)
    done[0] = True

def NetflixInternet(q: Q):
    fh = open("netflix.txt")
    data = fh.readlines()
    fh.close()
    i = 0
    for line in data:
        d = line.replace("\n",'')
        q.put(d)
        i += 1
        time.sleep(1/netflix_datarate)
    done[1] = True


def GameInternet(q: Q):
    fh = open("game.txt")
    data = fh.readlines()
    fh.close()
    i = 0
    for burst in range(3):
        for line in data:
            d = line.replace("\n",'')
            q.put(d)
            i += 1
            time.sleep(1/game_datarate)
        time.sleep(1)
    done[2] = True


network_queue = Q()
kids_thread = Thread(target=KidsInternet, args=(network_queue,))
game_thread = Thread(target=GameInternet, args=(network_queue,))
netflix_thread = Thread(target=NetflixInternet, args=(network_queue,))
kids_thread.start()
game_thread.start()
netflix_thread.start()

x = []
y = []

try:
    t = 0
    while network_queue.count() == 0:
        # wait until there is a packet to process
        time.sleep(1 / 10)
    while True:
        if network_queue.count() > 0:
            pkt = network_queue.get()
            for i in pkt:
                print(i,end='')
            print("")
            time.sleep(1/processing_rate )
            x.append(t)
            t += 1
            y.append(network_queue.count())
        if all(done) is True and network_queue.count() == 0:
            break

    plt.plot(x,y)
    plt.show()

except KeyboardInterrupt:
        print("")
        print("quitting")

print('*** Done')