// TB diseñado para trabajar con quartus
`timescale 1ns/1ps // Definir escala de tiempo
module MIPSQUARTUS_TB();

reg clk = 1;
wire [31:0]resultado;

MIPS cpu(.clk_CPU(clk),.resultado(resultado));

always #10 clk = !clk;

initial
    begin
    $display("Iniciando...");
    $readmemb("C:/Users/luman/OneDrive/Documentos/GitHub/MIPS_BasicVerilogDesign/registerBankMemory.mem",cpu.BR.registerBank);
	$readmemb("C:/Users/luman/OneDrive/Documentos/GitHub/MIPS_BasicVerilogDesign/dataMemory.mem",cpu.DM.dataMemory);
    $readmemb("C:/Users/luman/OneDrive/Documentos/GitHub/MIPS_BasicVerilogDesign/instructionMemory.mem",cpu.IM.instBank);

    #1000
    $stop;
    end
endmodule