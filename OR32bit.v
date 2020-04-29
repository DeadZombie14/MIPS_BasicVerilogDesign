// Def I/O
module OR32bit(
	input [31:0]aOR32bit, bOR32bit,
	output [31:0]or32bit
);
// Conexiones


// Cuerpo del modulo
assign or32bit[31:0] = aOR32bit[31:0] | bOR32bit[31:0];

endmodule
