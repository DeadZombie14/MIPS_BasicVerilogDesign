`timescale 1ns/1ps // Definir escala de tiempo
module ALUCTRL_TB();

// === Señales ===

//Registros
reg [5:0]aluMIPS;
//Conexiones
wire [3:0]aluSelectorOut;
//Instancia
ALUCTRL aluctrltb(.alu_in(aluMIPS),.alu_out(aluSelectorOut));

// === Patrones de pruebas ===

/*
CODIGOS R FUNCT MIPS (cuando OP = 000000)

ADD 100000
SUB 100010
MUL 000010
DIV 011010
AND 100100
OR  100101
NOR 100111
SLL 000000
SRL 000011 // Cambiar en futuro
SLT 101010
XOR 100110

*/

initial
	begin
    aluMIPS = 6'b100000;
    #10
    aluMIPS = 6'b100010;
    #10
    aluMIPS = 6'b000010;
    #10
    aluMIPS = 6'b011010;
    #10
    aluMIPS = 6'b100100;
    #10
    aluMIPS = 6'b100101;
    #10
    aluMIPS = 6'b100111;
    #10
    aluMIPS = 6'b000000;
    #10
    aluMIPS = 6'b000011;
    #10
    aluMIPS = 6'b101010;
    #10
    aluMIPS = 6'b100110;
    #10
	$stop;
	end
endmodule
