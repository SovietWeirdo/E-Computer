# A and B registers are accessible by program
# C register is only the output of the ALU and cannot be changed by code
# X Y and Z registers are accessible by program
# PC is indirectly accesible by program (JMP, CALL, RET)
# SP is indirectly accesible by program (PUSH, POP, CALL, RET)
# Flags are [ZF, CF, NF]
GLOBALS = {
  "A REGISTER": 0,
  "B REGISTER": 0,
  "C REGISTER": 0,
  "X REGISTER": 0,
  "Y REGISTER": 0,
  "Z REGISTER": 0,
  "PC REGISTER": 0,
  "SP REGISTER": 0,
  "Flags REGISTER": [False, False, False],
  "ROM_FILE": []
}

CHARACTER_MAP = {
  "0x10": "\n",
  "0x21": "!",
  "0x22": '"',
  "0x23": "#",
  "0x24": "$",
  "0x25": "%",
  "0x26": "&",
  "0x27": "'",
  "0x28": "(",
  "0x29": ")",
  "0x2a": "*",
  "0x2b": "+",
  "0x2c": ",",
  "0x2d": "-",
  "0x2e": ".",
  "0x2f": "/",
  "0x30": "0",
  "0x31": "1",
  "0x32": "2",
  "0x33": "3",
  "0x34": "4",
  "0x35": "5",
  "0x36": "6",
  "0x37": "7",
  "0x38": "8",
  "0x39": "9",
  "0x3a": ":",
  "0x3b": ";",
  "0x3c": "<",
  "0x3d": "=",
  "0x3e": ">",
  "0x3f": "?",
  "0x40": "@",
  "0x41": "A",
  "0x42": "B",
  "0x43": "C",
  "0x44": "D",
  "0x45": "E",
  "0x46": "F",
  "0x47": "G",
  "0x48": "H",
  "0x49": "I",
  "0x4a": "J",
  "0x4b": "K",
  "0x4c": "L",
  "0x4d": "M",
  "0x4e": "N",
  "0x4f": "O",
  "0x50": "P",
  "0x51": "Q",
  "0x52": "R",
  "0x53": "S",
  "0x54": "T",
  "0x55": "U",
  "0x56": "V",
  "0x57": "W",
  "0x58": "X",
  "0x59": "Y",
  "0x5a": "Z",
  "0x5b": "[",
  "0x5c": "\\",
  "0x5d": "]",
  "0x5e": "^",
  "0x5f": "_",
  "0x60": "`",
  "0x61": "a",
  "0x62": "b",
  "0x63": "c",
  "0x64": "d",
  "0x65": "e",
  "0x66": "f",
  "0x67": "g",
  "0x68": "h",
  "0x69": "i",
  "0x6a": "j",
  "0x6b": "k",
  "0x6c": "l",
  "0x6d": "m",
  "0x6e": "n",
  "0x6f": "o",
  "0x70": "p",
  "0x71": "q",
  "0x72": "r",
  "0x73": "s",
  "0x74": "t",
  "0x75": "u",
  "0x76": "v",
  "0x77": "w",
  "0x78": "x",
  "0x79": "y",
  "0x7a": "z",
  "0x7b": "{",
  "0x7c": "|",
  "0x7d": "}",
  "0x7e": "~",
}

class INSTRUCTION_DECODER:
  def __init__(self):
    self.instruction_set = {
      "0x000": "NOP",
      "0x001": "HLT",
      "0x101": "ADD-L-L",
      "0x102": "SUB-L-L",
      "0x103": "ADD-A-B",
      "0x104": "SUB-A-B",
      "0x201": "REG-A-LD-L",
      "0x202": "REG-B-LD-L",
      "0x203": "REG-X-LD-L",
      "0x204": "REG-Y-LD-L",
      "0x205": "REG-Z-LD-L",
      "0x800": "PRNT-L",
      "0x801": "PRNT-A",
      "0x802": "PRNT-B",
      "0x803": "PRNT-C",
      "0x804": "PRNT-X",
      "0x805": "PRNT-Y",
      "0x806": "PRNT-Z",
    }
    self.BASIC_instructions = [
      "NOP", "HLT"
    ]
    self.ALU_instructions = [
      "ADD-L-L","SUB-L-L","ADD-A-B","SUB-A-B"
    ]
    self.ALU_L_L_instructions = [
      "ADD-L-L","SUB-L-L",
    ]
    self.REG_instructions = [
      "REG-A-LD-L",
      "REG-B-LD-L",
      "REG-X-LD-L",
      "REG-Y-LD-L",
      "REG-Z-LD-L",
      "ADD-A-B",
      "SUB-A-B",
    ]
    self.REG_SET_instructions = [
      "REG-A-LD-L",
      "REG-B-LD-L",
      "REG-X-LD-L",
      "REG-Y-LD-L",
      "REG-Z-LD-L",
    ]
    self.REG_L_instructions = [
      "REG-A-LD-L",
      "REG-B-LD-L",
      "REG-X-LD-L",
      "REG-Y-LD-L",
      "REG-Z-LD-L",
    ]
    self.IO_instructions = [
      "PRNT-L",
      "PRNT-A",
      "PRNT-B",
      "PRNT-C",
      "PRNT-X",
      "PRNT-Y",
      "PRNT-Z",
    ]
  def decode(self, instruction):
    try:
      return self.instruction_set[instruction]
    except KeyError:
      return "NOP"

