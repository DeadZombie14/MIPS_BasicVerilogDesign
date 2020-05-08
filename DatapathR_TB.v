`timescale 1ns/1ps // Definir escala de tiempo
module DatapathR();

reg clk_CPU_tb = 1;
wire [31:0]resultado_tb;

CPUControlRType DatapathTypeR(.clk_CPU(clk_CPU_tb),.resultado(resultado_tb));
always #10 clk_CPU_tb = !clk_CPU_tb; //Ciclos de reloj cada 20 ns

 initial
 	begin
 	$readmemb("C:/Users/luman/OneDrive/Documentos/GitHub/MIPS_BasicVerilogDesign/BancoRegistrosMem.bin", DatapathTypeR.BR.registerBank);
 	$readmemb("C:/Users/luman/OneDrive/Documentos/GitHub/MIPS_BasicVerilogDesign/instruccionesBinario.bin", DatapathTypeR.IM.instBank);
	#30 // Dar tiempo a cargar la memoria.

     #400
    
 	$stop;
 	end

endmodule 