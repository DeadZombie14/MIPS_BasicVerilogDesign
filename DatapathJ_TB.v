`timescale 1ns/1ps // Definir escala de tiempo
module DatapathJ_TB();

reg clk = 1;
wire [31:0]resultado;

CPUControlRType Datapath_TB(.clk_CPU(clk),.resultado(resultado));

always #10 clk = !clk;

initial
    begin
    $readmemb("C:/Users/luman/OneDrive/Documentos/GitHub/MIPS_BasicVerilogDesign/TestF1_BReg.mem",Datapath_TB.BR.registerBank);
    $readmemb("C:/Users/luman/OneDrive/Documentos/GitHub/MIPS_BasicVerilogDesign/TestF3_MemInst.mem",Datapath_TB.IM.instBank);
	$readmemb("C:/Users/luman/OneDrive/Documentos/GitHub/MIPS_BasicVerilogDesign/dataMemory.mem",Datapath_TB.DM.dataMemory);

    #30 //carga de memoria
    
    #800

    $stop;
    end
endmodule 