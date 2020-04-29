`timescale 1ns/1ps // Definir escala de tiempo
module InstMemory_TB();

// === Señales ===
//Registros
reg [7:0]instAddrIMTB;
//Conexiones
wire [31:0]instructionIMTB;
//Instancia
InstMemory insmem(.instAddr(instAddrIMTB),.instruction(instructionIMTB));

initial
	begin
	$readmemb("D:/intelFPGA/CF-DE-EX/instruccionesBinario.o", insmem.instBank);
	#30 // Dar tiempo a cargar la memoria.
    
	instAddrIMTB = 8'b00000000;
	#10

	instAddrIMTB = 8'b00000100;
	#10

	instAddrIMTB = 8'b00001000;
	#10

	$stop;
	end
endmodule
