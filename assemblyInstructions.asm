# Instrucciones
 NOP $0, $0, $0
 NOP $0, $0, $0
main:
 NOP $0, $0, $0
 NOP $0, $0, $0
# NOP necesarios para la carga de memorias, y evitacion de arrores con jump
 BEQ $1, $2, 9
# Compara el valor que esta en 1 != 2, por lo tanto ignora beq
 NOP $0, $0, $0
 NOP $0, $0, $0
 Add $30, $31, $29
# Suma 30 + 31 = 61 <- Se guarda en 29
 Sub $29, $29, $29
# Resta 61 - 61 = 0 <- Se guarda en 29
 Div $20, $10, $23
# Divide 20 / 10 = 2 <- Se guarda en 23
 AND $23, $23, $22
# Operacion 23 && 23 = 23 <- Se guarda en 22
 OR $22, $21, $20
 # Operacion 23 || 21 = 23 <- Se guarda en 20
 ADDI $30, $31, 1
# Suma inmediata de 30 + 1 = 31 <- Se guarda en 31
 ADD $1, $1, $1
# Suma 1 + 1 = 2 <- Se guarda en 1, esto con fin de salir del bucle de beq
 j main
# Jump de regreso al bucle beq para evaluar de nuevo
 NOP $0, $0, $0
 NOP $0, $0, $0


 
 




































