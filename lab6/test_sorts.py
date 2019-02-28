import unittest
import numpy as np

#import your sort function

class TestSorts(unittest.TestCase):

	def readList(self, filename):
		fh = open(filename, 'r')
		lines = fh.readlines()
		fh.close()

		r = []
		for x in lines:
			r.append(int(x))

		return r

	def test_binary(self):
		testlist = self.readList('testlist.txt')
		# if you want to work with a more managable list that you can inspect more easily in the debugger, comment out the above line and make your own shorter list
		# such as: testlist = np.random.randint(0,10000,100)
		#testlist = np.random.randint(0, 10000, 100)

		# replace mySort with your sorting function
		list_to_test = mySort(testlist)
		sortedList = testlist.copy()
		sortedList.sort()

		i = 0
		for x in list_to_test:
			self.assertEqual(x,sortedList[i] )
			i += 1


if __name__ == '__main__':
	unittest.main()