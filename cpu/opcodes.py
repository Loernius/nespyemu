import numpy as np


class opcodes:
    # Jump/Flag instructions
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

    def BRK(self, cpu):
        print('ação de break')

    def BPL(self,cpu,addr):
        print('branch on N=0')

    def BMI(self,cpu,addr):
        print('branch on N=1')

    def BVC(self,cpu,addr):
        print('branch on V=0')

    def BVS(self,cpu,addr):
        print('branch on V=1')

    def BCC(self,cpu,addr):
        print('branch on C=0')

    def BCS(self,cpu,addr):
        print('branch on C=1')

    def BNE(self,cpu,addr):
        print('branch on Z=0')

    def BEQ(self,cpu,addr):
        print('branch on Z=1')

    def RTI(self,cpu):
        print('P,PC:=+(S)')

    def JSR(self,cpu,addr):
        print('(S)-:=PC; PC:=addr')

    def RTS(self,cpu):
        print('PC:=+(S)')

    def JMP(self,cpu,addr):
        print('PC:=addr')

    def BIT(self,cpu,addr):
        print('N:=byte 7; V:=byte 6; Z:=A&addr')

    def NOP(self,cpu):
        print('nothing')

    # logical and aritmetical commands
    def ORA(self, cpu, addr):
        cpu.acc = cpu.acc & addr

    def AND(self, cpu, addr):
        cpu.acc = cpu.acc & addr

    def EOR(self, cpu, addr):
        cpu.acc = cpu.acc ^ addr

    def ADC(self, cpu, addr):
        print('acc = acc + addr')

    def SBC(self, cpu, addr):
        print('acc = acc - addr')

    def CMP(self, cpu, addr):
        print('acc-addr')

    def CPX(self, cpu, addr):
        print('X-addr')

    def CPY(self,cpu,addr):
        print('Y-addr')

    def DEC(self,cpu,addr):
        print('addr = addr-1')

    def DEX(self,cpu,addr):
        print('x = x-1')

    def DEY(self,cpu,addr):
        print('y = y-1')

    def INC(self,cpu,addr):
        print('addr = addr+1')

    def INX(self,cpu,addr):
        print('x = x+1')

    def INY(self,cpu,addr):
        print('y=y+1')

    def ASL(self,cpu,addr):
        print('addr = addr*2')

    def ROL(self,cpu,addr):
        print('addr = addr*2+C')

    def LSR(self,cpu,addr):
        print('addr = addr/2')

    def ROR(self,cpu,addr):
        print('addr = addr/2+C*128')

    # move commands
    def LDA(self,cpu,addr):
        print('a:=addr')

    def STA(self,cpu,addr):
        print('adr:=A')

    def LDX(self,cpu,addr):
        print('x:=addr')

    def STX(self,cpu,addr):
        print('addr:=x')

    def LDY(self,cpu,addr):
        print('y:=addr')

    def STY(self,cpu,addr):
        print('addr:=y')

    def TAX(self,cpu):
        print('x:=acc')

    def TXA(self,cpu):
        print('acc:=x')

    def TAY(self,cpu):
        print('y:=acc')

    def TYA(self,cpu):
        print('acc:=y')

    def TSX(self,cpu):
        print('x:=s')

    def TXS(self,cpu):
        print('s:=x')

    def PLA(self,cpu):
        print('acc:=+(S)')

    def PHA(self,cpu):
        print('(S)-:=A')

    def PLP(self,cpu):
        print('P:=+(s)')

    def PHP(self,cpu):
        print('(S)-:=P')

    # illegal opcodes

    def SLO(self,cpu,addr):
        print('ASL {adr} + ORA {adr}')

    def RLA(self,cpu,addr):
        print('ROL {adr} + AND {adr}')

    def SRE(self,cpu,addr):
        print('LSR {adr} + EOR {adr}')

    def RRA(self,cpu,addr):
        print('ROR {adr} + ADC {adr}')

    def SAX(self,cpu,addr):
        print('addr:=acc&X')

    def LAX(self,cpu,addr):
        print('LDA {adr} + LDX {adr}')

    def DCP(self,cpu,addr):
        print('DEC {adr} + CMP {adr}')

    def ISC(self,cpu,addr):
        print('INC {adr} + SBC {adr}')

    def ANC(self,cpu,addr):
        print('A:=A&#{imm}')

    def ALR(self,cpu,addr):
        print('A:=(A&#{imm})/2')

    def ARR(self,cpu,addr):
        print('')

    def XAA(self,cpu,addr):
        print('')

    def LAX(self,cpu,addr):
        print('')

    def AXS(self,cpu,addr):
        print('')

    def SBC(self,cpu,addr):
        print('')

    def AHX(self,cpu,addr):
        print('')

    def SHY(self,cpu,addr):
        print('')

    def SHX(self,cpu,addr):
        print('')

    def TAS(self,cpu,addr):
        print('')

    def LAS(self,cpu,addr):
        print('')

    def add_binary(self, num1, num2):

        if num1 > 0xFF | num2 > 0xFF:
            print('sistema não permite operações com digitos maiores que 255')
            return False

        bin1 = bin(num1)[2:]
        bin2 = bin(num2)[2:]

        maxlength = max(len(bin1), len(bin2))

        if len(bin1)== maxlength:
            bin2.zfill(maxlength)
        else:
            bin1.zfill(maxlength)

        print(bin1)
        print(bin2)

