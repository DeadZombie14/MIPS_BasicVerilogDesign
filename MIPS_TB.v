/* verilator lint_off UNUSED */
//`timescale 1ns/1ps // Definir escala de tiempo
module MIPS_TB(
    input clkTB,
    output [31:0]resultadoTB
);

MIPS cpu(.clk_CPU(clkTB),.resultado(resultadoTB));

initial
    begin
    $display("Iniciando...");
    $dumpfile("dump.vcd");
    $dumpvars();
    $readmemb("registerBankMemory.mem",cpu.BR.registerBank);
	$readmemb("dataMemory.mem",cpu.DM.dataMemory);
    $readmemb("instructionMemory.mem",cpu.IM.instBank);

    //$stop;
    end
endmodule 