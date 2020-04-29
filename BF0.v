// Def I/O
module BF0(
    input [31:0]dIn1_BF0,
    input clk_BF0,
	output reg [4:0]rsBF0, rtBF0, rdBF0, shamtBF0,
    output reg [5:0]opBF0, functBF0
);
// Conexiones 


// Cuerpo del modulo
always@(posedge clk_BF0)
begin
   opBF0 <= dIn1_BF0[31:26];
   rsBF0 <= dIn1_BF0[25:21];
   rtBF0 <= dIn1_BF0[20:16];
   rdBF0 <= dIn1_BF0[15:11];
   shamtBF0 <= dIn1_BF0[10:6];
   functBF0 <= dIn1_BF0[5:0];
end
//31 30 29 28 27 26  OP
//25 24 23 22 21     RS
//20 19 18 17 16     RT
//15 14 13 12 11     RD
//10 9  8  7  6      SH
//5  4  3  2  1  0   FUNCTION
endmodule
