#!/bin/bash
rm -rf obj_dir/
mkdir obj_dir
cp MIPS.cpp obj_dir/MIPS.cpp
verilator -Wall -cc --exe MIPS.cpp -f fileList.txt --top-module MIPS
cd obj_dir/
make -f VMIPS.mk