# RISC-V Instruction Set Simulator

## 1️⃣ Overview:
The RISC-V Instruction Set Simulator is an educational tool (developed based on my [simple-riscv-compiler](https://github.com/anhtngc/simple-riscv-compiler)) designed to decode and simulate the execution of RISC-V assembly instructions. By analyzing binary machine code, this project mimics the behavior of a RISC-V processor, updating register values and memory states as instructions execute. This simulator serves as a practical resource for students and developers to deepen their understanding of RISC-V architecture and instruction flow.

## 2️⃣ Key Features:
- **Binary Input Parsing**: Read machine code directly from a binary.bin file for instruction simulation.
- **Instruction Decoding**: Support decoding of all major RISC-V instruction types: R-type, I-type, S-type, B-type, U-type, and J-type.
- **Label Offset Calculation**: Correctly compute forward label offsets for branch (beq, bne) and jump (jal) instructions.
- **Register and Memory Simulation**: Simulate RISC-V registers (x0 - x31) and read/write/store data memory (analyze `lw` and `sw` instructions), updating states after each instruction execution.
- **Error Handling**: Provide clear error messages for invalid instructions, memory accesses, or unsupported operations.
- **Result**: Generating the final state of registers (Register File) and data memory (Data Memory) to two separate output files for easy analysis.

## 3️⃣ Getting Started:
Before using the my Simple RISC-V Compiler, ensure you have the following installed: `python 3.x`
### Installation
Clone the repository:
```bash
    git clone https://github.com/anhtngc/risc-v_instruction-set-simulator.git
    cd simple-riscv-compiler
```
### Usage
#### 1. Edit your RISC-V Assembly codes:
Modify the content of the code.asm file with your RISC-V Assembly instructions.
#### 2. Prepare the input file:
Add your binary machine code to the `binary.bin` file or run the following command to compile your assembly code:
```bash
    python3 assembler.py
```
#### 3. Run the simulator:
Execute the following command to start the simulation:
```bash
    python3 processor.py
```
#### 3. Result:
- The final state of registers will be saved in `registerFiles.txt`.
- The state of data memory will be saved in `dataMemory.txt`.

Note that the commands nop, ret, la ect are being ignored and cannot be converted into binary machine code.

Contributions are welcome! If you encounter bugs or have suggestions for new features, feel free to open an issue or submit a pull request.
