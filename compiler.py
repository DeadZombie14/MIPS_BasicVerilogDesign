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

class Main:
    def __init__(self):
        self.leerArchivos()
        pass

    def leerArchivos(self):
        ensamblador = open("instruccionesEnsamblador.asm", "r")
        codigoMaquina = open("instruccionesBinario.bin","w+")
        i = 0
        for line in ensamblador:
            print(line.rstrip())
            if line.rstrip() != "":
                if line.rstrip()[0] != "#":
                    #Cortar la primer palabra de instrucción y leerla
                    binarioInstr = self.leerInstruccion(line)
                    print(binarioInstr)
                    # Dividir cada linea en N caracteres
                    for j in range(0, len(binarioInstr), corteLinea):
                        lineaNueva = binarioInstr[j:j+corteLinea]
                        codigoMaquina.write(lineaNueva)
                        codigoMaquina.write("\n")
                        i = i + 1
        # Completar la memoria de instrucciones con 0
        for k in range(i,lineasMinimas,1):
            lineaVacia = "0" * corteLinea
            codigoMaquina.write(lineaVacia)
            #Evitar escribir más de las lineas minimas
            if k != lineasMinimas-1:
                codigoMaquina.write("\n")
        ensamblador.close()
        codigoMaquina.close()

    def leerInstruccion(self,linea):
        instruccion = linea.split()[0]
        op = ""
        instCode = ""
        shamt = ""
        if instruccion.upper() == "ADD":
            op = "000000"
            instCode = "100000"
            shamt = "00000"
            parametros = self.leerParametros(op, linea)
            return op + espaciado + parametros + shamt + espaciado  + instCode
        elif instruccion.upper() == "SUB":
            op = "000000"
            instCode = "100010"
            shamt = "00000"
            parametros = self.leerParametros(op, linea)
            return op + espaciado + parametros + shamt + espaciado  + instCode
        elif instruccion.upper() == "MUL":
            op = "000000"
            instCode = "000010"
            shamt = "00000"
            parametros = self.leerParametros(op, linea)
            return op + espaciado + parametros + shamt + espaciado  + instCode
        elif instruccion.upper() == "DIV":
            op = "000000"
            instCode = "011010"
            shamt = "00000"
            parametros = self.leerParametros(op, linea)
            return op + espaciado + parametros + shamt + espaciado  + instCode
        elif instruccion.upper() == "AND":
            op = "000000"
            instCode = "100100"
            shamt = "00000"
            parametros = self.leerParametros(op, linea)
            return op + espaciado + parametros + shamt + espaciado  + instCode
        elif instruccion.upper() == "OR":
            op = "000000"
            instCode = "100101"
            shamt = "00000"
            parametros = self.leerParametros(op, linea)
            return op + espaciado + parametros + shamt + espaciado  + instCode
        elif instruccion.upper() == "NOR":
            op = "000000"
            instCode = "100111"
            shamt = "00000"
            parametros = self.leerParametros(op, linea)
            return op + espaciado + parametros + shamt + espaciado  + instCode
        elif instruccion.upper() == "SLL":
            op = "000000"
            instCode = "000000"
            shamt = "00000"
            parametros = self.leerParametros(op, linea)
            return op + espaciado + shamt + espaciado  + parametros + instCode
        elif instruccion.upper() == "SRL":
            op = "000000"
            instCode = "000011"
            shamt = "00000"
            parametros = self.leerParametros(op, linea)
            return op + espaciado + shamt + espaciado  + parametros + instCode
        elif instruccion.upper() == "SLT":
            op = "000000"
            instCode = "101010"
            shamt = "00000"
            parametros = self.leerParametros(op, linea)
            return op + espaciado + parametros + shamt + espaciado  + instCode
        elif instruccion.upper() == "XOR":
            op = "000000"
            instCode = "100110"
            shamt = "00000"
            parametros = self.leerParametros(op, linea)
            return op + espaciado + parametros + shamt + espaciado  + instCode

    def leerParametros(self, op, linea):
        parametros = ""
        if op == "000000":
            # Cortar parametros de la instruccion
            for palabra in linea.split():
                if palabra[0] == "$":
                    palabra = palabra[1:] # Cortar el signo $
                    if palabra[-1] == ",":
                        palabra = palabra[:-1] # Cortar el signo ,
                    parametros = parametros + f"{int(palabra):05b}" + espaciado
            return parametros

# Primera función que se ejecuta
# Aqui se hacen todas las llamadas a las clases
Aplicacion = Main()
