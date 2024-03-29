import numpy as np

from cpu import opcodes
from cpu import addr_modes

class cpu:
	
	# construtor
	def __init__(self):

		# registers
		self.acc = 0x00
		self.x = 0x00
		self.y = 0x00
		self.pc = 0x0000
		self.stack_pointer = 0x00

		self.ram = [0] * 0xFFFF
		self.addr_abs = 0x00
		self.addr_rel = 0x00
		
			
		# status flags
		self.flags = {
			"C": False,
			"Z": False,
			"I": False,
			"D": False,
			"B": False,
			"V": False,
			"N": False
		}
		self.opcode = opcodes.opcodes()

	# addressing modes
	

	def check_op(self, i):
		if i == 0x00:
			print('caiu no break')
		elif i == 0x78:
			self.opcode.SEI(self)
		else:
			print('unexpected opcode')
	
	def read(self, addr):
		if addr < 0x0000 or addr > 0xFFFF:
			print('addr out of bounds')
		else:
			return self.ram[addr]

	def write(self, addr, data):
		if addr < 0x0000 or addr > 0xFFFF:
			print('addr out of bounds')
		else:
			self.ram[addr] = data

	