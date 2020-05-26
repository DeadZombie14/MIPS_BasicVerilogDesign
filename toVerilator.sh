#!/bin/bash
rm -r obj_dir/
mkdir obj_dir
cp MIPS.cpp obj_dir/MIPS.cpp
cp registerBankMemory.mem obj_dir/registerBankMemory.mem
cp dataMemory.mem obj_dir/dataMemory.mem
cp instructionMemory.mem obj_dir/instructionMemory.mem
verilator -Wall -cc --exe MIPS.cpp -f fileList.txt --top-module MIPS_TB --trace
cd obj_dir/
make -f VMIPS_TB.mk