// El objetivo CF este módulo es probar el funcionamiento CFl ciclo fetch.
// CFf I/O
module CF(
	input [7:0]initialPCCF,
    input clk_CF,
    output [4:0]rsCF, rtCF, rdCF, shamtCF,
    output [5:0]functCF,op_CF,
    output reg [7:0]MemAddrRegCF
);
// Conexiones
wire [7:0]currentInstAddrCF;
wire [31:0]currentInstFromMemCF;
wire [7:0]nextInstAddrCF;


PC PCCF(.inputPC(MemAddrRegCF),.clk_PC(clk_CF),.outputPC(currentInstAddrCF));
InstAdder IACF(.currentInst(currentInstAddrCF),.nextInst(nextInstAddrCF));
InstMemory IMCF(.instAddr(currentInstAddrCF),.instruction(currentInstFromMemCF));
BF0 BF0CF(.dIn1_BF0(currentInstFromMemCF),.clk_BF0(clk_CF),.opBF0(op_CF),.rsBF0(rsCF),.rtBF0(rtCF),.rdBF0(rdCF),.shamtBF0(shamtCF),.functBF0(functCF));

always@*
begin
    if(nextInstAddrCF)
        MemAddrRegCF[7:0] <= nextInstAddrCF;
    else
        MemAddrRegCF[7:0] <= initialPCCF;
end

endmodule
