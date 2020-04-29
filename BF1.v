// Def I/O
module BF1(
    input [31:0]dIn1_BF1,dIn2_BF1,
    input [3:0]dIn3_BF1,
    input [4:0]dIn4_BF1,
    input [4:0]dIn5_BF1,
    input clk_BF1,
	output reg [31:0]data1BF1,data2BF1,
    output reg [3:0]selBF1,
    output reg [4:0]rdBF1,
    output reg [4:0]shamtBF1
);
// Conexiones 


// Cuerpo del modulo
always@(posedge clk_BF1)
begin
   data1BF1 <= dIn1_BF1;
   data2BF1 <= dIn2_BF1;
   selBF1 <= dIn3_BF1; // sel de ALU
   rdBF1 <= dIn4_BF1; // rd
   shamtBF1 <= dIn5_BF1; // shamt
end

endmodule
