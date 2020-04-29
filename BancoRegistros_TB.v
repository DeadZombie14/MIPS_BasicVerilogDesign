`timescale 1ns/1ps // Definir escala de tiempo
module BancoRegistros_TB();

// === Señales ===

//Registros
reg [31:0]wrDataBRTB;
reg [4:0]rAddr1BRTB,rAddr2BRTB,wAddrBRTB;
reg regWriteFlagBRTB;
//Conexiones
wire dataOutBRTB1, dataOutBRTB2;
wire [31:0]reOutput;
//Instancia
BancoRegistros BRTB(.wrData(wrDataBRTB),.rAddr1(rAddr1BRTB),.rAddr2(rAddr2BRTB),.wAddr(wAddrBRTB),.regWriteFlag(regWriteFlagBRTB),.data1(dataOutBRTB1),.data2(dataOutBRTB2));

// === Patrones de pruebas ===

initial
	begin
	$readmemb("D:/intelFPGA/DE-EX/BancoRegistrosMem.txt", BRTB.registerBank);
	#30

	$stop;
	end
endmodule
