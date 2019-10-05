import numpy as np

from . import opcodes as opcode_class
from . import addr_modes as addr_modes_class

class CPU:
	# inicialização de utils
	opcode = opcode_class.opcodes()
	address_mode = addr_modes_class.addr_modes()

	# construtor
	def __init__(self):

		# registers
		self.acc = np.uint8()
		self.x = np.uint8()
		self.y = np.uint8()
		self.pc = np.uint16()

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


	