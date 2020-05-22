// Def I/O
module BF0(
    input [31:0]instruction_BF0_IN,
    input clk_BF0,
    input [7:0]nextInst_BF0_IN,
    output reg [7:0]nextInst_BF0,
	output reg [4:0]rs_BF0, rt_BF0, rd_BF0,
    output reg [5:0]op_BF0,
    output reg [15:0]rdshfunct_BF0,
    output reg [25:0]target_BF0
);
// Conexiones 


// Cuerpo del modulo
always@(posedge clk_BF0)
begin
   nextInst_BF0 <= nextInst_BF0_IN[7:0];
   op_BF0 <= instruction_BF0_IN[31:26];
   rdshfunct_BF0 <= instruction_BF0_IN[15:0];
   rs_BF0 <= instruction_BF0_IN[25:21];
   rt_BF0 <= instruction_BF0_IN[20:16];
   rd_BF0 <= instruction_BF0_IN[15:11];
   target_BF0 <= instruction_BF0_IN[25:0];
end
//31 30 29 28 27 26  OP
//25 24 23 22 21     RS
//20 19 18 17 16     RT
//15 14 13 12 11     RD
//10 9  8  7  6      SH
//5  4  3  2  1  0   FUNCTION
endmodule
