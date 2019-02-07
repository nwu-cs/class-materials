# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 14:16:34 2019

@author: c_mob
"""

import random
import time
import numpy as np

# Returns index of x in arr if present, else -1 
def binarySearch (arr, l, r, x): 
  
    # Check base case 
    if r >= l: 
  
        mid = int(l + (r - l)/2)
  
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
  
  

if __name__ == '__main__':  
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
    
    print("time %f"%(builtin_exectime[0]))
    print("time for last_item -- builtin:%.1fns ---- binary:%.1fns -- ratio:%.1f"%(builtin_exectime[0],binary_exectime[0],builtin_exectime[0]/binary_exectime[0]))
    print("time for middle_item -- builtin:%.1fns ---- binary:%.1fns -- ratio:%.1f"%(builtin_exectime[1],binary_exectime[1],builtin_exectime[1]/binary_exectime[1]))
    print("time for missing_item -- builtin:%.1fns ---- binary:%.1fns -- ratio:%.1f"%(builtin_exectime[2],binary_exectime[2],builtin_exectime[2]/binary_exectime[2]))
