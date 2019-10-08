import numpy as np

from cpu import opcodes
from cpu import addr_modes

class cpu:
	# inicialização de utils
	opcode = opcodes.opcodes()
	address_mode = addr_modes.addr_modes()

	# construtor
	def __init__(self):

		# registers
		self.acc = np.uint8()
		self.x = np.uint8()
		self.y = np.uint8()
		self.pc = np.uint16(value=0x0000)

		# status flags
		self.p = {
			"C": False,
			"Z": False,
			"I": False,
			"D": False,
			"B": False,
			"V": False,
			"N": False
		}
		

	# addressing modes
	

	def check_op(self, i):
		if i == 0x00:
			self.address_mode.IMM(self)
		elif i == 0x78:
			self.address_mode.IMP(self)
		else:
			print('unexpected opcode')


	