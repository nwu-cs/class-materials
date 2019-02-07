
import numpy as np
import matplotlib.pyplot as plt
import time

# return the number of uniformly random birthdates it takes to have a duplicate
def birthdays_simu():
    n = 2
    
    
    return n
        
# generate n uniformly random birthdates, return True if there are any duplicates, False otherwise
def test_birthday(n):
    # generate n random birthdates
    if "there is a pair within the n birthdates":
        return True
    else:
        return False

if __name__ == '__main__':
    trials = 100
    nPeople = []
    
    # how many random people 
    start = time.time()
    for i in range(trials):
        nPeople.append(birthdays_simu())
    simulation_endtime = time.time()

    # how often 23 people have the same birthday (what are the expected results?)
    bdmatches = np.empty(0)
    start = time.time()
    for i in range(trials):
        bdmatches = np.append(bdmatches,test_birthday(23))
    endtime_23people = time.time()

    # make a numpy array from the results
    npPeople = np.array(nPeople)
        
    # make a list for the x axis, and another for the y axis
    
    plt.plot(x,y)   # plot the data
    plt.grid()      # turn the grid on
    plt.show()      # update the plot
         
