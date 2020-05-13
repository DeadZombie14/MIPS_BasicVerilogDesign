# Mendoza Morelos Martin Mathier
# Programa para auto-generar código máquina a partir de instrucciones en ensamblador para MIPS
# 1 instruccion por línea
# Comentarios usando # al inicio de la linea

# Espaciado entre elementos
espaciado = ""
# Dividir cada linea en N caracteres
corteLinea = 8 #37 #8
# Cantidad de lineas minimas
lineasMinimas = 128 #32 #128

# Diccionario de instrucciones MIPS
assemblyInstructions = {
    'NOP':  { 'OP':'000000', 'instCode':'000000'},
    'ADD':  { 'OP':'000000', 'instCode':'100000'},
    'SUB':  { 'OP':'000000', 'instCode':'100010'},
    'MUL':  { 'OP':'011100', 'instCode':'000010'},
    'DIV':  { 'OP':'000000', 'instCode':'011010'},
    'AND':  { 'OP':'000000', 'instCode':'100100'},
    'OR':   { 'OP':'000000', 'instCode':'100101'},
    'NOR':  { 'OP':'000000', 'instCode':'100111'},
    'XOR':  { 'OP':'000000', 'instCode':'100110'},
    'SLT':  { 'OP':'000000', 'instCode':'101010'},
    'SLL':  { 'OP':'000000', 'instCode':'000000'},
    'SRL':  { 'OP':'000000', 'instCode':'000010'},
    'LW':   { 'OP':'100011', 'instCode':'000000'},
    'SW':   { 'OP':'100011', 'instCode':'000000'},
    'J':    { 'OP':'000010', 'instCode':'000000'},
    'JAL':  { 'OP':'000011', 'instCode':'000000'},
    'BEQ':  { 'OP':'000100', 'instCode':'000000'},
    'ANDI': { 'OP':'001100', 'instCode':'000000'},
    'ORI':  { 'OP':'001101', 'instCode':'000000'}
}

def readFiles():
    ensamblador = open("instruccionesEnsamblador.asm", "r")
    codigoMaquina = open("instruccionesBinario.bin","w+")
    return