import cpu.cpu as cpu_class
def main():
	cpu = cpu_class.cpu()
	raw_rom = open('mario.nes', 'rb')

	header = raw_rom.read1(4)
	
	if header != b'NES\x1a':
		print('CHECKSUM FAILED')
	else:
		raw_rom.seek(0x10, 0)
		instruction = int.from_bytes(raw_rom.read(1), 'little')
		print(instruction)
		cpu.check_op(instruction)

if __name__ == '__main__':
	main()