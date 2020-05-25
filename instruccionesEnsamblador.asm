# Instrucciones tipo I
main:
BEQ $0, $8, 10
NOP $0, $0, $0
SLTI $0, $9, 10
ANDI $1, $10, 10
ORI $2, $11, 10
SW $0, 0(8)
LW $0, 0(12)
J main
J 24
JAL main



