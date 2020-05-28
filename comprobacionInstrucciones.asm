# Instrucciones para comprobar el funcionamiento del MIPS
# nop necesarios para la carga de memorias, y evitacion de arrores con jump
 nop $0, $0, $0
 nop $0, $0, $0
 nop $0, $0, $0
 nop $0, $0, $0
main:
 add $31, $30, $29 # Suma 10 + 20 = 30 <- Se guarda en $29
 sub $29, $28, $29 # Resta 30 - 5 = 25 <- Se guarda en $29
 div $29, $28, $27 # Divide 25 / 5 = 5 <- Se guarda en $27
 and $27, $27, $26 # Operacion 5 && 5 = 1 <- Se guarda en $26
 or $27, $0, $25 # Operacion 27 || 0 = 27 <- Se guarda en $25
 lw $22, 0($0) # Recupera el contenido de la posicion 0 en memoria (osea 35) y lo guarda en $22 
 addi $22, $22, 13 # Suma inmediata para sumarle a 35 el valor 13
 sw $22, 0($1) # Guarda el contenido de $22 en la pos 1 de la memoria de datos 
 beq $1, $1, 19 # Compara el valor 1 != 2, por lo tanto ignora beq (la primera vez)
 addi $1, $1, 1 # Suma 1 + 1 = 2 <- Se guarda en 1, esto con fin de salir del bucle de beq y pasar a la inst 19
 j main # Jump de regreso al bucle beq para evaluar de nuevo
 nop $0, $0, $0
 nop $0, $0, $0


 

 
 






































