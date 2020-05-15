// // Def I/O
// module CFDEEX(
// 	input [7:0]initPCvalue,
//     input clk_DE, regWriteFlagDE,
// 	output [31:0]res_DE,
//     output [5:0]op_DE,
//     output zf_DE
// );
// // Conexiones
// wire [3:0]alu_sel;
// wire [4:0]rsDE, rtDE, rdDE, shamtDE;
// wire [5:0]functDE;
// wire [7:0]currentInstAddr, nextInstAddr;
// wire [31:0]currentInstFromMem;
// wire [31:0]readData1,readData2,alu_output;
// wire [31:0]readData3,readData4;
// wire [3:0]readData5;
// wire [4:0]readData6; // Direccion de escritura en el Banco de Registros
// wire [4:0]readData7; // shift amount salida BF1
// wire zf_DE_temp;
// reg [7:0]instMAR; // Instruction Memory Address Register [MAR]

// // Cuerpo del modulo

// PC PCDE(.inputPC(instMAR),.clk_PC(clk_DE),.outputPC(currentInstAddr));
// InstAdder IADE(.currentInst(currentInstAddr),.nextInst(nextInstAddr));
// InstMemory IMDE(.instAddr(currentInstAddr),.instruction(currentInstFromMem));
// BF0 BF0DE(.dIn1_BF0(currentInstFromMem),.clk_BF0(clk_DE),.opBF0(op_DE),.rsBF0(rsDE),.rtBF0(rtDE),.rdBF0(rdDE),.shamtBF0(shamtDE),.functBF0(functDE));
// BancoRegistros BRDE(.wrData(alu_output),.rAddr1(rsDE),.rAddr2(rtDE),.wAddr(readData6),.regWriteFlag(regWriteFlagDE),.data1(readData1),.data2(readData2));
// ALUCTRL aluctrlDE(.alu_in(functDE),.alu_out(alu_sel));
// BF1 BF1DE(.dIn1_BF1(readData1),.dIn2_BF1(readData2),.dIn3_BF1(alu_sel),.dIn4_BF1(rdDE),.dIn5_BF1(shamtDE),.clk_BF1(clk_DE),.data1BF1(readData3),.data2BF1(readData4),.selBF1(readData5),.rdBF1(readData6),.shamtBF1(readData7));
// ALU aluDE(.sel(readData5),.zf(zf_DE_temp),.x32bit(readData3),.y32bit(readData4),.shiftAmount(readData7),.res32bit(alu_output));
// BF2 BF2DE(.dIn1_BF2(alu_output),.dIn2_BF2(zf_DE_temp),.clk_BF2(clk_DE),.dOut1_BF2(res_DE),.dOut2_BF2(zf_DE));

// always@*
// begin
//     if(nextInstAddr)
//         instMAR[7:0] <= nextInstAddr;
//     else
//         instMAR[7:0] <= initPCvalue;
// end


// endmodule
