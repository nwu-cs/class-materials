# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 14:16:34 2019

@author: c_mob
"""

import random
import time
import numpy as np
import matplotlib.pyplot as plt

# Returns index of x in arr if present, else -1 
def binarySearch (arr, l, r, x): 
  
    # Check base case 
    if r >= l: 
  
        mid = (l + (r - l)//2)
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
          
        # If element is smaller than mid, then it  
        # can only be present in left subarray 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
  
        # Else the element can only be present  
        # in right subarray 
        else: 
            return binarySearch(arr, mid + 1, r, x) 
  
    else: 
        # Element is not present in the array 
        return -1


def interpolationSearch(arr, x):
    # Find indexs of two corners
    lo = 0              # first index
    hi = len(arr)-1     # last index

    # Since array is sorted, an element present
    # in array must be in range defined by corner
    while lo <= hi and x >= arr[lo] and x <= arr[hi]:
        # Probing the position with keeping
        # uniform distribution in mind.
        pos = lo + int(((float(hi - lo) / (arr[hi] - arr[lo])) * (x - arr[lo])))

        # Condition of target found
        if arr[pos] == x:
            return pos

            # If x is larger, x is in upper part
        if arr[pos] < x:
            lo = pos + 1;

            # If x is smaller, x is in lower part
        else:
            hi = pos - 1;

    return -1

if __name__ == '__main__':  

    rs = [1, 9, 27, 27, 36, 42, 80, 83, 94, 92]
    print(binarySearch(rs, 0, len(rs)-1, rs[-1]) )
    print(interpolationSearch(rs, rs[-1]) )
  
    r = []
    for i in range(1000000):
        r.append(random.randint(0,10000))
    r.sort()

    last_item = r[-1]
    middle_item = r[len(r)//2]
    missing_item = .5       # only integers in the list!
    binary_starts = np.empty(3)
    builtin_starts = np.empty(3)
    binary_stops = np.empty(3)
    builtin_stops = np.empty(3)
    binary_exectime = np.empty(3)
    builtin_exectime = np.empty(3)
    interpolation_exectime = np.empty(3)
    
    i = 0
    binary_starts[i] = time.perf_counter_ns()
    print(binarySearch(r, 0, len(r)-1, last_item) )
    binary_stops[i] = time.perf_counter_ns()
    binary_exectime[i] = binary_stops[i] - binary_starts[i]
    i += 1
    
    binary_starts[i] = time.perf_counter_ns()
    print(binarySearch(r, 0, len(r)-1, middle_item) )
    binary_stops[i] = time.perf_counter_ns()
    binary_exectime[i] = binary_stops[i] - binary_starts[i]
    i += 1
    
    binary_starts[i] = time.perf_counter_ns()
    print(binarySearch(r, 0, len(r)-1, missing_item) )
    binary_stops[i] = time.perf_counter_ns()
    binary_exectime[i] = binary_stops[i] - binary_starts[i]
    i += 1
    #builtin searches
    i = 0
    builtin_starts[i] = time.perf_counter_ns()
    test = last_item in r
    builtin_stops[i] = time.perf_counter_ns()
    builtin_exectime[i] = builtin_stops[i] - builtin_starts[i]
    print(test)
    i += 1
    
    builtin_starts[i] = time.perf_counter_ns()
    test = middle_item in r
    builtin_stops[i] = time.perf_counter_ns()
    builtin_exectime[i] = builtin_stops[i] - builtin_starts[i]
    print(test)
    i += 1
    
    builtin_starts[i] = time.perf_counter_ns()
    test = missing_item in r
    builtin_stops[i] = time.perf_counter_ns()
    builtin_exectime[i] = builtin_stops[i] - builtin_starts[i]
    print(test)
    i += 1
    
    #interpolationSearch
    i = 0
    start = time.perf_counter_ns()
    print(interpolationSearch(r, last_item) )
    stop = time.perf_counter_ns()
    interpolation_exectime[i] = stop - start
    i += 1
    
    start = time.perf_counter_ns()
    print(interpolationSearch(r, middle_item) )
    stop = time.perf_counter_ns()
    interpolation_exectime[i] = stop - start
    i += 1
    
    start = time.perf_counter_ns()
    print(interpolationSearch(r, missing_item) )
    stop = time.perf_counter_ns()
    interpolation_exectime[i] = stop - start
    
    #print("time %f"%(builtin_exectime[0]))
#    print("time for last_item -- builtin:%.1fns ---- binary:%.1fns -- ratio:%.1f"%(builtin_exectime[0],binary_exectime[0],builtin_exectime[0]/binary_exectime[0]))
#    print("time for middle_item -- builtin:%.1fns ---- binary:%.1fns -- ratio:%.1f"%(builtin_exectime[1],binary_exectime[1],builtin_exectime[1]/binary_exectime[1]))
#    print("time for missing_item -- builtin:%.1fns ---- binary:%.1fns -- ratio:%.1f"%(builtin_exectime[2],binary_exectime[2],builtin_exectime[2]/binary_exectime[2]))
    print("time for builtin      --\tlast:%.1fns ----\tmiddle:%.1fns --\tmissing:%.1f"%(builtin_exectime[0],builtin_exectime[1],builtin_exectime[2]))
    print("time for binary       --\tlast:%.1fns ----\tmiddle:%.1fns --\tmissing:%.1f"%(binary_exectime[0],binary_exectime[1],binary_exectime[2]))
    print("time for interpolation--\tlast:%.1fns ----\tmiddle:%.1fns --\tmissing:%.1f"%(interpolation_exectime[0],interpolation_exectime[1],interpolation_exectime[2]))

    x = ["last","middle","missing"]
    y = [[builtin_exectime[0],builtin_exectime[1],builtin_exectime[2]],
         [binary_exectime[0],binary_exectime[1],binary_exectime[2]],
         [interpolation_exectime[0],interpolation_exectime[1],interpolation_exectime[2]]]
    ynp = np.array(y)
    ynp = np.transpose(ynp)    
    
    #plt.plot(x,ynp)
    #plt.show()