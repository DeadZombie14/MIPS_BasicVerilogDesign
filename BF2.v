// Def I/O
module BF2(
    input [31:0]dIn1_BF2,
    input dIn2_BF2, clk_BF2,
	output reg [31:0]dOut1_BF2,
    output reg dOut2_BF2
);
// Conexiones 


// Cuerpo del modulo
always@(posedge clk_BF2)
begin
   dOut1_BF2 <= dIn1_BF2;
   dOut2_BF2 <= dIn2_BF2;
end

endmodule
