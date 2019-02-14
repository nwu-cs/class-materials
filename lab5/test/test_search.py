from binary import binarySearch
from binary import interpolationSearch


if __name__ == "__main__":
    print(__name__)
    t1 = [1, 9, 27, 28, 36, 42, 80, 83, 94, 97]

    for i in range(len(t1)):
        x = t1[i]
        test = i
        print(binarySearch(t1,0,len(t1)-1, x))
