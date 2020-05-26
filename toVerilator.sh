#!/bin/bash
rm -r obj_dir/
mkdir obj_dir
cp MIPS.cpp obj_dir/MIPS.cpp
verilator -Wall -cc --exe MIPS.cpp -f fileList.txt --top-module MIPS_TB
cd obj_dir/
make -f VMIPS_TB.mk