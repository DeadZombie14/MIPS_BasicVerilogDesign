# Ahorcado

# Inicializar programa
NOP $0, $0, $0
NOP $0, $0, $0
NOP $0, $0, $0
NOP $0, $0, $0
NOP $0, $0, $0

# Palabra: submarino
# Palabra2: laberinto
#for i:palabra: if palabra[i] == palabra2[i]: correctas++ else incorrectas++
main:
addi $0, $0, 8 # Tamaño de palabra1
beq $1, $0, 6 # Salir si ya no quedan letras
lw $2, 0($1) # Letra de palabra1
lw $3, 1($1) # Letra de palabra2
beq $2, $3, 2 # si las letras son iguales
addi $5, $5, 1 # Sumar 1 a los errores
addi $4, $4, 1 # Sumar 1 a los aciertos 

addi $1, $1, 1 # Siguientes letras
j main

salir:
    NOP $0, $0, $0



