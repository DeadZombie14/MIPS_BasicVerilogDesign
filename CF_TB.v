`timescale 1ns/1ps // Definir escala de tiempo
module CF_TB();

// === Señales ===

//Registros
reg clk_CFTB;
//Conexiones
wire [7:0]instAddrCFTB;
wire [5:0]op_CFTB;
wire [4:0]rsCFTB, rtCFTB, rdCFTB, shamtCFTB;
wire [5:0]functCFTB;
//Instancia
CF cftb(.initialPCCF(8'b00000000),.clk_CF(clk_CFTB),.rsCF(rsCFTB),.rtCF(rtCFTB),.rdCF(rdCFTB),.shamtCF(shamtCFTB),.functCF(functCFTB),.op_CF(op_CFTB),.MemAddrRegCF(instAddrCFTB));
always #10 clk_CFTB = !clk_CFTB;

initial
	begin
    clk_CFTB = 1'b0;
	$readmemb("D:/intelFPGA/CF-DE-EX/instruccionesBinario.bin", cftb.IMCF.instBank);
	#30 // Dar tiempo a cargar la memoria.

    #400    
	$stop;
	end
endmodule
