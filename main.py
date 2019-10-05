import cpu.cpu as cpu_class

def main():
	cpu = cpu_class.CPU()

	instruction = 0x00
	cpu.check_op(instruction)

if __name__ == '__main__':
	main()