class INSTRUCTION_EXECUTOR:
  def __init__(self):
    pass
  def L_L_get_operands(self):
    ROM = GLOBALS["ROM_FILE"]
    BF = CPU_BASIC_FUNCTIONS()
    BF.increment_pc()
    OPERAND_1 = int(ROM[GLOBALS["PC Register"]], 16)
    BF.increment_pc()
    OPERAND_2 = int(ROM[GLOBALS["PC Register"]], 16)
    return (OPERAND_1, OPERAND_2)
  def L_get_operands(self):
    ROM = GLOBALS["ROM_FILE"]
    BF = CPU_BASIC_FUNCTIONS()
    BF.increment_pc()
    OPERAND_1 = int(ROM[GLOBALS["PC Register"]], 16)
    return OPERAND_1
  def execute(self, instruction):
    ID = INSTRUCTION_DECODER()
    INSTRUCTION = ID.decode(instruction)
    ROM = GLOBALS["ROM_FILE"]
    BF = CPU_BASIC_FUNCTIONS()
    if INSTRUCTION in ID.BASIC_instructions:
      if INSTRUCTION == "HLT":
        while True:
          exit("CPU HALTED")
    if INSTRUCTION in ID.ALU_instructions:
      alu = ALU()
      if INSTRUCTION in ID.REG_instructions:
        RC = REG_CONTROL()
        RC.UPDATE_LOCAL_REGISTERS()
        if INSTRUCTION == "ADD-A-B":
          A, B = RC.RETRIEVE_REGISTER("A"), RC.RETRIEVE_REGISTER("B")
          alu.add(A, B)
        elif INSTRUCTION == "SUB-A-B":
          A, B = RC.RETRIEVE_REGISTER("A"), RC.RETRIEVE_REGISTER("B")
          alu.subtract(A, B)
        print(GLOBALS["C REGISTER"])
      if INSTRUCTION in ID.ALU_L_L_instructions:
        if INSTRUCTION == "ADD-L-L":
          Operands = self.L_L_get_operands()
          alu.add(Operands[0], Operands[1])
          print(GLOBALS["C REGISTER"], GLOBALS["Flags REGISTER"])
        elif INSTRUCTION == "SUB-L-L":
          Operands = self.L_L_get_operands()
          alu.subtract(Operands[0], Operands[1])
          print(GLOBALS["C REGISTER"], GLOBALS["Flags REGISTER"])
    if INSTRUCTION in ID.REG_instructions:
      RC = REG_CONTROL()
      RC.UPDATE_LOCAL_REGISTERS()
      if INSTRUCTION in ID.REG_SET_instructions:
        if INSTRUCTION in ID.REG_L_instructions:
          INSTRUCTION_TO_REGISTER = {
            "REG-A-LD-L": "A",
            "REG-B-LD-L": "B",
            "REG-X-LD-L": "X",
            "REG-Y-LD-L": "Y",
            "REG-Z-LD-L": "Z",
          }
          RC.SET_REGISTER(INSTRUCTION_TO_REGISTER[INSTRUCTION], self.L_get_operands())
      print(GLOBALS["A REGISTER"],GLOBALS["B REGISTER"],GLOBALS["X REGISTER"],GLOBALS["Y REGISTER"],GLOBALS["Z REGISTER"])
    if INSTRUCTION in ID.IO_instructions:
      if INSTRUCTION == "PRNT-L":
        print(BF.hex_thru_char_map(self.L_get_operands()), end="")
      elif INSTRUCTION == "PRNT-A":
        print(BF.hex_thru_char_map(hex(GLOBALS["A REGISTER"])), end="")
      elif INSTRUCTION == "PRNT-B":
        print(BF.hex_thru_char_map(hex(GLOBALS["B REGISTER"])), end="")
      elif INSTRUCTION == "PRNT-C":
        print(BF.hex_thru_char_map(hex(GLOBALS["C REGISTER"])), end="")
      elif INSTRUCTION == "PRNT-X":
        print(BF.hex_thru_char_map(hex(GLOBALS["X REGISTER"])), end="")
      elif INSTRUCTION == "PRNT-Y":
        print(BF.hex_thru_char_map(hex(GLOBALS["Y REGISTER"])), end="")
      elif INSTRUCTION == "PRNT-Z":
        print(BF.hex_thru_char_map(hex(GLOBALS["Z REGISTER"])), end="")
    BF.increment_pc()
    return 0
  def execute_pc_instruction(self):
    self.execute(GLOBALS["ROM_FILE"][GLOBALS["PC Register"]])

