// Def I/O
module AND32bit(
	input [31:0]aAND32bit, bAND32bit,
	output [31:0]and32bit
);
// Conexiones


// Cuerpo del modulo
assign and32bit[31:0] = aAND32bit[31:0] & bAND32bit[31:0];

endmodule
