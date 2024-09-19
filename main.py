import cpu
import gpu
RAM = []
#for i in range(1048576):
  #RAM.append(0)

gpu.start()

CPU = cpu.CPU_BOOT("BOOT_ROM.EC")
IE = cpu.INSTRUCTION_EXECUTOR()
BF = cpu.CPU_BASIC_FUNCTIONS()

while True:
  EXECUTE = IE.execute_pc_instruction()
  #gpu.frame()