class REG_CONTROL:
  def __init__(self):
    self.A_REGISTER = 0
    self.B_REGISTER = 0
    self.X_REGISTER = 0
    self.Y_REGISTER = 0
    self.Z_REGISTER = 0
  def UPDATE_GLOBAL_REGISTERS(self):
    try:
      GLOBALS["A REGISTER"] = hex(self.A_REGISTER)
    except TypeError:
      pass
    try:
      GLOBALS["B REGISTER"] = hex(self.B_REGISTER)
    except TypeError:
      pass
    try:
      GLOBALS["X REGISTER"] = hex(self.X_REGISTER)
    except TypeError:
      pass
    try:
      GLOBALS["Y REGISTER"] = hex(self.Y_REGISTER)
    except TypeError:
      pass
    try:
      GLOBALS["Z REGISTER"] = hex(self.Z_REGISTER)
    except TypeError:
      pass
  def UPDATE_LOCAL_REGISTERS(self):
    self.A_REGISTER = GLOBALS["A REGISTER"]
    self.B_REGISTER = GLOBALS["B REGISTER"]
    self.X_REGISTER = GLOBALS["X REGISTER"]
    self.Y_REGISTER = GLOBALS["Y REGISTER"]
    self.Z_REGISTER = GLOBALS["Z REGISTER"]
  def SET_REGISTER(self, REGISTER:str, VALUE:int):
    if REGISTER == "A":
      self.A_REGISTER = VALUE
    elif REGISTER == "B":
      self.B_REGISTER = VALUE
    elif REGISTER == "X":
      self.X_REGISTER = VALUE
    elif REGISTER == "Y":
      self.Y_REGISTER = VALUE
    elif REGISTER == "Z":
      self.Z_REGISTER = VALUE
    else:
      print(f"ERROR: {REGISTER} REGISTER NOT FOUND")
    self.UPDATE_GLOBAL_REGISTERS()
  def RETRIEVE_REGISTER(self, REGISTER:str):
    if REGISTER == "A":
      return int(self.A_REGISTER, 16)
    elif REGISTER == "B":
      return int(self.B_REGISTER, 16)
    elif REGISTER == "X":
      return int(self.X_REGISTER, 16)
    elif REGISTER == "Y":
      return int(self.Y_REGISTER, 16)
    elif REGISTER == "Z":
      return int(self.Z_REGISTER, 16)
    else:
      print(f"ERROR: {REGISTER} REGISTER NOT FOUND")
  
class ALU:
  # Flags: ZF(Zero), CF(Carry), NF(Negative)
  def __init__(self):
    self.ZF = False
    self.CF = False
    self.NF = False
  def refresh_flags(self):
    GLOBALS["Flags REGISTER"][0] = self.ZF
    GLOBALS["Flags REGISTER"][1] = self.CF
    GLOBALS["Flags REGISTER"][2] = self.NF
  def falsify_flags(self):
    self.ZF = False
    self.CF = False
    self.NF = False
  def add(self, a:int, b:int):
    self.falsify_flags()
    GLOBALS["C REGISTER"] = hex(int(a)+int(b))
    C_REG = GLOBALS["C REGISTER"]
    if int(C_REG, 16) > 65535:
      GLOBALS["C REGISTER"] = hex(int(C_REG, 16) - 65536)
      self.CF = True
    else:
      self.CF = False
    if int(C_REG, 16) == 0:
      self.ZF = True
    else:
      self.ZF = False
    self.refresh_flags()
  def subtract(self, a:int, b:int):
    self.falsify_flags()
    GLOBALS["C REGISTER"] = hex(int(a)-int(b))
    C_REG = GLOBALS["C REGISTER"]
    if int(C_REG, 16) < 0:
      GLOBALS["C REGISTER"] = hex(abs(int(C_REG, 16)))
      self.NF = True
    else:
      self.NF = False
    if int(C_REG, 16) == 0:
      self.ZF = True
    else:
      self.ZF = False
    self.refresh_flags()


class CPU_BOOT:
  def __init__(self, ROM_FILE):
    with open(ROM_FILE, "r") as f:
      self.ROM = f.readlines()
    l_index = 0
    for line in self.ROM:
      self.ROM[l_index] = line.replace("\n", "")
      l_index += 1
    self.SET_PC()
    GLOBALS["ROM_FILE"] = self.ROM
  def SET_PC(self):
    GLOBALS["PC Register"] = int(self.ROM[511], 16)

class CPU_BASIC_FUNCTIONS:
  def increment_pc(self, inc_amount:int=1):
    GLOBALS["PC Register"] += inc_amount
  def set_pc(self, address):
    GLOBALS["PC Register"] = address
  def hex_thru_char_map(self, char):
    return CHARACTER_MAP[hex(char)]
