from registerFile import registerfiles
from registerTable import register_table
from binary_parsing import machineCode_parser
import sys

try:
    print('Pprogram running...')

    file_in = open('binary.bin')
    instructions = []
    for line in file_in:
        line = line.strip()
        instructions.append(line)
    parse_instructions = machineCode_parser(registerfiles,register_table)
    parse_instructions.parse(instructions)

    print('Program finished!')
    sys.exit(0)

except Exception as e:
    print(f'Program failed: {e}')
    sys.exit(1)