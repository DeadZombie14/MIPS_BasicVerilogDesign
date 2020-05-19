`timescale 1ns/1ps // Definir escala de tiempo
module DatapathI_TB();

reg clk = 1;
wire [31:0]resultado;

CPUControlRType DatapathI_TB(.clk_CPU(clk),.resultado(resultado));

always #10 clk = !clk;

initial
    begin
    $readmemb("C:/Users/aleja/OneDrive/Documentos/GitHub/MIPS_BasicVerilogDesign/TestF1_BReg.mem",DatapathI_TB.BR.registerBank);
    $readmemb("C:/Users/aleja/OneDrive/Documentos/GitHub/MIPS_BasicVerilogDesign/TestF2_MemInstruct.mem",DatapathI_TB.IM.instBank);
	 $readmemb("C:/Users/aleja/OneDrive/Documentos/GitHub/MIPS_BasicVerilogDesign/dataMemory.mem",DatapathI_TB.DM.dataMemory);

    #30 //carga de memoria
    
    #400

    $stop;
    end
endmodule 