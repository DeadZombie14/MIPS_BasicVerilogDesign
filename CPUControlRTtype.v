//Def I/O
module CPUControlRType(
input clk_CPU,
output [31:0]resultado
);

//Conexiones
wire [7:0]mux0_inputPC, PC_Ins, bf2_mux0, insaddr_mux0, bf0_bf1_1, bf1_add, add_bf2;
wire and_mux0, bf3_br2, bf1_mux1_1, bf1_mux2, ALU_bf2_1, bf2_and_2, bf2_and_1, bf2_dm_3, bf2_dm_4, bf3_mux3_1;
wire [31:0]insmem_bf0, SE_bf1, mux3_br, br_bf1_1, br_bf1_2, bf1_AC_2, bf1_mux1_2, bf1_ALU, mux1_ALU, sl_add, ALU_bf2_2, bf2_dm_1, bf2_dm_2, dm_bf3, bf3_mux3_2, bf3_mux3_3;
wire [5:0]bf0_uc;
wire [15:0]bf0_SE;
wire [4:0]bf0_br1, bf0_br2, bf0_bf1_2, bf3_br, bf1_mux2_2, bf1_mux2_1, mux2_bf2, bf2_bf3_2;
wire [2:0]bf1_bf2_2, uc_bf1_2;
wire [1:0]bf1_bf2_1, bf2_bf3_1, uc_bf1_3, bf1_AC_1;
wire [3:0]AC_ALU, uc_bf1_1;



//Cuerpo del modulo
PC PC_TR(.inputPC(mux0_inputPC),.clk_PC(clk_CPU),.outputPC(PC_Ins));
Mux0 MUX0(.input1_mux0(insaddr_mux0),.input2_mux0(bf2_mux0),.ctrlSignalmux0(and_mux0),.output_mux0(mux0_inputPC));
InstAdder INSA(.currentInst(PC_Ins),.nextInst(insaddr_mux0));
InstMemory IM(.instAddr(PC_Ins),.instruction(insmem_bf0));
BF0 bf0(.clk_BF0(clk_CPU),.nextInst_BF0_IN(insaddr_mux0),.instruction_BF0_IN(insmem_bf0),.nextInst_BF0(bf0_bf1_1),.op_BF0(bf0_uc),.rdshfunct_BF0(bf0_SE),.rs_BF0(bf0_br1),.rt_BF0(bf0_br2),.rd_BF0(bf0_bf1_2));
SignE SE(.inputSignE(bf0_SE),.outputSignE(SE_bf1));
BancoRegistros BR(.rAddr1(bf0_br1),.rAddr2(bf0_br2),.wAddr(bf3_br),.wrData(mux3_br),.regWriteFlag(bf3_br2),.regData1(br_bf1_1),.regData2(br_bf1_2));
Control UC(.op(bf0_uc),.EX(uc_bf1_1),.M(uc_bf1_2),.WB(uc_bf1_3));
BF1 bf1(.nextInst_BF1_IN(bf0_bf1_1),.regData1_BF1_IN(br_bf1_1),.regData2_BF1_IN(br_bf1_2),.rdshfunct_BF1_IN(SE_bf1),.rd_BF1_IN(bf0_bf1_2),.rt_BF1_IN(bf0_br2),.M_BF1_IN(uc_bf1_2),.EX_BF1_IN(uc_bf1_1),.WB_BF1_IN(uc_bf1_3),.clk_BF1(clk_CPU),.WB_BF1(bf1_bf2_1),.M_BF1(bf1_bf2_2),.ALUSrc_BF1(bf1_mux1_1),.ALUOp_BF1(bf1_AC_1),.RegDst(bf1_mux2),.nextInst_BF1(bf1_add),.regData1_BF1(bf1_ALU),.regData2_BF1(bf1_mux1_2),.rdshfunct_BF1(bf1_AC_2),.rd_BF1(bf1_mux2_2),.rt_BF1(bf1_mux2_1));
Mux2 MUX2(.ctrlSignalmux2(bf1_mux2),.input1_mux2(bf1_mux2_1),.input2_mux2(bf1_mux2_2),.output_mux2(mux2_bf2));
Mux1 MUX1(.ctrlSignalmux1(bf1_mux1_1),.input1_mux1(bf1_mux1_2),.input2_mux1(bf1_AC_2),.output_mux1(mux1_ALU));
SLL2 SL(.inputSLL2(bf1_AC_2),.outputSll2(sl_add));
ALUCTRL AC(.alu_in(bf1_AC_2),.alu_op_in(bf1_AC_1),.alu_out(AC_ALU));
Add1 ADD1(.xAdd1(bf1_add),.yAdd1(sl_add[7:0]),.resAdd1(add_bf2));
ALU alu(.x32bit(bf1_ALU),.y32bit(mux1_ALU),.sel(AC_ALU),.res32bit(ALU_bf2_2),.zf(ALU_bf2_1));
BF2 bf2(.resAdd1_BF2_IN(add_bf2),.zf_BF2_IN(ALU_bf2_1),.resALU_BF2_IN(ALU_bf2_2),.regData2_BF2_IN(bf1_mux1_2),.mux2Output_BF2_IN(mux2_bf2),.M_BF2_BF2_IN(bf1_bf2_2),.WB_BF2_BF2_IN(bf1_bf2_1),.clk_BF2(clk_CPU),.resAdd1_BF2(bf2_mux0),.zf_BF2(bf2_and_2),.resALU_BF2(bf2_dm_1),.regData2_BF2(bf2_dm_2),.mux2Output_BF2(bf2_bf3_2),.WB_BF2(bf2_bf3_1),.branch_BF2(bf2_dm_4),.MemRead_BF2(bf2_and_1),.MemWrite_BF2(bf2_dm_3));
DataMemory DM(.memAddr(bf2_dm_1),.memData(bf2_dm_2),.memReadFlag(bf2_dm_4),.memWriteFlag(bf2_dm_3),.data(dm_bf3));
BF3 bf3(.data_BF3_IN(dm_bf3),.resALU_BF3_IN(bf2_dm_1),.mux2Output_BF3_IN(bf2_bf3_2),.WB_BF3_IN(bf2_bf3_1),.clk_BF3(clk_CPU),.data_BF3(bf3_mux3_2),.resALU_BF3(bf3_mux3_3),.mux2Output_BF3(bf3_br),.RegWrite_BF3(bf3_br2),.MemtoReg_BF3(bf3_mux3_1));
Mux3 MUX3(.ctrlSignalmux3(bf3_mux3_1),.input1_mux3(bf3_mux3_2),.input2_mux3(bf3_mux3_3),.output_mux3(mux3_br));

assign and_mux0 = bf2_and_1 && bf2_and_2; //Compuerta and
assign resultado = mux3_br; //Salida para verificar el resultado

endmodule

