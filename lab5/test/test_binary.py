import unittest
import sys

sys.path.append("..")

#from captured_output import captured_output
from binary import binarySearch
from binary import interpolationSearch


class TestSearchs(unittest.TestCase):

	def test_binary(self):
        
		t1 = [1, 9, 27, 28, 36, 42, 80, 83, 94, 97]

		for i in range(len(t1)):
			x = t1[i]
			test = i
			self.assertEqual(binarySearch(t1,x),test)
		self.assertEqual(binarySearch(t1,t1[len(t1)//2]+.5),-1)
		self.assertEqual(binarySearch(t1,-50),-1)


	def test_interpolation(self):
		t1 = [1, 9, 27, 28, 36, 42, 80, 83, 94, 97]

		for i in range(len(t1)):
			x = t1[i]
			test = i
			self.assertEqual(interpolationSearch(t1, 0, len(t1)-1, x), test)
		self.assertEqual(interpolationSearch(t1, 0, len(t1)-1, t1[len(t1) // 2] + .5), -1)
		self.assertEqual(interpolationSearch(t1, 0, len(t1)-1, -50), -1)




if __name__ == '__main__':
	unittest.main()