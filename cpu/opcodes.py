import numpy as np

class opcodes:
	# Flag instructions
	def SEI(self, cpu):
		cpu.flags['I'] = True
	def CLI(self, cpu):
		cpu.flags['I'] = False
	def CLC(self, cpu):
		cpu.flags['C'] = False
	def SEC(self, cpu):
		cpu.flags['C'] = True
	def CLV(self, cpu):
		cpu.flags['V'] = False
	def CLD(self, cpu):
		cpu.flags['D'] = False
	def SED(self, cpu):
		cpu.flags['D'] = True
	
	


	