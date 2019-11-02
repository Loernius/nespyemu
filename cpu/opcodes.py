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

    def BPL(self,cpu,data):
        print('branch on N=0')

    def BMI(self,cpu,data):
        print('branch on N=1')

    def BVC(self,cpu,data):
        print('branch on V=0')

    def BVS(self,cpu,data):
        print('branch on V=1')

    def BCC(self,cpu,data):
        print('branch on C=0')

    def BCS(self,cpu,data):
        print('branch on C=1')

    def BNE(self,cpu,data):
        print('branch on Z=0')

    def BEQ(self,cpu,data):
        print('branch on Z=1')

    def RTI(self,cpu):
        print('P,PC:=+(S)')

    def JSR(self,cpu,data):
        print('(S)-:=PC; PC:=data')

    def RTS(self,cpu):
        print('PC:=+(S)')

    def JMP(self,cpu,data):
        print('PC:=data')

    def BIT(self,cpu,data):
        print('N:=byte 7; V:=byte 6; Z:=A&data')

    def NOP(self,cpu):
        print('nothing')

    # logical and aritmetical commands
    def ORA(self, cpu, data):
        cpu.acc = cpu.acc & data

    def AND(self, cpu, data):
        cpu.acc = cpu.acc & data

    def EOR(self, cpu, data):
        cpu.acc = cpu.acc ^ data

    def ADC(self, cpu, data):
        carry = 1 if cpu.flags['C'] == True else 0
        result = (cpu.acc + data + carry) & 0xFF
        #if (result & 0x80) != (self.A & 80):
        #ref: http://nesdev.parodius.com/bbs/viewtopic.php?t=6331&sid=c635c096178295cde45bd5e7ba0d2ca5
        if (cpu.acc ^ result) & (result ^ result) & 0x80:
            cpu.flags['V'] = 1
        else:
            cpu.flags['V'] = 0
        
        if result > 0xFF:
            cpu.flags['C'] = 1
            result = 0xFF - result
        else:
            cpu.flags['C'] = 0
        
        cpu.acc = result & 0xFF

    def SBC(self, cpu, data):
        data = ~data
        carry = 1 if cpu.flags['C'] == True else 0
        result = (cpu.acc + data + carry) & 0xFF
        #if (result & 0x80) != (self.A & 80):
        #ref: http://nesdev.parodius.com/bbs/viewtopic.php?t=6331&sid=c635c096178295cde45bd5e7ba0d2ca5
        if (cpu.acc ^ result) & (result ^ result) & 0x80:
            cpu.flags['V'] = 1
        else:
            cpu.flags['V'] = 0
        
        if result > 0xFF:
            cpu.flags['C'] = 1
            result = 0xFF - result
        else:
            cpu.flags['C'] = 0
        
        cpu.acc = result & 0xFF

    def CMP(self, cpu, data):
        print('acc-data')

    def CPX(self, cpu, data):
        print('X-data')

    def CPY(self,cpu,data):
        print('Y-data')

    def DEC(self,cpu,data):
        print('data = data-1')

    def DEX(self,cpu,data):
        print('x = x-1')

    def DEY(self,cpu,data):
        print('y = y-1')

    def INC(self,cpu,data):
        print('data = data+1')

    def INX(self,cpu,data):
        print('x = x+1')

    def INY(self,cpu,data):
        print('y=y+1')

    def ASL(self,cpu,data):
        print('data = data*2')

    def ROL(self,cpu,data):
        print('data = data*2+C')

    def LSR(self,cpu,data):
        print('data = data/2')

    def ROR(self,cpu,data):
        print('data = data/2+C*128')

    # move commands
    def LDA(self,cpu,data):
        print('a:=data')

    def STA(self,cpu,data):
        print('adr:=A')

    def LDX(self,cpu,data):
        print('x:=data')

    def STX(self,cpu,data):
        print('data:=x')

    def LDY(self,cpu,data):
        print('y:=data')

    def STY(self,cpu,data):
        print('data:=y')

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

    def SLO(self,cpu,data):
        print('ASL {adr} + ORA {adr}')

    def RLA(self,cpu,data):
        print('ROL {adr} + AND {adr}')

    def SRE(self,cpu,data):
        print('LSR {adr} + EOR {adr}')

    def RRA(self,cpu,data):
        print('ROR {adr} + ADC {adr}')

    def SAX(self,cpu,data):
        print('data:=acc&X')

    def LAX(self,cpu,data):
        print('LDA {adr} + LDX {adr}')

    def DCP(self,cpu,data):
        print('DEC {adr} + CMP {adr}')

    def ISC(self,cpu,data):
        print('INC {adr} + SBC {adr}')

    def ANC(self,cpu,data):
        print('A:=A&#{imm}')

    def ALR(self,cpu,data):
        print('A:=(A&#{imm})/2')

    def ARR(self,cpu,data):
        print('')

    def XAA(self,cpu,data):
        print('')

    def AXS(self,cpu,data):
        print('')

    def AHX(self,cpu,data):
        print('')

    def SHY(self,cpu,data):
        print('')

    def SHX(self,cpu,data):
        print('')

    def TAS(self,cpu,data):
        print('')

    def LAS(self,cpu,data):
        print('')
