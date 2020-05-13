`timescale 1ns/1ps // Definir escala de tiempo
module SignE_TB();

// === Señales ===

//Registros
reg [15:0]aluSelSETB;
//Conexiones
wire [31:0]resSignoExtendido;
//Instancia
SignE extensorSignoTB(.inputSignE(aluSelSETB),.outputSignE(resSignoExtendido));

initial
	begin
    aluSelSETB = 16'b1000000000000001;

    #400    
	$stop;
	end
endmodule
