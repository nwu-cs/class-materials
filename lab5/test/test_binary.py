import unittest
import sys

# so this can import the decoder
sys.path.append("../Py106")

from captured_output import captured_output
import Packet
import DecodeTMATS as decoder


class TestDecodeTMATS(unittest.TestCase):

	def setUp(self):
#		print("doing setup")
		self.PktIO       = Packet.IO()
		self.decoder = decoder.DecodeTMATS(self.PktIO)

	def test_decode_summary(self):
#		print("doing test")
		with captured_output() as (out, err):
			self.decoder.print_summary('../data/8S-IRIG11.ch10')

		output = out.getvalue().split('\n')
#		print(output)
		self.assertEqual("TMATS record 0",output[0])
		self.assertEqual("NumberOfTmatsLines : 199",output[1])
		self.assertEqual("AvailableTmatsLines : 200",output[2])
		self.assertEqual("File Name     : ../data/8S-IRIG11.ch10",output[3])
		self.assertEqual("Program Name  : UIC-6.007(1.594)",output[4])
		self.assertEqual("IRIG Version  : 9",output[5])
		self.assertEqual("TMATS Version : 11",output[6])
		self.assertEqual("Data Type Counts",output[7])
		self.assertEqual("Data Type User Defined             : 1",output[8])
		self.assertEqual("Data Type TMATS                    : 1",output[9])
		self.assertEqual("Data Type Index                    : 16",output[10])
		self.assertEqual("Data Type UART                     : 59",output[11])
		self.assertEqual("Data Type Time                     : 59",output[12])

# 2nd test file
		with captured_output() as (out, err):
			self.decoder.print_summary('../data/Wyle_24042009_15425242.ch10')

		output = out.getvalue().split('\n')
#		print(output)
		self.assertEqual("TMATS record 0",output[0])
		self.assertEqual("NumberOfTmatsLines : 876",output[1])
		self.assertEqual("AvailableTmatsLines : 900",output[2])
		self.assertEqual("File Name     : ../data/Wyle_24042009_15425242.ch10",output[3])
		self.assertEqual("Program Name  : Wyle TDS IMUX G2",output[4])
		self.assertEqual("IRIG Version  : 0",output[5])
		self.assertEqual("TMATS Version : 7",output[6])
		self.assertEqual("Data Type Counts",output[7])
		self.assertEqual("Data Type Video Format 0           : 176",output[8])
		self.assertEqual("Data Type TMATS                    : 1",output[9])
		self.assertEqual("Data Type Time                     : 525",output[10])
		self.assertEqual("Data Type 1553                     : 52",output[11])
		self.assertEqual("Data Type Analog                   : 684",output[12])
		self.assertEqual("Data Type Ethernet                 : 173",output[13])
		self.assertEqual("Data Type PCM Format 1             : 2296",output[14])


# 3rd test file
		with captured_output() as (out, err):
			self.decoder.print_summary('../data/Sypris-M800_04022009_030016.ch10')

		output = out.getvalue().split('\n')

		self.assertEqual("TMATS record 0",output[0])
		self.assertEqual("NumberOfTmatsLines : 661",output[1])
		self.assertEqual("AvailableTmatsLines : 700",output[2])
		self.assertEqual("File Name     : ../data/Sypris-M800_04022009_030016.ch10",output[3])
		self.assertEqual("Program Name  : M800",output[4])
		self.assertEqual("IRIG Version  : 0",output[5])
		self.assertEqual("TMATS Version : 07",output[6])
		self.assertEqual("Data Type Counts",output[7])
		self.assertEqual("Data Type TMATS                    : 1",output[8])
		self.assertEqual("Data Type PCM Format 1             : 6976",output[9])
		self.assertEqual("Data Type Analog                   : 872",output[10])
		self.assertEqual("Data Type Time                     : 80",output[11])

if __name__ == '__main__':
	unittest.main()