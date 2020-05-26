/* verilator lint_off UNUSED */
//`timescale 1ns/1ps // Definir escala de tiempo
module DatapathJ_TB();

reg clk = 1;
wire [31:0]resultado;

CPUControlRType cpu(.clk_CPU(clk),.resultado(resultado));

//always #10 clk = !clk;

initial
    begin
    // $readmemb("/TestF1_BReg.mem",Datapath_TB.BR.registerBank);
    // $readmemb("/TestF3_MemInst.mem",Datapath_TB.IM.instBank);
	// $readmemb("/dataMemory.mem",Datapath_TB.DM.dataMemory);

    $stop;
    end
endmodule 