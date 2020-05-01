`timescale 1ns/1ps // Definir escala de tiempo
module CFDEEX_TB();

// === Señales ===
//


//Registros
reg clk_DETB,regWriteFlagDETB;
//Conexiones
wire [31:0]res_DETB;
wire [5:0]op_DETB;
wire zf_DETB;
//Instancia
CFDEEX cf_de_ex(.initPCvalue(8'b00000000),.clk_DE(clk_DETB),.regWriteFlagDE(regWriteFlagDETB),.res_DE(res_DETB),.op_DE(op_DETB),.zf_DE(zf_DETB));
always #10 clk_DETB = !clk_DETB;

initial
	begin
    clk_DETB = 1'b0;
	regWriteFlagDETB = 1'b1;
	$readmemb("D:/intelFPGA/CF-DE-EX/BancoRegistrosMem.bin", cf_de_ex.BRDE.registerBank);
	$readmemb("D:/intelFPGA/CF-DE-EX/instruccionesBinario.bin", cf_de_ex.IMDE.instBank);
	#30 // Dar tiempo a cargar la memoria.

    #400
    
	$stop;
	end
endmodule
