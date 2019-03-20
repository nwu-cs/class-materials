# System modules
import queue
from threading import Thread
import time
import random
import matplotlib.pyplot as plt
from myPriQ import PriorityQ



# these value are in Hz, or # of times per second
kids_datarate = 20
netflix_datarate = 10
game_datarate = 50
processing_rate = 50
num_packets_to_send = 200
done = [False, False, False]

def KidsInternet(q: PriorityQ):
    fh = open("kids.txt")
    data = fh.readlines()
    fh.close()
    i = 0
    while i < num_packets_to_send:
        for line in data:
            d = line.replace("\n",'')
            q.put(d,2)
            i += 1
            time.sleep(1/kids_datarate)
        time.sleep(1)
    done[0] = True

def NetflixInternet(q: PriorityQ):
    try:
        fh = open("netflix.txt")
        data = fh.readlines()
        fh.close()
    except FileNotFoundError:

    i = 0
    while i < num_packets_to_send:
        for line in data:
            d = line.replace("\n",'')
            q.put(d,1)
            i += 1
            time.sleep(1/netflix_datarate)
    done[1] = True

def GameInternet(q: PriorityQ):
    fh = open("game.txt")
    data = fh.readlines()
    fh.close()
    i = 0
    while i < num_packets_to_send:
        for line in data:
            d = line.replace("\n",'')
            q.put(d)
            i += 1
            #time.sleep(1/game_datarate)
        time.sleep(5)
    done[2] = True


network_queue = PriorityQ(3)
kids_thread = Thread(target=KidsInternet, args=(network_queue,))
game_thread = Thread(target=GameInternet, args=(network_queue,))
netflix_thread = Thread(target=NetflixInternet, args=(network_queue,))
kids_thread.start()
game_thread.start()
netflix_thread.start()

x = []
y = []
y1 = []
y2 = []

try:
    t = 0
    while True:
        if network_queue.count() > 0:
            pkt = network_queue.get()
            for i in pkt:
                print(i,end='')
            print("")
            time.sleep(1/processing_rate )
            x.append(t)
            t += 1
            y.append(network_queue.count(0))
            y1.append(network_queue.count(1))
            y2.append(network_queue.count(2))
#        if all(done) is True and network_queue.count() == 0:
        if t >= num_packets_to_send * 2 or all(done):
                break

    plt.plot(x,y,x,y1,x,y2)
    #plt.legend('game','netflix','kids')
    plt.show()

except KeyboardInterrupt:
        print("quitting")

print('*** Done')