// Def I/O
module BF2(
    input [7:0]resAdd1_BF2_IN,
    input zf_BF2_IN,
    input [31:0]resALU_BF2_IN, concatenador_BF2_IN,
    input [31:0]regData2_BF2_IN,
    input [25:0]target_BF2_IN,
    input [4:0]mux2Output_BF2_IN,
    input [3:0]M_BF2_BF2_IN, //Señales de Unidad de control(M)
    input [1:0]WB_BF2_BF2_IN, //Señales de Unidad de control(WB)
    input clk_BF2,
	output reg [7:0]resAdd1_BF2,
    output reg zf_BF2, 
	output reg [31:0]resALU_BF2, concatenador_BF2,
	output reg [31:0]regData2_BF2,
    output reg [25:0]target_BF2,
	output reg [4:0]mux2Output_BF2,
	output reg [1:0]WB_BF2, //Señales de Unidad de control(WB)
    output reg branch_BF2,MemRead_BF2,MemWrite_BF2,jump_BF2
);
// Conexiones 


// Cuerpo del modulo
always@(posedge clk_BF2)
begin
   // ==== Señales de control ===
   WB_BF2 <= WB_BF2_BF2_IN[1:0];

   branch_BF2 <= M_BF2_BF2_IN[3];
   MemRead_BF2 <= M_BF2_BF2_IN[2];
   MemWrite_BF2 <= M_BF2_BF2_IN[1];
   jump_BF2 <= M_BF2_BF2_IN[0];
   // ===========================

   resAdd1_BF2 <= resAdd1_BF2_IN[7:0];
   zf_BF2 <= zf_BF2_IN;
   resALU_BF2 <= resALU_BF2_IN[31:0];
   regData2_BF2 <= regData2_BF2_IN[31:0];
   mux2Output_BF2 <= mux2Output_BF2_IN[4:0];
   concatenador_BF2 <= concatenador_BF2_IN; //Jump que va al multiplexor 4
   target_BF2 <= target_BF2_IN; // 26 bits de address de la instruccion

end

endmodule
