// Def I/O
module SUB32bit(
	input [31:0]aSub32bit, bSub32bit,
	output [31:0]sub32bit
);
// Conexiones


// Cuerpo del modulo
assign sub32bit[31:0] = aSub32bit[31:0] - bSub32bit[31:0];

endmodule 
